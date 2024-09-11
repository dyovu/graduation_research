from sqlalchemy.orm import Session
from sql_app import schemas, models
import queue

from backend.models import body_parts


def insert_right_arm(db: Session, q: queue.Queue, rightArms:schemas.RightArmCreate):
	# queueから右腕のデータのみを抽出してinset_dataとする
	insert_data = _create_right_arm_data(q)
	db_obj = body_parts.RightArm(**insert_data)
	db.add(db_obj)
	db.commit()
	db.refresh(db_obj)
	return db_obj

# -----------------
# uttmのdeserialiczeを治さないといけない、motion_dataに関してどれが必要なのかも
# -----------------

def _create_right_arm_data(
	q: queue.Queue
):
	if not q.empty():
		tmp_data = q.get()
	uttm = tmp_data['fram']['uttm']
	motion_data = tmp_data['fram']['btrs']
	retunr_data = {
		"uttm":uttm,
		'r_shoulder': motion_data[15]['tran'],
		'r_uparm': motion_data[16]['tran'],
		'r_lowarm': motion_data[17]['tran'],
		'r_hand': motion_data[18]['tran'],
		}
	return retunr_data
	