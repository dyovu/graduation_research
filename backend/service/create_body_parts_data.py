from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import queue
from typing import Optional

import backend.schemas.body_parts as body_parts_schemas
import backend.models.body_parts as body_parts_models

def insert_right_arm(db: Session, q: queue.Queue, max_rows: Optional[int] = None):
    db_objs = []
    count = 0
    while not q.empty() and (max_rows is None or count < max_rows):
        insert_data = _create_right_arm(q)
        db_obj = body_parts_models.RightArm(**insert_data.dict())
        db_objs.append(db_obj)
        count += 1

    db.bulk_save_objects(db_objs)
    db.commit()
    # db.refresh(db_obj)
    print(count)
    return count

# -----------------
# motion_dataに関してどれが必要なのか確認する
# -----------------
def _create_right_arm(
    q: queue.Queue,
):
    tmp_data = q.get()
    if not "fram" in tmp_data:
        tmp_data = q.get()
    uttm = tmp_data["fram"]["uttm"]
    motion_data = tmp_data["fram"]["btrs"]
    return body_parts_schemas.RightArmCreate(
        uttm=uttm,
        r_shoulder=motion_data[15]["tran"],
        r_uparm=motion_data[16]["tran"],
        r_lowarm=motion_data[17]["tran"],
        r_hand=motion_data[18]["tran"]
    )
    