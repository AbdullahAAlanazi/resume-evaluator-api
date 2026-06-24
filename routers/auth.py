from fastapi import APIRouter, HTTPException, status
from schemas import RegisterRequest, LoginRequest, UserResponse, TokenResponse
from store import users

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(request: RegisterRequest):
    if request.email in users:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    users[request.email] = {
        "email": request.email,
        "password": request.password,
        "role": "user"
    }

    return UserResponse(email=request.email, role="user")


@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):
    return TokenResponse(access_token="fake-token")