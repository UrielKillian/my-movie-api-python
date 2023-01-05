from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
# from fastapi import Request
# from models.Pokemon import Pokemon
import requests
# from typing import List

# Initializing the API and the fake data

app = FastAPI()
app.title = "My first application with fastAPI"
app.version = "0.0.1"

new_pokes = []


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
    return "Hello world"


@app.get('/pokemons/{name}', tags=['Pokemons'])
def getPokemonByName(name: str):
    # __Init__
    data = None
    # Searching the Pokemon with the id
    resp = requests.get('https://pokeapi.co/api/v2/pokemon/' + name)
    if resp.status_code != 200:
        return "Cannot get the information of the pokemon"
    print(resp.url)
    data = resp.json()
    return "Hello world"


@app.get('/mypokes', tags=['My Pokemons'])
def getMyPokemons():
    return new_pokes


"""

@app.post('/pokemon', tags=['Pokemons'], response_model=List[Pokemon])
def addPokemon(pokemon: Pokemon):
    new_pokemon = pokemon.json()
    new_pokes.append(new_pokemon)
    return JSONResponse(content=new_pokemon, status_code=201)


@app.put('/mypokes/{name}', tags=['My Pokemons'], response_model=dict)
def updatePokemon(name: str, pokemon: Pokemon):
    update_pokemon = pokemon.json()
    for i in range(len(new_pokes)):
        if new_pokes[i]['name'] == name:
            new_pokes[i] = Pokemon
            return JSONResponse(content=update_pokemon, status_code=200)
    return JSONResponse(status_code=404, content="Pokemon not found")


@app.delete('/mypokes/{name}', tags=['My Pokemons'])
def deletePokemon(name: str):
    for i in range(len(new_pokes)):
        if new_pokes[i]['name'] == name:
            new_pokes.pop(i)
            return JSONResponse(content={"message": "Pokemon deleted"}, status_code=200)
    return JSONResponse(status_code=404, content="Pokemon not found")
"""
