# _*_ coding: utf-8 _*_

"""
models module
"""

from typing import Any

import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

from core.settings import settings

# define session
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@as_declarative
class BaseModel:
    __name__: str

    id: Any
    created_at: sqlalchemy.DateTime = sqlalchemy.Column(
        sqlalchemy.DateTime, default=func.now(), doc="Created At"
    )
    updated_at: sqlalchemy.DateTime = sqlalchemy.Column(
        sqlalchemy.DateTime, default=func.now(), onupdate=func.now(), doc="Updated At"
    )

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
