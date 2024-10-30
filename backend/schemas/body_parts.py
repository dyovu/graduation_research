import datetime as dt

from pydantic import BaseModel, ConfigDict, Field

# 右手
class RightArmBase(BaseModel):
    r_shoulder: list[float] = Field(..., min_items=7, max_items=7)
    r_uparm: list[float] = Field(..., min_items=7, max_items=7)
    r_lowarm: list[float] = Field(..., min_items=7, max_items=7)
    r_hand: list[float] = Field(..., min_items=7, max_items=7)

class RightArmCreate(RightArmBase):
    uttm: dt.datetime
    pass

class RightArmRead(RightArmBase):
    class Config:
        from_attributes = True 
    pass

# 左手
class LeftArmBase(BaseModel):
    l_shoulder: list[float] = Field(..., min_items=7, max_items=7)
    l_uparm: list[float] = Field(..., min_items=7, max_items=7)
    l_lowarm: list[float] = Field(..., min_items=7, max_items=7)
    l_hand: list[float] = Field(..., min_items=7, max_items=7)

class LeftArmCreate(LeftArmBase):
    uttm: dt.datetime
    pass

class LeftArmRead(LeftArmBase):
    class Config:
        from_attributes = True 
    pass
