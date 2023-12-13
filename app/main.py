from typing import Union
from fastapi import FastAPI, BackgroundTasks
from loguru import logger
import sys
import time
import random
import json




logger.add(sys.stdout, colorize=True, format="{time:HH:mm:ss} | {level} | {message}")

app = FastAPI()



def data_moduler():
    data = {
        "Frequence":random.randint(1,4),
        "StarupBuffer":random.randint(1,4),
        "Buffer":random.randint(1,4)
    }
    return data


@app.get("/")
async def read_root():
    """sample to test rebase 1 2 3 4 5"""
    loop=1
    while loop<=10000:
        data = data_moduler()
        loop = loop+1
        logger.info("checking the application logs info")
        logger.debug(data)
        logger.warning("checking the application logs warning ")
        logger.error("checking the application logs error")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
