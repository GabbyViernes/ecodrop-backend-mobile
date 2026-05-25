from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.api_v1.api import api_router

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    
    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include API Routers
    app.include_router(api_router, prefix="/api/v1")
    
    @app.get("/")
    async def root():
        return {"message": "Welcome to EcoDrop API (Modular)"}

    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}

    return app

app = start_application()
