from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Voice to Law API",
    description="ملخص قانوني للنصوص باستخدام الذكاء الاصطناعي",
    version="1.0.0"
)

app.include_router(router)
