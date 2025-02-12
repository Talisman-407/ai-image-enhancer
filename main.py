from fastapi import FastAPI, UploadFile, File, Form, Request, HTTPException
from fastapi.responses import Response, JSONResponse
import requests
import asyncio
import logging
from src.model.schemas import ImageGenerationRequest
from src.api.background_api import router as background_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/test")
async def test_server():
    return {"message": "So you thought I am down ?! No, I am running !"}

app.include_router(background_router)
