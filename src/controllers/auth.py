from fastapi import APIRouter, Body, HTTPException
from src.models.auth import RegisterRequest, LoginRequest, ProfileResponse, ProfileWithTokenResponse
from src.services.auth import insert_new_acc, find_by_id, find_by_email
from argon2 import PasswordHasher
from cryptography.fernet import Fernet
from datetime import timedelta, datetime, timezone

import jwt
import os
import json

auth_router = APIRouter(tags=['Authentication'])


@auth_router.post('/api/auth/register', summary='to register new account')
async def register(body: RegisterRequest = Body()) -> ProfileResponse:
    oid = insert_new_acc(body.name, body.email, body.password)
    user = find_by_id(oid)
    return ProfileResponse(
        id=str(oid),
        name=user['name'],
        avatar=user['avatar'],
        email=user['email']
    )


@auth_router.post('/api/auth/login', summary='to login into system')
async def login(body: LoginRequest = Body()) -> ProfileWithTokenResponse:
    # verify email
    user = find_by_email(body.email)
    if user is None:
        raise HTTPException(401, 'Incorrect email or password')
    
    # verify password
    ph = PasswordHasher()
    try:
        ph.verify(user['password'], body.password)
    except Exception as e:
        raise HTTPException(401, 'Incorrect email or password') 
    
    # generate token
    data_str = json.dumps({'email': user['email'], 'id': str(user['_id'])})
    key = os.getenv('ENCRYPTION_KEY')

    f = Fernet(key.encode())
    data_encrypted = f.encrypt(data_str.encode()).decode()

    exp = datetime.now(timezone.utc) + timedelta(days=365)
    token = jwt.encode({'data': data_encrypted, 'exp': exp}, os.getenv('JWT_SECRET_KEY'), algorithm='HS256')

    return ProfileWithTokenResponse(
        id=str(user['_id']),
        name=user['name'],
        avatar=user['avatar'],
        email=user['email'],
        token=token
    )