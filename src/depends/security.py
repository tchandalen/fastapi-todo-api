from fastapi.security import APIKeyHeader
from fastapi import Depends, HTTPException
from cryptography.fernet import Fernet
import jwt
import os
import json

api_key = APIKeyHeader(name='Authorization', auto_error=False)

async def is_valid_token(token: str = Depends(api_key)):
    try:
        data = jwt.decode(token, os.getenv('JWT_SECRET_KEY'), algorithms=['HS256'])
        
        str_encrypted = data['data']
        key = os.getenv('ENCRYPTION_KEY')

        f = Fernet(key.encode())
        data_json = f.decrypt(str_encrypted).decode()
        data_dict = json.loads(data_json) # email, id, role

        return data_dict
    except Exception as e:
        raise HTTPException(403)