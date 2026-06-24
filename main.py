from fastapi import FastAPI

app = FastAPI(title="Resume Evaluator API")


@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}


@app.get("/ping")
def ping():
    return {"status": "ok"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}
