from distutils.log import info


Frase = "Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth."
Frase_split = Frase.split('. ')
Frase_split
Palabra_clave = ["average","temperature","distance"]
for x in Frase_split:
    for y in Palabra_clave:
        if y in x:
            print(x)
#%%
print("\n\nEjercicio 2\n")
nombre = "Ganímides"
gravedad  = 0.00142
planeta = "Marte"

titulo = f"""Gravity facts about {planeta}
--------------------"""
info = f"""Nombre del planeta: {planeta} 
Gravedad en el satélite, {nombre}: {gravedad * 1000} m/s2 
"""
plantilla = f"""{titulo.title()}\n{info}"""
print(plantilla)
print("Recalculando información\n")

plantilla_2 = f"""Gravity facts about {planeta}
--------------------
Nombre del planeta: {planeta} 
Gravedad en el satélite, {nombre}: {gravedad} m/s2 
"""

print(plantilla_2.format(nombre=nombre,planeta=planeta,gravedad=gravedad*1000))
