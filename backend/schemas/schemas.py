import datetime as dt

from pydantic import BaseModel, ConfigDict, Field


class RightArmBase(BaseModel):
    uttm: dt.datetime
    r_shoulder: list[float] = Field(..., min_items=7, max_items=7)
    r_uparm: list[float] = Field(..., min_items=7, max_items=7)
    r_lowarm: list[float] = Field(..., min_items=7, max_items=7)
    r_hand: list[float] = Field(..., min_items=7, max_items=7)

class RightArmCreate(RightArmBase):
    pass

class RightArmRead(RightArmBase):
    pass

