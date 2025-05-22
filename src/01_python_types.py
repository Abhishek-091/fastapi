

from typing import Union
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


def join_upper_case_names(first_name: str, last_name: str) -> str:
    f_name = first_name.upper()
    l_name = last_name.upper()
    return f"{first_name} : {last_name}"




# You can declare that a variable can be any of several types, for example, an int or a str.
# In Python 3.6 and above (including Python 3.10) you can use the Union type from typing and 
# put inside the square brackets the possible types to accept.

def process_item_0(item: Union[int, str]):
    print(item)

def process_item_1(item: int | str):
    print(item)




# Optional[Something] is actually a shortcut for Union[Something, None], they are equivalent.

def say_hi_0(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

def say_hi_1(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")






def say_hi_2(name: Optional[str]):
    print(f"Hey {name}!")

# say_hi_2()

def say_hi_3(name: str | None):
    print(f"Hey {name}!")

# say_hi_3()





# Pydantic is a Python library to perform data validation.
class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123




# Why Annotated?
# Before Annotated, FastAPI relied on parameter defaults like Query(), Path(), Body(), etc.,
#  which made type annotations harder to read. Annotated lets you separate the type from the metadata, 
# leading to more readable and reusable code.

from typing import Annotated
from fastapi import Query
from fastapi import Depends

def get_user_name():
    return "John Doe"

def get_user(name: Annotated[str, Query(min_length=2, max_length=50), Depends(get_user_name)]):
    return {"name": name}

CommonParams = Annotated[int, Query(gt=0)]

def read_items(limit: CommonParams):
    return {"limit": limit}
