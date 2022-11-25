from fastapi import FastAPI
from routes.locations import location
app = FastAPI()
app.include_router(location)

