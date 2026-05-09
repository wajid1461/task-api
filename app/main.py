from fastapi import FastAPI

app = FastAPI()

tasks = [
    {"id": 1, "title": "Learn Jenkins"},
    {"id": 2, "title": "Build CI Pipeline"}
]

@app.get("/")
def home():
    return {"message": "CI/CD Learning Project"}

@app.get("/tasks")
def get_tasks():
    return tasks