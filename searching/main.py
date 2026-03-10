from fastapi import FastAPI, HTTPException
import uvicorn
import dal
import elastic
from config import SearchingConfig

logger = SearchingConfig.logger
elastic_client = elastic.Elastic()


app = FastAPI()

@app.get('/')
def home():
    return {
        "message" : "FastAPI server running and healthy!"
    }


@app.get('/query/all-data')
def get_all_data():
    try:
        result = dal.get_all(elastic_client)
        return result
    except Exception as e:
        logger.error(f'{type(e)} : {e}')
        raise HTTPException(500, f'{type(e)} : {e}')


@app.get('/query/top-5-terrorists')
def top_5():
    try:
        result = dal.top_5_terrorists(elastic_client)
        return result
    except Exception as e:
        logger.error(f'{type(e)} : {e}')
        raise HTTPException(500, f'{type(e)} : {e}')



@app.get('/query/avg-precent-dbs')
def get_precent_average():
    try:
        return dal.avg_precent_bds(elastic_client)
    except Exception as e:
        logger.error(f'{type(e)} : {e}')
        raise HTTPException(500, f'{type(e)} : {e}')



@app.get('/query/precent-bds-per-level')
def precent_bds_per_level():
    try:
        return dal.get_precent_per_level(elastic_client)
    except Exception as e:
        logger.error(f'{type(e)} : {e}')
        raise HTTPException(500, f'{type(e)} : {e}')


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )