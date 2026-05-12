from fastapi import Depends, FastAPI, Header, HTTPException
from sqlalchemy.orm import Session

from auth import create_access_token, decode_token, hash_password, verify_password
from database import Base, engine, get_db
from models import User
from schemas import TokenResponse, UserCreate, UserLogin, UserResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI JWT Auth API")


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # check if user already exists
    existing = db.query(User).filter(User.email == user_data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hash_password(user_data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/login", response_model=TokenResponse)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_data.email).first()

    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Wrong email or password")

    token = create_access_token({"sub": user.email})
    return TokenResponse(access_token=token)


def get_current_user(authorization: str = Header(default=None), db: Session = Depends(get_db)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token missing")

    token = authorization.replace("Bearer ", "")
    payload = decode_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    email = payload.get("sub")
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user


@app.get("/profile", response_model=UserResponse)
def profile(current_user: User = Depends(get_current_user)):
    return current_user
