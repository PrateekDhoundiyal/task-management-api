from enum import Enum
from pydantic import BaseModel,Field,field_validator

class Status(Enum):
   pending="pending"
   completed="completed"
#Task is a request model - decribes the data coming into api
#we can also control and validate what goes out of our API
#FastApi calls this a response Model
class TaskResponse(BaseModel):
   #task response can be list
   id:int
   title:str
   status:Status

class Task(BaseModel):
   title:str=Field(min_length=3)
   status:Status
   @field_validator("title")
   @classmethod
   def validate_title(cls,value):
      if value.strip()=='':
         raise ValueError("Title cannot contain only whitespaces")
      return value
class UpdateTask(BaseModel):
    title: str| None=Field(default=None,min_length=3)#remember this syntax
    status: Status | None = None
    @field_validator("title")
    @classmethod
    def validate_title(cls,value):
          if value is None:
             return value
          if value.strip()=='':
             raise ValueError("Title cannot contain only whitespaces")
          return value