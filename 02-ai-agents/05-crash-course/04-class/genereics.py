from typing import TypeVar

T = TypeVar("T")

def value(x:T) -> T:
    return x

y = value(10)
x = value("hello")
