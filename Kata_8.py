#$
planet = {"name": "marte","moons": "2"}
planet["circunferencia(km)"] = {"polar":6752,"equatorial":6792}
print (f'El planeta {planet["name"]} tiene {planet["moons"]} lunas')
print (f'El planeta {planet["name"]} tiene una circuferencia polar de {planet["circunferencia(km)"]["polar"]}')

planet_moons ={'mercury': 0,'venus': 0,'earth': 1,'mars': 2,'jupiter': 79,'saturn': 82,'uranus': 27,
'neptune': 14,'pluto': 5,'haumea': 2,'makemake': 1,'eris': 1}
moons = planet_moons.values()
planets = len(planet_moons.keys())
total = 0
for i in moons:
    total = total + i
promedio = total/planets
print(f'el promedio de lunas es: {round(promedio,2)}')