from database import Base, db_engine
from backend.models.body_parts import RightArm, RightArmTurn, LeftArmTurn

# 
# 
# RightArmTurn.__table__.drop(bind=db_engine)


# def reset_database():
#     Base.metadata.drop_all(bind=db_engine)
#     Base.metadata.create_all(bind=db_engine)

# def reset_right_arm_turn_table():
#     RightArmTurn.__table__.create(bind=db_engine)

def reset_left_arm_turn_table():
    LeftArmTurn.__table__.create(bind=db_engine)


reset_left_arm_turn_table()