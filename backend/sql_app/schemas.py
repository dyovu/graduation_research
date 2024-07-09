import datetime as dt

from pydantic import BaseModel, ConfigDict, Field

class AllData(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    uttm: dt.datetime
    bnid: int
    tran: list[float] = Field(..., min_items=7, max_items=7)