import datetime as dt

from pydantic import BaseModel, ConfigDict, Field

class AllData(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    uttm: dt.datetime
    time: int
    hip : list[float] = Field(..., min_items=7, max_items=7)
    torso1 : list[float] = Field(..., min_items=7, max_items=7)
    torso2 : list[float] = Field(..., min_items=7, max_items=7)
    torso3 : list[float] = Field(..., min_items=7, max_items=7)
    torso4 : list[float] = Field(..., min_items=7, max_items=7)
    torso5: list[float] = Field(..., min_items=7, max_items=7)
    torso6 : list[float] = Field(..., min_items=7, max_items=7)
    torso7: list[float] = Field(..., min_items=7, max_items=7)
    neck1: list[float] = Field(..., min_items=7, max_items=7)
    neck2: list[float] = Field(..., min_items=7, max_items=7)
    head: list[float] = Field(..., min_items=7, max_items=7)
    l_shoulder: list[float] = Field(..., min_items=7, max_items=7)
    l_uparm: list[float] = Field(..., min_items=7, max_items=7)
    l_lowarm: list[float] = Field(..., min_items=7, max_items=7)
    l_hand : list[float] = Field(..., min_items=7, max_items=7)
    r_shoulder: list[float] = Field(..., min_items=7, max_items=7)
    r_uparm: list[float] = Field(..., min_items=7, max_items=7)
    r_lowarm: list[float] = Field(..., min_items=7, max_items=7)
    r_hand: list[float] = Field(..., min_items=7, max_items=7)
    l_upleg: list[float] = Field(..., min_items=7, max_items=7)
    l_lowleg: list[float] = Field(..., min_items=7, max_items=7)
    l_foot: list[float] = Field(..., min_items=7, max_items=7)
    l_toe: list[float] = Field(..., min_items=7, max_items=7)
    r_upleg: list[float] = Field(..., min_items=7, max_items=7)
    r_lowleg: list[float] = Field(..., min_items=7, max_items=7)
    r_foot: list[float] = Field(..., min_items=7, max_items=7)
    r_toe: list[float] = Field(..., min_items=7, max_items=7)