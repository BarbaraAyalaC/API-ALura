from pydantic import BaseModel

class TopicBase(BaseModel):
    title: str
    description: str

class TopicCreate(TopicBase):
    pass

class TopicUpdate(TopicBase):
    pass

class Topic(TopicBase):
    id: int

    class Config:
        orm_mode = True
