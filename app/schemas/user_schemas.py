import datetime
from typing import List, Optional
from pydantic import BaseModel

from app.models.tables import Users


class UserCreate(BaseModel):
    id_telegram: int
    fullname: str
    username: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    subscription_is_active: Optional[bool] = None
    subscription_active_to: Optional[str] = None
    fop_name: Optional[str] = None
    iban: Optional[str] = None
    edrpou: Optional[str] = None
    email: Optional[str] = None
    path_to_logo: Optional[str] = None
    free_invoices: Optional[int] = None
