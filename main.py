import re
import os
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import requests

app = FastAPI()


@app.post("/get-activity-history-data")
async def getActivityHistoryData(request: Request):
    sentData = await request.body()
    headers = {"Content-Type": "application/json"} 
    result = requests.post(url="https://script.google.com/macros/s/AKfycbxk6qa0p1dQjXrpodWTmKEeV92i8q0jGKMHeuS_QFnVpUAVi6X_5y_nnir4Y9I41OKw/exec", data=sentData, headers=headers)
    return result.text

