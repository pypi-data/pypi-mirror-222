import json
#import boto3
import logging

from time import gmtime, strftime
from typing import Sequence, List, Dict#, Any, Union

import awswrangler as wr

from pandas import DataFrame
from boto3.session import Session

from aws_feature_store.feature_definition import (
    FeatureDefinition,
    #FeatureTypeEnum,
)

from aws_feature_store.inputs import (
    # OnlineStoreConfig,
    # OnlineStoreSecurityConfig,
    S3StorageConfig,
    OfflineStoreConfig,
    # DataCatalogConfig,
    # FeatureValue,
    # FeatureParameter,
)


class FeatureGroup:
    """FeatureGroup definition.

    This class instantiates a FeatureGroup object that comprises of a name for the FeatureGroup,
    session instance, and a list of feature definition objects i.e., FeatureDefinition.

    Attributes:
        name (str): name of the FeatureGroup instance.
        s3_uri (str): S3 URI of the offline store
        boto3_session (Session): session instance to perform boto calls.
        
    """

    def __init__(
        self,
        name: str,
        s3_uri: str,
        boto3_session: Session,
        use_date=False
        ):
        
        self.name = name
        self.s3_uri = s3_uri
        self.boto3_session = boto3_session
        self.use_date = use_date
        #==========================================
        
        bucket_name = s3_uri.replace('s3://','').split('/')[0]
        s3_folder = s3_uri.replace(f's3://{bucket_name}/','')
        
        if len(s3_folder)==0:
            raise FileNotFoundError(f'Folder {s3_folder}/ does not exist.')
        
        if s3_folder[-1]=='/':
            s3_folder = s3_folder[:-1]
        
        self.s3_folder = s3_folder
        self.bucket_name = bucket_name
        self.bucket = boto3_session.resource('s3').Bucket(bucket_name)
        
        #===set up utils functions ================
        json.load_s3 = lambda f: json.load(self.bucket.Object(key=f).get()["Body"])
        json.dump_s3 = lambda obj, f: self.bucket.Object(key=f).put(Body=json.dumps(obj))
        
        #===check bucket existance=================
        folder_exists=False
        for folder_exists in self.bucket.objects.filter(Prefix=f'{self.s3_folder}/'):
            break
        if not folder_exists:
            logging.error(f'Folder {s3_folder}/ does not exist.')
            raise FileNotFoundError(f'Folder {s3_folder}/ does not exist.')
                
        for folder in ['data','meta_data']:
            folder_exists=False
            for folder_exists in self.bucket.objects.filter(Prefix=f'{self.s3_folder}/{folder}/'):
                break
            if not folder_exists:
                logging.warning(f'Folder {s3_folder}/{folder}/ does not exist. Will be created')
                self.bucket.put_object(Key=f'{s3_folder}/{folder}/')
                 
        #===check if feature_group_exists===========
        exists_name = self.exists()
        if exists_name is not None:
            print(f'Found feature group {exists_name}')
            self.create_feature_store_args = json.load_s3(exists_name)
            self.name = exists_name.replace('/config.json','').replace(f'{s3_folder}/{folder}/','')
    
    
    def exists(self):
        #===check if feature_group_exists===========
        s3=self.boto3_session.client('s3')
        rsp = s3.list_objects_v2(Bucket=self.bucket_name, Prefix=f'{self.s3_folder}/data/{self.name}')#, Delimiter="/")
        if rsp['KeyCount']==0:
            return None
        
        objs=list(obj["Prefix"] for obj in rsp["CommonPrefixes"])
        
        #get last oblect
        key = objs[-1]
        key=key.replace('/data/','/meta_data/')
        
        objs = [o for o in self.bucket.objects.filter(Prefix=key)]
        if len(objs)==0:
            return None
        
        try:
            #print(f'Read config from {objs[-1].key}')
            json.load_s3(objs[-1].key)
        except Exception as exeption:
            print(f'Failed to read config for {self.name}\n{exeption}')
            return None
        
        return objs[-1].key
        

    def create(
        self,
        event_time_feature_name: str,
        record_identifier_name: str = None,
        description: str = None,
        feature_script_repo: str = None,
        data_source: str = None,
        file_format: str='json',
        partition_columns: List[str] = None,
        feature_definitions: Sequence[FeatureDefinition] = None,
        tags: List[Dict[str, str]] = None
    ):
        """sumary_line
        
        Keyword arguments:
            description: What is this feature group about
            feature_script_repo: link to the repo with script used to create the feature group
            data_source: description what data are used to create the feature group
            feature_definitions (Sequence[FeatureDefinition]): list of FeatureDefinitions.
            partition_columns: ordered list columns expected in data_frame which will be used for partitioning on S3
        
        Return: return_description
        """
        create_feature_store_args = dict(
            feature_group_name=self.name,
            record_identifier_name=record_identifier_name,
            event_time_feature_name=event_time_feature_name,
            feature_definitions=[
                feature_definition.to_dict() for feature_definition in feature_definitions
            ],
            partition_columns=partition_columns,
            description=description,
            feature_script_repo=feature_script_repo,
            data_source=data_source,
            tags=tags,
            file_format=file_format
        )

        s3_uri = self.s3_uri
        
        #===check feature_group_exists===========
        if self.exists() is not None:
            raise
        #========================================
        
        fg_time = gmtime()
        fg_timestamp = strftime("%Y-%m-%d'T'%H:%M:%SZ", fg_time)
        
        #===create folder =======================
        self.name = f'{self.name}_{fg_timestamp}'
        self.bucket.put_object(Key=f'{self.s3_folder}/data/{self.name}/')
    
        #===create config =======================
        s3_storage_config = S3StorageConfig(s3_uri=s3_uri)
        offline_store_config = OfflineStoreConfig(
            s3_storage_config=s3_storage_config,
            data_catalog_config=None,
        )
        create_feature_store_args.update(
            {"offline_store_config": offline_store_config.to_dict()}
        )
        self.create_feature_store_args = create_feature_store_args
        
        #===record config to meta_data==========
        key = f'{self.s3_folder}/meta_data/{self.name}/config.json'
        json.dump_s3(create_feature_store_args, key)
        
        return create_feature_store_args
            
    def describe(
        self,
    ):
        """Describe a FeatureGroup in FeatureStore service.

        Returns:
            Response dict from service.
        """

        return self.create_feature_store_args
    
    def ingest_data_frame(
        self,
        data_frame: DataFrame,
        file_name: str
    ):
        """Ingest the content of a pandas DataFrame to feature store.

        Args:
            data_frame (DataFrame): data_frame to be ingested to feature store splited by biz_id.
            file_name (str): json name of the file to store on s3. (usually timestamp)
            
        Returns:
            Nothing.
        """
        # filter columns
        columns = [f['FeatureName'] for f in self.create_feature_store_args['feature_definitions']]
        
        # add event_time
        event_time_feature_name = self.create_feature_store_args['event_time_feature_name']
        partition_columns = self.create_feature_store_args['partition_columns']
        fg_time = gmtime()
        fg_timestamp = strftime("%Y-%m-%dT%H:%M:%SZ", fg_time)
        
        print(f'Writing features to {self.s3_uri}/data/{self.name}')
        file_format = self.create_feature_store_args['file_format']
        if partition_columns:
            for ids, g in data_frame.groupby(partition_columns):
                if isinstance(ids,tuple):
                    ids = [str(x) for x in ids]
                else:
                    ids = [str(ids)]
                    
                ids = [f'{x[0]}={x[1]}' for x in zip(partition_columns,ids)]
                ids_key = '/'.join(ids)
                
                if self.use_date:
                    key = f'{self.s3_uri}/data/{self.name}/{ids_key}/year={fg_time.tm_year}/month={fg_time.tm_mon}/day={fg_time.tm_mday}/{file_name}.{file_format}'#{fg_time.tm_hour}/
                else:
                    key = f'{self.s3_uri}/data/{self.name}/{ids_key}/{file_name}.{file_format}'#{fg_time.tm_hour}/
                        
                df = g[columns]
                df[event_time_feature_name] = fg_timestamp
                
                if file_format=='json':
                    wr.s3.to_json(df=df, path=key, boto3_session=self.boto3_session)
                elif file_format=='parquet':
                    wr.s3.to_parquet(df=df, path=key, boto3_session=self.boto3_session)
        else:
            if self.use_date:
                key = f'{self.s3_uri}/data/{self.name}/year={fg_time.tm_year}/month={fg_time.tm_mon}/day={fg_time.tm_mday}/{file_name}.{file_format}'#{fg_time.tm_hour}/
            else:
                key = f'{self.s3_uri}/data/{self.name}/{file_name}.{file_format}'
                    
            df = data_frame[columns]
            df[event_time_feature_name] = fg_timestamp
            
            if file_format=='json':
                wr.s3.to_json(df=df, path=key, boto3_session=self.boto3_session)
            elif file_format=='parquet':
                wr.s3.to_parquet(df=df, path=key, boto3_session=self.boto3_session)
                    
            