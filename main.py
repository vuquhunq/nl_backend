from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import routes

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins='*', allow_methods='*')
app.include_router(routes)
