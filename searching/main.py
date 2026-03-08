from fastapi import FastAPI, HTTPException
import uvicorn
import dal
import elastic
from config import SearchingConfig

elastic_client = elastic.Elastic()


app = FastAPI()

@app.get('/')
def home():
    return {
        "message" : "FastAPI server running and healthy!"
    }


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )