from typing import Union

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from loguru import logger as loguru_logger


class Log(BaseModel):
    log_level: str
    log_msg: str
    time: Union[str, None] = None


app = FastAPI()


@app.post("/log", status_code=201)
async def create_log(log: Log):
    loglevel_mapper = {
        "info": loguru_logger.info,
        "warn": loguru_logger.warning,
        "error": loguru_logger.error,
    }

    if log.log_level not in loglevel_mapper:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"unknown log level"
        )

    logger = loglevel_mapper[log.log_level]
    logger(log.log_msg)

    return log
