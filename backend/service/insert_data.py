from sqlalchemy.orm import Session
import queue

from sql_app.put_data import create_data


def insert_all_data(db: Session, q: queue.Queue):
  while not q.empty():
    one_data = q.get()
    #
    #入れた順にidを振っていくように修正する,多分schemaを変えてidだけDBの方で振り分ける
    #
    uttm = one_data['fram']['uttm']
    time = one_data['fram']['time']
    motion_data = one_data['fram']['btrs']
    insert_data = {'id': 1, 'uttm':uttm, 'time':time,
                  'hip' : motion_data[0]['tran'],
                  'torso1' : motion_data[1]['tran'],
                  'torso2' : motion_data[2]['tran'],
                  'torso3' : motion_data[3]['tran'],
                  'torso4' : motion_data[4]['tran'],
                  'torso5': motion_data[5]['tran'],
                  'torso6' : motion_data[6]['tran'],
                  'torso7': motion_data[7]['tran'],
                  'neck1': motion_data[8]['tran'],
                  'neck2': motion_data[9]['tran'],
                  'head': motion_data[10]['tran'],
                  'l_shoulder': motion_data[11]['tran'],
                  'l_uparm': motion_data[12]['tran'],
                  'l_lowarm': motion_data[13]['tran'],
                  'l_hand' : motion_data[14]['tran'],
                  'r_shoulder': motion_data[15]['tran'],
                  'r_uparm': motion_data[16]['tran'],
                  'r_lowarm': motion_data[17]['tran'],
                  'r_hand': motion_data[18]['tran'],
                  'l_upleg': motion_data[19]['tran'],
                  'l_lowleg': motion_data[20]['tran'],
                  'l_foot': motion_data[21]['tran'],
                  'l_toe': motion_data[22]['tran'],
                  'r_upleg': motion_data[23]['tran'],
                  'r_lowleg': motion_data[24]['tran'],
                  'r_foot': motion_data[25]['tran'],
                  'r_toe': motion_data[26]['tran'],
                  }
    create_data(db=db, alldata = insert_data)
    


def insert_some_data(db: Session, q: queue.Queue, n: int):
  while n>0:
    one_data = q.get()
    uttm = one_data['fram']['uttm']
    time = one_data['fram']['time']
    motion_data = one_data['fram']['btrs']
    insert_data = {'id': 1, 'uttm':uttm, 'time':time,
                  'hip' : motion_data[0]['tran'],
                  'torso1' : motion_data[1]['tran'],
                  'torso2' : motion_data[2]['tran'],
                  'torso3' : motion_data[3]['tran'],
                  'torso4' : motion_data[4]['tran'],
                  'torso5': motion_data[5]['tran'],
                  'torso6' : motion_data[6]['tran'],
                  'torso7': motion_data[7]['tran'],
                  'neck1': motion_data[8]['tran'],
                  'neck2': motion_data[9]['tran'],
                  'head': motion_data[10]['tran'],
                  'l_shoulder': motion_data[11]['tran'],
                  'l_uparm': motion_data[12]['tran'],
                  'l_lowarm': motion_data[13]['tran'],
                  'l_hand' : motion_data[14]['tran'],
                  'r_shoulder': motion_data[15]['tran'],
                  'r_uparm': motion_data[16]['tran'],
                  'r_lowarm': motion_data[17]['tran'],
                  'r_hand': motion_data[18]['tran'],
                  'l_upleg': motion_data[19]['tran'],
                  'l_lowleg': motion_data[20]['tran'],
                  'l_foot': motion_data[21]['tran'],
                  'l_toe': motion_data[22]['tran'],
                  'r_upleg': motion_data[23]['tran'],
                  'r_lowleg': motion_data[24]['tran'],
                  'r_foot': motion_data[25]['tran'],
                  'r_toe': motion_data[26]['tran'],
                  }
    create_data(db=db, alldata = insert_data)
    n -= 1

  