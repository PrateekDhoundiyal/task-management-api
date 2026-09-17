from app.data.tasks import tasks
from app.schemas.task import Task,Status,UpdateTask
from app.models.task import TaskModel
from sqlalchemy.orm import Session
def get_all_tasks(status:Status|None=None,skip:int=0,limit:int=10,db:Session=None):
    query=db.query(TaskModel)#db.query lets us use query directly in database
    if status is not None:
        #this filters the rows by status is specific status is provided  in query parameter 
        query=query.filter(TaskModel.status==status.value)
    #pagination handelling with sql query prev we were doing it with our tasks list
    tasks=query.offset(skip).limit(limit).all()
    return tasks

def get_task_by_id(task_id:int,db:Session):
    query=db.query(TaskModel).filter(TaskModel.id==task_id).first()
    return query
def create_task(task:Task,db:Session):
    #need to generate id by ourself a common approach is to give it a new id which equals to current length of
    #tasks -1
    #Note:This method for id generation is not realiable in real backend as it can cause reusability of id's due to deletion
    #we will use better method when we will use MySQL
   # new_id=len(tasks)+1 #Temporary MySQL will handle IDs buffer
        #add this id into a dictionary
    new_task=TaskModel(
        title=task.title,
        status=task.status.value
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task
def update_task(task_id:int ,updated_task:Task):
    for task in tasks:
        if(task["id"]==task_id):
             #update
            task["title"]=updated_task.title
            task["status"]=updated_task.status.value
            return task 
    return None
def patch_task(task_id:int,updated_task:UpdateTask):
    for task in tasks:
        if(task["id"]==task_id):
                #update
            if updated_task.title is not None:
                task["title"]=updated_task.title
            if updated_task.status is not None:
                task["status"]=updated_task.status.value
            return task 
    return None
def delete_by_id(task_id:int):
    for task in tasks:
        if(task["id"]==task_id):
            tasks.remove(task)
            return True
    return None