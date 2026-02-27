from src.config.mongo import collections
from datetime import datetime, timezone
from argon2 import PasswordHasher


def insert_new_acc(name: str, email: str, password: str) -> str:
    ph = PasswordHasher()
    password_hashed = ph.hash(password)
    result = collections('users').insert_one({
        'name': name,
        'avatar': None,
        'email': email,
        'password': password_hashed,
        'created_at': datetime.now(timezone.utc),
        'updated_at': None
    })
    return result.inserted_id


def find_by_id(oid):
    user = collections('users').find_one({'_id': oid})
    return user


def find_by_email(email):
    user = collections('users').find_one({'email': email})
    return user