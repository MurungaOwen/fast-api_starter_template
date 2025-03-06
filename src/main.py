"""main application"""
from fastapi import FastAPI

app = FastAPI()

# include other routers down here
# app.include_router(user.router, prefix="/users", tags=["users"])

# api base api route
@app.get("/")
def read_root():
    return {"status": "Server is up and running"}
