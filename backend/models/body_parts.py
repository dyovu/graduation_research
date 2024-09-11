from sqlalchemy import JSON, Column, DateTime, Double, Integer
from sqlalchemy.orm import relationship
from sql_app.database import Base


# ここはデータベースのテーブルごとのクラスをつくる
# 本当はテーブルごとのまとまりとしてファイルを作るはず

class RightArm(Base):
    __tablename__ = "right_arms"

    id = Column(Integer, primary_key=True, index = True)
    uttm = Column(DateTime, nullable=False)
    r_shoulder = Column(JSON, nullable=False)
    r_uparm = Column(JSON, nullable=False)
    r_lowarm = Column(JSON, nullable=False)
    r_hand = Column(JSON, nullable=False)