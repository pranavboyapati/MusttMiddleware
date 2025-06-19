import re
import os
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI()

@app.post("get-activity-history-data")
def getActivityHistoryData(data):
    return {"status": "success"}