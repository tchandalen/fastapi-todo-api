from src.config.mongo import collections
from datetime import datetime, timezone

def insert_todo(title, oid_creator):
    result = collections('todos').insert_one({
        'title': title,
        'creator_id': oid_creator,
        'is_completed': False,
        'created_at': datetime.now(timezone.utc),
        'updated_at': None
    })
    return result.inserted_id


def find_by_id(oid):
    todo = collections('todos').find_one({'_id': oid})
    return todo


def find_all(oid):
    todos = collections('todos').find({'creator_id': oid}).to_list()
    return todos