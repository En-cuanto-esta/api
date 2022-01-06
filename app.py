from fastapi import FastAPI
from reports import all_resources

app = FastAPI()

posts = []

@app.get('/')
def index():
    return {"message": 'Bienvenido a En cuanto Está api', "success": True}

@app.get('/reports')
def reports():
    return all_resources()

