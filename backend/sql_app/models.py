from sqlalchemy import JSON, Column, DateTime, Double, Integer
from sqlalchemy.orm import relationship

from sql_app.database import Base


class AllData(Base):
    __tablename__ = "alldata"

    id = Column(Integer, primary_key=True)
    uttm = Column(DateTime, nullable=False)
    time = Column(DateTime, nullable=False)
    hip = Column(JSON, nullable=False)
    torso1 = Column(JSON, nullable=False)
    torso2 = Column(JSON, nullable=False)
    torso3 = Column(JSON, nullable=False)
    torso4 = Column(JSON, nullable=False)
    torso5 = Column(JSON, nullable=False)
    torso6 = Column(JSON, nullable=False)
    torso7 = Column(JSON, nullable=False)
    neck1 = Column(JSON, nullable=False)
    neck2 = Column(JSON, nullable=False)
    head = Column(JSON, nullable=False)
    l_shoulder = Column(JSON, nullable=False)
    l_uparm = Column(JSON, nullable=False)
    l_lowarm = Column(JSON, nullable=False)
    l_hand = Column(JSON, nullable=False)
    r_shoulder = Column(JSON, nullable=False)
    r_uparm = Column(JSON, nullable=False)
    r_lowarm = Column(JSON, nullable=False)
    r_hand = Column(JSON, nullable=False)
    l_upleg = Column(JSON, nullable=False)
    l_lowleg = Column(JSON, nullable=False)
    l_foot = Column(JSON, nullable=False)
    l_toe = Column(JSON, nullable=False)
    r_upleg = Column(JSON, nullable=False)
    r_lowleg = Column(JSON, nullable=False)
    r_foot = Column(JSON, nullable=False)
    r_toe = Column(JSON, nullable=False)

