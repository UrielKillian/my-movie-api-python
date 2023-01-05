from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests

# Initializing the API

app = FastAPI()
app.title = "My first application with fastAPI"
app.version = "0.0.1"


# Creating endpoints
@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')


@app.get('/pokemons', tags=['Pokemons'])
def getAllPokemons():
    # Connecting with the poke api
    resp = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0', timeout=1)
    if resp.status_code != 200:
        return "Cannot connect with the poke server"
    data = resp.json()
    return data


@app.get('/pokemons/{name}', tags=['Pokemons'])
def getPokemonByName(name: str):
    # __Init__
    data = None
    # Searching the Pokemon with the id
    resp = requests.get('https://pokeapi.co/api/v2/pokemon/'+name)
    if resp.status_code != 200:
        return "Cannot get the information of the pokemon"
    print(resp.url)
    data = resp.json()
    return data
