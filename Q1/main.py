from fastapi import FastAPI
from routes.system import router as system_router

app = FastAPI(
    title="Linux Command Executor API",
    description="API to execute predefined Linux system commands",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(system_router)

