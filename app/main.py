from typing import List

import mlflow
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    texts: List[str]


MODEL_PATH = "./model"

app = FastAPI()
model = mlflow.sklearn.load_model(MODEL_PATH)


@app.post("/query")
def query(item: Item):
    try:
        input = item.texts
        res = model.predict(input)
        
        return {"result": {i: r.tolist() for i, r in zip(input, res)}}
    except Exception as e:
        return HTTPException(status_code=501, detail=f"failed to predict - reason: {e}")

