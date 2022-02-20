from operator import index


planets = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Neptuno']
print("Hay un total de:",len(planets),"planetas")
planets.append("pluton")
print("El último planeta en lista es:",planets[-1])
#%%
print("Ejercicio 2\n")
planeta = input("Ingrese el nombre de un planeta:\n")
index = planets.index(planeta)
print("Los planetas cercanos a al sol hasta",planeta,"son:")
print(planets[0:index])
print("Los planetas alejados de sol desde",planeta,"son:")
print(planets[index+1:])