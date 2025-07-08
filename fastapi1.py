# TO CREATE A SIMPLE API

from typing import Optional # Optional is used to indicate that a parameter can be None
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# GET(GET INFO FROM SERVER)
# POST(CREATE)
# PUT(UPDATE)
# DELETE(DELETE)


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"aww lobuu, {name}!"}


@app.get("/square/{num}")
def square_number(num: int):
    return {"result": num * num}


@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    return {"sum": a + b}


@app.get("/is_even/{num}")
def check_even(num: int):
    return {"even": num % 2 == 0}


@app.get("/reverse/{text}")
def reverse_text(text: str):
    return {"reversed": text[::-1]}


# Optional parameters with default values
# Optional parameters can be used to make parameters optional in the API endpoint.


@app.get("/greet")
def greet(name: Optional[str] = None, age: Optional[int] = None):
    if name and age:
        return {"message": f"Hello, {name}! You're {age} years old."}
    elif name:
        return {"message": f"Hello, {name}!"}
    else:
        return {"message": "Hello, stranger!"}


@app.get("/goodbye")
def goodbye(name: Optional[str] = None):
    if name:
        return {"message": f"Goodbye, {name}!"}
    else:
        return {"message": "Goodbye, cutie!"}
