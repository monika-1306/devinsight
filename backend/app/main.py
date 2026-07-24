from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import setup_logging

setup_logging()

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting DevInsight API...")
    yield
    logger.info("Stopping DevInsight API...")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }