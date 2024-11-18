from sqlalchemy import JSON, Column, DateTime, Double, Integer
from sqlalchemy.orm import relationship

from backend.database import Base


class ClapOverHead(Base):
    __tablename__ = "clap_over_head_pq"

    id = Column(Integer, primary_key=True, index = True)
    l_shoulder = Column(JSON, nullable=False)
    l_uparm = Column(JSON, nullable=False)
    l_lowarm = Column(JSON, nullable=False)
    l_hand = Column(JSON, nullable=False)
    r_shoulder = Column(JSON, nullable=False)
    r_uparm = Column(JSON, nullable=False)
    r_lowarm = Column(JSON, nullable=False)
    r_hand = Column(JSON, nullable=False)


class DownTwoTimes(Base):
    __tablename__ = "down_two_times_pq"

    id = Column(Integer, primary_key=True, index = True)
    root = Column(JSON, nullable=False)

    l_up_leg = Column(JSON, nullable=False)
    l_low_leg = Column(JSON, nullable=False)
    l_foot = Column(JSON, nullable=False)
    l_toes = Column(JSON, nullable=False)

    r_up_leg = Column(JSON, nullable=False)
    r_low_leg = Column(JSON, nullable=False)
    r_foot = Column(JSON, nullable=False)
    r_toes = Column(JSON, nullable=False)


class FrontBack(Base):
    __tablename__ = "front_back_pq"

    id = Column(Integer, primary_key=True, index = True)
    root = Column(JSON, nullable=False)
    
    l_up_leg = Column(JSON, nullable=False)
    l_low_leg = Column(JSON, nullable=False)
    l_foot = Column(JSON, nullable=False)
    l_toes = Column(JSON, nullable=False)

    r_up_leg = Column(JSON, nullable=False)
    r_low_leg = Column(JSON, nullable=False)
    r_foot = Column(JSON, nullable=False)
    r_toes = Column(JSON, nullable=False)


class Jump(Base):
    __tablename__ = "jump_pq"

    id = Column(Integer, primary_key=True, index = True)

    root = Column(JSON, nullable=False)
    torso_1 = Column(JSON, nullable=False)
    torso_2 = Column(JSON, nullable=False)
    torso_3 = Column(JSON, nullable=False)
    torso_4 = Column(JSON, nullable=False)
    torso_5= Column(JSON, nullable=False)


class LeftArmAndLegSide(Base):
    __tablename__ = "l_arm_and_leg_side_pq"

    id = Column(Integer, primary_key=True, index = True)

    l_shoulder = Column(JSON, nullable=False)
    l_uparm = Column(JSON, nullable=False)
    l_lowarm = Column(JSON, nullable=False)
    l_hand = Column(JSON, nullable=False)

    l_up_leg = Column(JSON, nullable=False)
    l_low_leg = Column(JSON, nullable=False)
    l_foot = Column(JSON, nullable=False)
    l_toes = Column(JSON, nullable=False)


class RightArmAndLegSide(Base):
    __tablename__ = "r_arm_and_leg_side_pq"

    id = Column(Integer, primary_key=True, index = True)

    r_shoulder = Column(JSON, nullable=False)
    r_uparm = Column(JSON, nullable=False)
    r_lowarm = Column(JSON, nullable=False)
    r_hand = Column(JSON, nullable=False)

    r_up_leg = Column(JSON, nullable=False)
    r_low_leg = Column(JSON, nullable=False)
    r_foot = Column(JSON, nullable=False)
    r_toes = Column(JSON, nullable=False)

