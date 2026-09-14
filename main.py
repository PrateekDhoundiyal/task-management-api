from fastapi import FastAPI,HTTPException,Query
from app.routers.tasks import router as task_router
from pydantic import BaseModel,Field,field_validator
from enum import Enum


app=FastAPI()#this creates fastAPI application
app.include_router(task_router)
#app is like the main object representing our api
#this below is a decorator that registers the home function as the handler for GET requests.
@app.get("/")# this is a route which tells FastAPI that if someone sends a GET request to /, execute the function below it.
def home():
    return {"message":"Task Management API is running"}#FastAPI converts this dictionary into JSON response 

   
