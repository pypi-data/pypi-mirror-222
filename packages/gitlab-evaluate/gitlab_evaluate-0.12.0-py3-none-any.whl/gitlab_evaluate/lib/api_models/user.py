from dataclasses import dataclass, asdict
from  typing import Optional

@dataclass
class User():
   username: str
   email: str
   state: str
   using_license_seat: Optional[bool]

   def to_dict(self):
        return asdict(self)
