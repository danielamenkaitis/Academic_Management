from functools import wraps
from fastapi import HTTPException

def transactional(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
            return result
        except Exception as e:
            self.db.rollback()
            if not isinstance(e, HTTPException):
                raise HTTPException(status_code=500)
            raise e
    return wrapper

def NotFound():
    raise HTTPException(status_code=404)