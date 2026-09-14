from fastapi import APIRouter,Query,HTTPException
from app.schemas.task import Status,TaskResponse,Task,UpdateTask
from app.services.task_service import get_task_by_id,create_task,get_all_tasks,update_task as update_task_service,patch_task as patch_task_service,delete_by_id

router=APIRouter()
@router.get("/tasks",response_model=list[TaskResponse])
def get_tasks(status:Status|None=None,skip:int=Query(0,ge=0),limit:int=Query(10,gt=0)):
    return get_all_tasks(status,skip,limit)
@router.get("/tasks/{task_id}",response_model=TaskResponse)
def get_task(task_id:int):
 result=get_task_by_id(task_id)
 if result is None:
   raise HTTPException(status_code=404,detail="Task doesn't exist")
 return result
    #this can give error id the task_id is out of range
    #this should be handeled  HTTPException
    #if any id present in tasks and matches tast_id return else through error
    
#we can directly specify status code into the decorator , fastAPI lets us do that
@router.post("/tasks",status_code=201,response_model=TaskResponse)
def create_post(task:Task):
    result=create_task(task)
    return result
#PUT for updating the task | Need to change later behaves same as patch
@router.put("/tasks/{task_id}",response_model=TaskResponse)
def update_task(task_id: int,updated_task:Task):
   result=update_task_service(task_id,updated_task)
   if result is None:
    raise HTTPException(status_code=404,detail="Task doesn't exist")
   return result
#creating patch endpoint so that user can willingly update in parts
@router.patch("/tasks/{task_id}",response_model=TaskResponse)
def patch_task(task_id:int,updated_task:UpdateTask):
   result=patch_task_service(task_id,updated_task)
   if result is None:
    raise HTTPException(status_code=404,detail="Task doesn't exist")
   return result   
#DELETE for deleting tasks
@router.delete("/tasks/{task_id}",status_code=204)
def delete_task(task_id:int):
   result=delete_by_id(task_id)
   if result is None:
    raise HTTPException(status_code=404,detail="Task not found")
   return 
