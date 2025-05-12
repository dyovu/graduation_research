from database import Base, db_engine
from backend.models.body_parts import RightArm, RightArmTurn, LeftArmTurn
# from backend.models.choreography import ClapOverHead, DownTwoTimes, FrontBack, Jump, LeftArmAndLegSide, RightArmAndLegSide
# from backend.models.choreography_nc import ClapOverHead, DownTwoTimes, FrontBack, Jump, LeftArmAndLegSide, RightArmAndLegSide
from backend.models.choreography_pq import ClapOverHead, DownTwoTimes, FrontBack, Jump, LeftArmAndLegSide, RightArmAndLegSide, SideWalk


# def reset_database():
#     Base.metadata.drop_all(bind=db_engine)
#     Base.metadata.create_all(bind=db_engine)


# def reset_right_arm_turn_table():
#     RightArmTurn.__table__.create(bind=db_engine)

# def reset_left_arm_turn_table():
#     LeftArmTurn.__table__.create(bind=db_engine)



# 振り付けデータのテーブルを作る関数、データの中身を入れ替える際は上を参考にdropしよう
def drop_all_coreography():
    Base.metadata.drop_all(bind=db_engine, tables={ClapOverHead.__table__, DownTwoTimes.__table__, FrontBack.__table__, Jump.__table__, LeftArmAndLegSide.__table__, RightArmAndLegSide.__table__})

def create_all_coreography():
    Base.metadata.create_all(bind=db_engine, tables={ClapOverHead.__table__, DownTwoTimes.__table__, FrontBack.__table__, Jump.__table__, LeftArmAndLegSide.__table__, RightArmAndLegSide.__table__})

def create_ClapOverHead():
    ClapOverHead.__table__.create(bind=db_engine)

def create_DownTwoTimes():
    DownTwoTimes.__table__.create(bind=db_engine)

def create_FrontBack():
    FrontBack.__table__.create(bind=db_engine)

def create_Jump():
    Jump.__table__.create(bind=db_engine)

def create_LeftArmAndLegSide():
    LeftArmAndLegSide.__table__.create(bind=db_engine)

def create_RightArmAndLegSide():
    RightArmAndLegSide.__table__.create(bind=db_engine)

def create_SideWalk():
    SideWalk.__table__.create(bind=db_engine)


def exec():
    create_SideWalk()
    print("OK")
    pass


exec()
