from sqlalchemy.orm import Session
from . import models, schemas

def create_topic(db: Session, topic: schemas.TopicCreate):
    db_topic = models.Topic(title=topic.title, description=topic.description)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic

def get_topics(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Topic).offset(skip).limit(limit).all()

def get_topic(db: Session, topic_id: int):
    return db.query(models.Topic).filter(models.Topic.id == topic_id).first()

def update_topic(db: Session, topic_id: int, topic: schemas.TopicUpdate):
    db_topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    if db_topic:
        db_topic.title = topic.title
        db_topic.description = topic.description
        db.commit()
        db.refresh(db_topic)
    return db_topic

def delete_topic(db: Session, topic_id: int):
    db_topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    if db_topic:
        db.delete(db_topic)
        db.commit()
    return db_topic
