# _*_ coding: utf-8 _*_

"""
user model
"""

import sqlalchemy

from models import BaseModel


class User(BaseModel):
    __table_args__ = (
        sqlalchemy.Index("index_u_1", "name"),
        sqlalchemy.Index("index_u_2", "email"),
        sqlalchemy.Index("index_u_3", "phone"),
    )

    # basic
    id = sqlalchemy.Column(sqlalchemy.String(255), primary_key=True)
    pwd = sqlalchemy.Column(sqlalchemy.String(512), nullable=True)

    # information
    name = sqlalchemy.Column(sqlalchemy.String(255), nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String(255), nullable=True)
    phone = sqlalchemy.Column(sqlalchemy.String(255), nullable=True)
    avatar = sqlalchemy.Column(sqlalchemy.String(255), nullable=True)

    # others columns
    token_verify = sqlalchemy.Column(sqlalchemy.String(255), nullable=True)
    token_expire_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=True)
