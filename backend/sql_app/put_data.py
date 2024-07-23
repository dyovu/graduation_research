from sql_app.database import get_db
from sql_app import schemas
from sql_app import models
from sqlalchemy.orm import Session



def create_data(db: Session, alldata :schemas.AllData):
  tmp_data = models.AllData(
    id = alldata['id'],
    uttm = alldata['uttm'],
    time = alldata['time'],
    hip = alldata['hip'],
    torso1 = alldata['torso1'],
    torso2 = alldata['torso2'],
    torso3 =alldata['torso3'],
    torso4 = alldata['torso4'],
    torso5 = alldata['torso5'],
    torso6 = alldata['torso6'],
    torso7 = alldata['torso7'],
    neck1 = alldata['neck1'],
    neck2 = alldata['neck2'],
    head = alldata['head'],
    l_shoulder = alldata['l_shoulder'],
    l_uparm = alldata['l_uparm'],
    l_lowarm = alldata['l_lowarm'],
    l_hand = alldata['l_hand'],
    r_shoulder = alldata['r_shoulder'],
    r_lowarm = alldata['r_lowarm'],
    r_hand = alldata['r_hand'],
    l_upleg = alldata['l_upleg'],
    l_lowleg = alldata['l_lowleg'],
    l_foot = alldata['l_foot'],
    l_toe = alldata['l_toe'],
    r_upleg = alldata['r_upleg'],
    r_lowleg = alldata['r_lowleg'],
    r_foot = alldata['r_foot'],
    r_toe = alldata['r_toe'],
    )
  db.add(tmp_data)
  db.commit()
  db.refresh(tmp_data)
  return tmp_data



