from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Optional

@dataclass
class Conversation:
    user_id: str
    id: Optional[str] = field(default=None)
    created_at: Optional[datetime] = field(default=None)

    def to_dict(self):
        return {k: v for k, v in asdict(self).items() if v is not None}

@dataclass
class Message:
    conversation_id: int
    user_id: str
    message_text: str
    from_bot: Optional[bool] = field(default=False)
    id: Optional[str] = field(default=None)
    created_at: Optional[datetime] = field(default=None)

    def to_dict(self):
        return {k: v for k, v in asdict(self).items() if v is not None}