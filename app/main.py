"""Main module for Azure Blob Storage interactions."""
from fastapi import FastAPI
from app.api.endpoints.api_v1.storage import CloudStorageApiRouter
import os

app = FastAPI(title="Azure Blob Storage API")

# Initialize storage router for Azure Blob Storage
storage_router = CloudStorageApiRouter()

@app.on_event("startup")
async def startup_event():
    app.state.blob_service_client = storage_router.blob_service_client
    print("Azure Blob Service client has been started.")

@app.on_event("shutdown")
def shutdown_event():
    print("Azure Blob Service client is shutting down.")

app.include_router(storage_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


