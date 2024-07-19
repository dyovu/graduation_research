from sql_app.database import get_db
from sql_app import schemas
from sql_app import models
from sqlalchemy.orm import Session


def create_data(db: Session, alldata :schemas.AllData):
  tmp_data = models.AllData(id = alldata['id'], uttm = alldata['uttm'], bnid = alldata['bnid'], tran = alldata['tran'])
  db.add(tmp_data)
  db.commit()
  db.refresh(tmp_data)
  return tmp_data
