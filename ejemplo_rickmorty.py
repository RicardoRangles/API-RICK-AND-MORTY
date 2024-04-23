import requests # type: ignore

personajes = "https://rickandmortyapi.com/api/character"

lugares =  "https://rickandmortyapi.com/api/location"

episodios = "https://rickandmortyapi.com/api/episode"

# Indica todos los personajes de la API RICK AND MORTY

dato = requests.get(personajes) # type: ignore

if dato.status_code == 200:
    dato = dato.json()
    for elementos in dato['results']:
        print(elementos['id'])
        print(elementos['name'])
        print(elementos['status'])
        print(elementos['species'])
        
        
# Indica todos los lugares de los personajes RICK AND MORTY

dato = requests.get(lugares) # type: ignore

if dato.status_code == 200:
    dato = dato.json()
    for elementos in dato['results']:
        print(elementos['id'])
        print(elementos['name'])
        print(elementos['type'])
        print(elementos['dimension'])
        
        
# Indica todos los episodios de RICK AND MORTY

dato = requests.get(episodios) # type: ignore

if dato.status_code == 200:
    dato = dato.json()
    for elementos in dato['results']:
        print(elementos['id'])
        print(elementos['name'])       
        print(elementos['air_date']) 
        print(elementos['episode']) 
        
        
        
