# _*_ coding: utf-8 _*_

"""
user model
"""

import sqlalchemy
from sqlalchemy.orm import relationship

from models import BaseModel


class Item(BaseModel):
    __table_args__ = (
        sqlalchemy.Index("index_i_1", "name"),
    )

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(255), nullable=True)
    owner_id = sqlalchemy.Column(sqlalchemy.String(255), sqlalchemy.ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")
