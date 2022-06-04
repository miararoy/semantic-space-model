from typing import List

import mlflow
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app import __version__


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

        result = {
            "version": __version__,
            "results": [
                {"input": input[i], "output": res[i]} for i in range(len(input))
            ]
        }
        
        return result
    except Exception as e:
        return HTTPException(status_code=501, detail=f"failed to predict - reason: {e}")

