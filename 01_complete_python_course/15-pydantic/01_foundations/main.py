from pydantic import BaseModel
from typing import TypedDict



#
class UserDict(TypedDict):
    name:str
    age:int
    is_adult:bool

class User(BaseModel):
    name:str
    age:int
    is_adult:bool
    

# an error woll occur saying :Argument 1 to "User" has incompatible type "**dict[str, object]"....
# so you can do two things 
# 1- use TypeDict
# 2- us ModelName.model_validate(userinfo) instead of ModelName(**dict_name)
"""user_info = {"name":"huzair", "age":19, "is_adult":True}"""
"""user = User(**user_info)"""

# 1st way (preferedd but feels like an overkill)
""" user_info:UserDict = {"name":"huzair", "age":19, "is_adult":True}"""
""" user = User(**user_info)"""

# 2nd way (less safe)
user_info = {"name":"huzair", "age":19, "is_adult":True}
user = User.model_validate(user_info)

print(user_info)