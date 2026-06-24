from fastapi import APIRouter, Depends, HTTPException, status

from auth_utils import create_access_token, get_current_user, hash_password, verify_password
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
        "hashed_password": hash_password(request.password),
        "role": "user"
    }

    return UserResponse(email=request.email, role="user")


@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):
    user = users.get(request.email)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(request.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = create_access_token(request.email)

    return TokenResponse(access_token=token)


@router.get("/me", response_model=UserResponse)
def get_me(current_user: str = Depends(get_current_user)):
    user = users.get(current_user)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return UserResponse(email=user["email"], role=user["role"])