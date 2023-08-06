__all__ = [
    'Storage',
    'InputConfig',
]

from pydantic import BaseModel, Field, model_validator
import datetime as datetime
from typing import Optional, Any, List

from junoplatform.io._driver import Pulsar as Pulsar, Opc as Opc, driver_cfg, Redis


class InputConfig(BaseModel):
    ''' InputConfig spec for JunoPlatform Runtime
    tags: OPC tags
    minutes: last n minutes of data
    items: last n records of data
    time_to: n minutes of data(or n items of data) to <time_to>, if not provided then default to now()
    inteval: algo schedule-interval in seconds

    '''
    tags: List[str]
    minutes: Optional[int] = Field(default=None, description='input data of last n minutes')
    items: Optional[int] = Field(default= None, description='input data of last n items')
    time_to: Optional[datetime.datetime] =Field(default= None, description='input data to time, default is now()')
    interval: int = Field(description='schedule interval in seconds')

    @model_validator(mode='before')
    def atleast_one(cls, values: 'dict[str, Any]') -> 'dict[str, Any]':
        if all([values.get('minutes'), values.get('items')]):
            raise ValueError("field 'minutes' or 'items' must be given")
        return values

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Storage(metaclass=Singleton):
    _cloud = None
    _opc = None
    _local = None

    @property
    def cloud(self):
        if not self._cloud:
            CloudStorage:Pulsar
            if 'pulsar' in driver_cfg:
                CloudStorage = Pulsar(**driver_cfg['pulsar'])
            else:
                CloudStorage = Pulsar(url='pulsar://192.168.101.157:6650')
            self._cloud = CloudStorage

        return self._cloud
    
    @property
    def opc(self):
        if not self._opc:     
            OpcWriter = Opc()
            self._opc = OpcWriter  
        
        return self._opc
    
    @property
    def local(self):
        if not self._local:
            _redis_cfg = {'host': '192.168.101.157', 'port': 6379, 'password': 'myredis', 'db': 0}
            if 'redis' in driver_cfg:
                _redis_cfg = driver_cfg['redis']
            self._local = Redis(**_redis_cfg)
        return self._local
