from datetime import date
from fastapi import FastAPI, Query
from typing import List
import pandas as pd
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datasets import mock_user_preferences
import db
from fastapi import HTTPException

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/top-destinations")
def get_top_destinations(group_id: int = Query(..., description="Group ID")):
    print(group_id)
    return {"top_destinations": {"Belgrade": "Test"}}


class UserRegistration(BaseModel):
    full_name: str
    email: str
    password: str
    dob: str
    gender: str


class UserLogin(BaseModel):
    email: str
    password: str


@app.post("/register")
def register_user(user: UserRegistration):
    # User registration logic
    print("registering user")
    print(user)
    response = db.register_user(user.dict())
    return {"message": "User registered successfully"}


@app.post("/login")
def login_user(user: UserLogin):
    # User login logic
    print("logging in user")
    print(user)
    response = db.login(user.dict())
    if response is None:
        raise HTTPException(status_code=401, detail="Invalid credentials!")

    return {"message": "User signed in successfully"}


# RUN APP: uvicorn main:app --reload
# uvicorn main:app  --reload --host 0.0.0.0 --port 8000
