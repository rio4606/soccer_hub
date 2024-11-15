from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import User
from app.core.security import verify_token  # Если вы    используете токены для аутентификации

# Получение текущего пользователя из токена
async def get_current_user(db: Session = Depends(get_db), token: str = Depends(verify_token)):
    user = db.query(User).filter(User.id == token.user_id).first()  # Предполагается, что verify_token возвращает объект с user_id
    if not user:
        raise HTTPException(status_code=401, detail="Пользователь не авторизован")
    return user

# Пример зависимости для получения только администраторов
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.is_active:  # Предполагается, что у вас есть поле is_active
        return current_user
    raise HTTPException(status_code=400, detail="Пользователь не активен")

# Пример зависимости для получения сессии базы данных
def get_db_session():
    db = get_db()  # Здесь вы должны получить сессию из вашего get_db() метода
    try:
        yield db
    finally:
        db.close()
