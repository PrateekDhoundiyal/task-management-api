from app.data.tasks import tasks
from app.schemas.task import Task,Status
def get_all_tasks(status:Status|None=None,skip:int=0,limit:int=10):
    if status is None:
        return tasks[skip:skip+limit]
    filtered=[]
    for task in tasks:
        if(task["status"]==status.value):
          filtered.append(task)
    return filtered[skip:skip+limit]
def get_task_by_id(task_id:int):
    for task in tasks:
         if(task["id"]==task_id):
           return task
    return None
def create_task(task:Task):
    #need to generate id by ourself a common approach is to give it a new id which equals to current length of
    #tasks -1
    #Note:This method for id generation is not realiable in real backend as it can cause reusability of id's due to deletion
    #we will use better method when we will use MySQL
    new_id=len(tasks)+1 #fixed using mysql
        #add this id into a dictionary
    new_task={
           "id":new_id,
           "title":task.title,
           "status":task.status.value
        }
    tasks.append(new_task)
    
    return new_task
def update_task(task_id:int ,updated_task:Task):
    for task in tasks:
        if(task["id"]==task_id):
             #update
            task["title"]=updated_task.title
            task["status"]=updated_task.status.value
            return task 
    return None