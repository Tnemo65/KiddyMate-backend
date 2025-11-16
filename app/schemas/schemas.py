from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime
import enum

class TaskCategory(str, enum.Enum):
    IQ = "IQ"
    EQ = "EQ"

class TaskType(str, enum.Enum):
    LOGIC = "logic"
    EMOTION = "emotion"

class ChildTaskStatus(str, enum.Enum):
    SUGGESTED = "suggested"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    VERIFIED = "verified"

class RewardType(str, enum.Enum):
    BADGE = "badge"
    SKIN = "skin"
    COIN = "coin"

class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class UserPublic(UserInDB):
    pass

class ChildBase(BaseModel):
    name: str
    birth_date: datetime
    initial_traits: Optional[dict]

class ChildCreate(ChildBase):
    pass

class ChildInDB(ChildBase):
    id: str
    current_coins: int
    level: int
    model_config = ConfigDict(from_attributes=True)

class ChildPublic(ChildInDB):
    pass

class TaskBase(BaseModel):
    title: str
    description: str
    category: TaskCategory
    type: TaskType
    difficulty: int
    suggested_age_range: str

class TaskCreate(TaskBase):
    pass

class TaskInDB(TaskBase):
    id: str
    reward_coins: int = 50
    reward_badge_name: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class TaskPublic(TaskInDB):
    pass

class ChildTaskBase(BaseModel):
    status: ChildTaskStatus
    assigned_at: datetime
    completed_at: Optional[datetime]

class ChildTaskCreate(ChildTaskBase):
    child_id: int
    task_id: int

class ChildTaskInDB(ChildTaskBase):
    id: str
    model_config = ConfigDict(from_attributes=True)

class ChildTaskPublic(ChildTaskInDB):
    pass

class RewardBase(BaseModel):
    name: str
    description: str
    type: RewardType
    image_url: Optional[str]

class RewardCreate(RewardBase):
    pass

class RewardInDB(RewardBase):
    id: str
    model_config = ConfigDict(from_attributes=True)

class RewardPublic(RewardInDB):
    pass

class ChildRewardBase(BaseModel):
    earned_at: datetime

class ChildRewardCreate(ChildRewardBase):
    child_id: int
    reward_id: int

class ChildRewardInDB(ChildRewardBase):
    id: str
    model_config = ConfigDict(from_attributes=True)

class ChildRewardPublic(ChildRewardInDB):
    pass

class MiniGameBase(BaseModel):
    name: str
    description: str
    linked_skill: str

class MiniGameCreate(MiniGameBase):
    pass

class MiniGameInDB(MiniGameBase):
    id: str
    model_config = ConfigDict(from_attributes=True)

class MiniGamePublic(MiniGameInDB):
    pass

class GameSessionBase(BaseModel):
    start_time: datetime
    end_time: Optional[datetime]
    score: Optional[int]
    behavior_data: Optional[dict]

class GameSessionCreate(GameSessionBase):
    child_id: int
    game_id: int

class GameSessionInDB(GameSessionBase):
    id: str
    model_config = ConfigDict(from_attributes=True)

class GameSessionPublic(GameSessionInDB):
    pass

class InteractionLogBase(BaseModel):
    timestamp: datetime
    user_input: str
    avatar_response: str
    detected_emotion: Optional[str]

class InteractionLogCreate(InteractionLogBase):
    child_id: int

class InteractionLogInDB(InteractionLogBase):
    id: str
    model_config = ConfigDict(from_attributes=True)

class InteractionLogPublic(InteractionLogInDB):
    pass

class ReportBase(BaseModel):
    period_start: datetime
    period_end: datetime
    generated_at: datetime
    summary_text: str
    insights: Optional[dict]
    suggestions: Optional[dict]

class ReportCreate(ReportBase):
    child_id: int

class ReportInDB(ReportBase):
    id: str
    model_config = ConfigDict(from_attributes=True)

class ReportPublic(ReportInDB):
    pass