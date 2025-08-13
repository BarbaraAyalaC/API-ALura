from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, crud, schemas, database, auth

app = FastAPI()

# Crear la base de datos
models.Base.metadata.create_all(bind=database.engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/topics/", response_model=schemas.Topic)
def create_topic(topic: schemas.TopicCreate, db: Session = Depends(get_db), user: dict = Depends(auth.verify_token)):
    return crud.create_topic(db=db, topic=topic)

@app.get("/topics/", response_model=list[schemas.Topic])
def read_topics(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_topics(db=db, skip=skip, limit=limit)

@app.get("/topics/{topic_id}", response_model=schemas.Topic)
def read_topic(topic_id: int, db: Session = Depends(get_db)):
    db_topic = crud.get_topic(db=db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_topic

@app.put("/topics/{topic_id}", response_model=schemas.Topic)
def update_topic(topic_id: int, topic: schemas.TopicUpdate, db: Session = Depends(get_db), user: dict = Depends(auth.verify_token)):
    db_topic = crud.update_topic(db=db, topic_id=topic_id, topic=topic)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_topic

@app.delete("/topics/{topic_id}", response_model=schemas.Topic)
def delete_topic(topic_id: int, db: Session = Depends(get_db), user: dict = Depends(auth.verify_token)):
    db_topic = crud.delete_topic(db=db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_topic
