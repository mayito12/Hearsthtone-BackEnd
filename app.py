from fastapi import FastAPI 
from routes.users import user
app = FastAPI()

app.include_router(user)

@app.get('/')
def home():
    return {"Home"}