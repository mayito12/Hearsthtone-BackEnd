from fastapi import FastAPI 
from routes.cards import r_card
from routes.rareza import r_rareza
from routes.tipecards import r_tipocarta
from routes.typeclass import r_tipoclase
app = FastAPI()

app.include_router(r_card)
app.include_router(r_rareza)
app.include_router(r_tipoclase)
app.include_router(r_tipocarta)

@app.get('/')
def home():
    return {"Home"}