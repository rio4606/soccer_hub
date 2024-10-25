from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.routes import router as api_router

app = FastAPI(
    title="Soccer Hub",
    description="API для футбольных команд с аналитикой и адаптацией под устройства",
    version="1.0.0",
)

# Подключение маршрутов
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать на Soccer Hub"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
