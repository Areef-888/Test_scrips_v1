from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Annotated
from app.services.multiply import multiply

class NumberRequest(BaseModel):
    number:Annotated[int, "The number to be processed"]

class NumberResponse(BaseModel):
    result:Annotated[int, "The result of the multiplication"]

app= FastAPI()

@app.get("/")
async def basic_route():
    return {"message": "Hello World"}

@app.post("/multiply_number",response_model=NumberResponse)
async def multiply_number(request: NumberRequest):
    try:
        return NumberResponse(result=multiply(request.number, 2))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))