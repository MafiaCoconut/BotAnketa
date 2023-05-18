import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Persons:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    first_name: str = field(default="")
    middle_name: str = field(default="")
    last_name: str = field(default="")
    specialization: str = field(default="")
    created: datetime.now = field(default=datetime.now())
    table = 'persons'


# @dataclass
# class Leute:
#     id: uuid.UUID = field(default_factory=uuid.uuid4)
#     login: str = field(default="")
#     password: str = field(default="")
#     status: str = field(default="user")
#     state: str = field(default="start")
#     created: datetime.now = field(default=datetime.now())
#     table = "leute"
