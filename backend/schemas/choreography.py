from pydantic import BaseModel, Field
from typing import List


class ClapOverHead(BaseModel):
    l_shoulder: List[float] = Field(..., min_items=6, max_items=6)
    l_uparm: List[float] = Field(..., min_items=6, max_items=6)
    l_lowarm: List[float] = Field(..., min_items=6, max_items=6)
    l_hand: List[float] = Field(..., min_items=6, max_items=6)

    r_shoulder: list[float] = Field(..., min_items=6, max_items=6)
    r_uparm: List[float] = Field(..., min_items=6, max_items=6)
    r_lowarm: List[float] = Field(..., min_items=6, max_items=6)
    r_hand: List[float] = Field(..., min_items=6, max_items=6)

class ClapOverHeadCreate(ClapOverHead):
    pass

class ClapOverHeadRead(ClapOverHead):
    id: int

    class Config:
        orm_mode = True  
        from_attributes = True 



class DownTwoTimes(BaseModel):
    root: List[float] = Field(..., min_items=6, max_items=6)

    l_up_leg: List[float] = Field(..., min_items=6, max_items=6)
    l_low_leg: List[float] = Field(..., min_items=6, max_items=6)
    l_foot: List[float] = Field(..., min_items=6, max_items=6)
    l_toes: List[float] = Field(..., min_items=6, max_items=6)

    r_up_leg: List[float] = Field(..., min_items=6, max_items=6)
    r_low_leg: List[float] = Field(..., min_items=6, max_items=6)
    r_foot: List[float] = Field(..., min_items=6, max_items=6)
    r_toes: List[float] = Field(..., min_items=6, max_items=6)

class DownTwoTimesCreate(DownTwoTimes):
    pass

class DownTwoTimesRead(DownTwoTimes):
    id: int

    class Config:
        orm_mode = True  
        from_attributes = True 



class FrontBack(BaseModel):
    root: List[float] = Field(..., min_items=6, max_items=6)

    l_up_leg: List[float] = Field(..., min_items=6, max_items=6)
    l_low_leg: List[float] = Field(..., min_items=6, max_items=6)
    l_foot: List[float] = Field(..., min_items=6, max_items=6)
    l_toes: List[float] = Field(..., min_items=6, max_items=6)

    r_up_leg: List[float] = Field(..., min_items=6, max_items=6)
    r_low_leg: List[float] = Field(..., min_items=6, max_items=6)
    r_foot: List[float] = Field(..., min_items=6, max_items=6)
    r_toes: List[float] = Field(..., min_items=6, max_items=6)

class FrontBackCreate(FrontBack):
    pass

class FrontBackRead(FrontBack):
    id: int

    class Config:
        orm_mode = True  
        from_attributes = True 



class Jump(BaseModel):
    root: List[float] = Field(..., min_items=6, max_items=6)
    torso_1: List[float] = Field(..., min_items=6, max_items=6)
    torso_2: List[float] = Field(..., min_items=6, max_items=6)
    torso_3: List[float] = Field(..., min_items=6, max_items=6)
    torso_4: List[float] = Field(..., min_items=6, max_items=6)
    torso_5: List[float] = Field(..., min_items=6, max_items=6)

class JumpCreate(Jump):
    pass

class JumpRead(Jump):
    id: int

    class Config:
        orm_mode = True  
        from_attributes = True 



class LeftArmAndLegSide(BaseModel):
    l_shoulder: List[float] = Field(..., min_items=6, max_items=6)
    l_uparm: List[float] = Field(..., min_items=6, max_items=6)
    l_lowarm: List[float] = Field(..., min_items=6, max_items=6)
    l_hand: List[float] = Field(..., min_items=6, max_items=6)

    l_up_leg: List[float] = Field(..., min_items=6, max_items=6)
    l_low_leg: List[float] = Field(..., min_items=6, max_items=6)
    l_foot: List[float] = Field(..., min_items=6, max_items=6)
    l_toes: List[float] = Field(..., min_items=6, max_items=6)

class LeftArmAndLegSideCreate(LeftArmAndLegSide):
    pass

class LeftArmAndLegSideRead(LeftArmAndLegSide):
    id: int

    class Config:
        orm_mode = True  
        from_attributes = True 



class RightArmAndLegSide(BaseModel):
    r_shoulder: list[float] = Field(..., min_items=6, max_items=6)
    r_uparm: List[float] = Field(..., min_items=6, max_items=6)
    r_lowarm: List[float] = Field(..., min_items=6, max_items=6)
    r_hand: List[float] = Field(..., min_items=6, max_items=6)

    r_up_leg: List[float] = Field(..., min_items=6, max_items=6)
    r_low_leg: List[float] = Field(..., min_items=6, max_items=6)
    r_foot: List[float] = Field(..., min_items=6, max_items=6)
    r_toes: List[float] = Field(..., min_items=6, max_items=6)

class RightArmAndLegSideCreate(RightArmAndLegSide):
    pass

class RightArmAndLegSideRead(RightArmAndLegSide):
    id: int

    class Config:
        orm_mode = True  
        from_attributes = True 


