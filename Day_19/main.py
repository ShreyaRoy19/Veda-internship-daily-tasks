from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
import models, schemas, database, auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Multi-User Task Management API")

@app.post("/register", response_model=schemas.TaskResponse) # or user response
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id, "username": db_user.username} # Simplify as needed

@app.post("/token", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode({"sub": user.username}, auth.SECRET_KEY, algorithm=auth.ALGORITHM) # use standard jose call
    return {"access_token": access_token, "token_type": "bearer"}

@post_task_endpoint = app.post("/tasks/", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_task = models.Task(**task.dict(), user_id=current_user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/", response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    # Ensures users only see their own tasks (Prevents IDOR)
    return db.query(models.Task).filter(models.Task.user_id == current_user.id).all()

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this task")
    
    db.delete(task)
    db.commit()
    return {"detail": "Task deleted successfully"}
