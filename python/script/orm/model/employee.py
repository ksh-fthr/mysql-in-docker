import sys

from sqlalchemy import Column, String, Integer, DateTime

sys.path.append("./script")
from orm.preparation import Base


##
# モデル
#
class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(100))
    phone = Column(String(100))
    created_at = Column(DateTime())
    updated_at = Column(DateTime())

    def __repr__(self):
        return "<Employee (id={}, name='{}', phone='{}'".format(self.id, self.name, self.phone)
