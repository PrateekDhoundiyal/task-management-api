#This is based on ORM(Object-Relational Mapping)
#model-how data is represented in the database
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
class TaskModel(Base):
    __tablename__="tasks"#we already have create the table
    id: Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    title:Mapped[str]=mapped_column()
    status:Mapped[str]=mapped_column()