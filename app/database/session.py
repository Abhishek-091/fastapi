from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import get_settings


settings = get_settings()
Base = declarative_base()

print("Database URL:", settings.DATABASE_URL)
engine = create_engine(settings.DATABASE_URL, echo=False)

# Create all tables
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()