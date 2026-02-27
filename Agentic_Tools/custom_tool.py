'''# to built a custom tool                    # cumpux sir method to make tool only for multiplication
from langchain.agents import tool

# step1 create a function
def multiply(a,b):
    """multiply two numbers"""
    return a*b

# add types hint
def multiply(a:int,b:int) ->int:
    """"multiply two numbers"""
    return a*b

# add tool decorater 
@tool
def multiply(a:int,b:int)->int:
    """multiply two numbers"""
    return a*b

result=multiply.invoke({'a':2,'b':5})
print(result)'''   


from langchain.agents import tool

# Addition
@tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Subtraction
@tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

# Multiplication
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

# Division
@tool
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    if b == 0:
        return float("inf")  # to avoid division by zero error
    return a / b


# ---- Test your tools ----
if __name__ == "__main__":
    print("Add:", add.invoke({"a": 5, "b": 3}))
    print("Subtract:", subtract.invoke({"a": 5, "b": 3}))
    print("Multiply:", multiply.invoke({"a": 5, "b": 3}))
    print("Divide:", divide.invoke({"a": 10, "b": 2}))






