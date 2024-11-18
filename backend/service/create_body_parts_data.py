# # from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# import queue
# from typing import Optional

# import backend.schemas.body_parts as body_parts_schemas
# import backend.models.body_parts as body_parts_models


# # -----------------
# # 右手
# # -----------------
# def insert_right_arm(db: Session, q: queue.Queue, max_rows: Optional[int] = None):
#     db_objs = []
#     count = 0
#     while not q.empty() and (max_rows is None or count < max_rows):
#         insert_data = _create_right_arm(q)
#         db_obj = body_parts_models.RightArm(**insert_data.dict())
#         db_objs.append(db_obj)
#         count += 1

#     db.bulk_save_objects(db_objs)
#     db.commit()
#     # db.refresh(db_obj)
#     print(count)
#     return count

# def insert_right_arm_turn(db: Session, q: queue.Queue, max_rows: Optional[int] = None):
#     db_objs = []
#     count = 0
#     while not q.empty() and (max_rows is None or count < max_rows):
#         insert_data = _create_right_arm(q)
#         db_obj = body_parts_models.RightArmTurn(**insert_data.dict())
#         db_objs.append(db_obj)
#         count += 1

#     db.bulk_save_objects(db_objs)
#     db.commit()
#     # db.refresh(db_obj)
#     print(count)
#     return count

# def _create_right_arm(
#     q: queue.Queue,
# ):
#     tmp_data = q.get()
#     if not "fram" in tmp_data:
#         tmp_data = q.get()
#     uttm = tmp_data["fram"]["uttm"]
#     motion_data = tmp_data["fram"]["btrs"]
#     return body_parts_schemas.RightArmCreate(
#         uttm=uttm,
#         r_shoulder=motion_data[15]["tran"],
#         r_uparm=motion_data[16]["tran"],
#         r_lowarm=motion_data[17]["tran"],
#         r_hand=motion_data[18]["tran"]
#     )


# # -----------------
# # 左手
# # -----------------
# def insert_left_arm_turn(db: Session, q: queue.Queue, max_rows: Optional[int] = None):
#     db_objs = []
#     count = 0
#     while not q.empty() and (max_rows is None or count < max_rows):
#         insert_data = _create_left_arm(q)
#         db_obj = body_parts_models.LeftArmTurn(**insert_data.dict())
#         db_objs.append(db_obj)
#         count += 1

#     db.bulk_save_objects(db_objs)
#     db.commit()
#     # db.refresh(db_obj)
#     print(count)
#     return count

# def _create_left_arm(
#     q: queue.Queue,
# ):
#     tmp_data = q.get()
#     if not "fram" in tmp_data:
#         tmp_data = q.get()
#     uttm = tmp_data["fram"]["uttm"]
#     motion_data = tmp_data["fram"]["btrs"]
#     return body_parts_schemas.LeftArmCreate(
#         uttm=uttm,
#         l_shoulder=motion_data[11]["tran"],
#         l_uparm=motion_data[12]["tran"],
#         l_lowarm=motion_data[13]["tran"],
#         l_hand=motion_data[14]["tran"]
#     )