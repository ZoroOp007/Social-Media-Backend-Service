from fastapi import FastAPI
from .database import Base,engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "Social Medial Application",
    description= "Modern & Robust backend service api for social media application",
    version= "0.0.1"
)