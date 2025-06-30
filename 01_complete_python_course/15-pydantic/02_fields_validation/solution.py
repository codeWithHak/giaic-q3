# TODO: Create Employee model
### Fields:
# - id: int
# - name: str (min 3 chars)
# - department: optional str (default 'General')
# - salary: float (must be >= 10000)

#type:ignore

from pydantic import BaseModel, Field

class Employee(BaseModel):
    id:int
    name:str = Field(..., min_length=3) # Triple dot(...) means it is a required field
    department: str | None = "General"
    salary: float = Field(..., ge=10000)
    
employee_details = {"id":111, "department":"Science", "salary":20000}

employee1:Employee = Employee(**employee_details)
print(employee1)