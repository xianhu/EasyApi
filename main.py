# _*_ coding: utf-8 _*_

"""
FastApi Application
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
