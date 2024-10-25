from app.main import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",   # Укажите путь к вашему приложению FastAPI
        port=8000,        # Порт, на котором будет запущен сервер
        log_level="info", # Уровень логирования
        reload=True       # Автоматическая перезагрузка при изменении кода
    )
