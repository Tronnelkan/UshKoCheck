from sqlalchemy import BigInteger, Column, String, Boolean, Integer
from sqlalchemy.orm import relationship

from app.core.database import Base


class Users(Base):
    __tablename__ = 'users'
    id_telegram = Column(BigInteger, primary_key=True)
    fullname = Column(String, nullable=True, default='0')
    username = Column(String, nullable=True, default='0')
    subscription_is_active = Column(Boolean, nullable=True, default=False)
    subscription_active_to = Column(String, nullable=True)
    fop_name = Column(String, nullable=True)
    iban = Column(String, nullable=True)
    edrpou = Column(String, nullable=True)
    email = Column(String, nullable=True)
    path_to_logo = Column(String, nullable=True)
    free_invoices = Column(Integer, default=5, nullable=False)
