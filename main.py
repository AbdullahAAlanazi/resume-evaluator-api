from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import auth, evaluate

app = FastAPI(title="Resume Evaluator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(evaluate.router, tags=["evaluate"])


@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}


@app.get("/ping")
def ping():
    return {"status": "ok"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}