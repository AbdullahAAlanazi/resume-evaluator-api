from pydantic import BaseModel


class RegisterRequest(BaseModel):
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    email: str
    role: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class EvaluateRequest(BaseModel):
    job_description: str
    prompt: str = ""


class EvaluateResponse(BaseModel):
    result: str