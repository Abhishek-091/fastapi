from fastapi import FastAPI
from app.api.user_route import router as user_route


app = FastAPI(title="FastAPI + Postgres")

app.include_router(user_route, prefix="/api/v1/user", tags=["Users"])

if __name__ == "__main__":
    from uvicorn import run
    run(
        "main:app", 
        host="127.0.0.1", 
        port=8080,
        workers=4
    )