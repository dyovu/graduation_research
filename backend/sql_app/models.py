from sqlalchemy import JSON, Column, DateTime, Double, Integer
from sqlalchemy.orm import relationship

from sql_app.database import Base


class AllData(Base):
    __tablename__ = "alldata"

    id = Column(Integer, primary_key=True)
    uttm = Column(DateTime, nullable=False)
    bnid = Column(Integer, nullable=False)
    tran = Column(JSON, nullable=False)
