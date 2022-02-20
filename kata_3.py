vel_asteroide = 49
vel_asteroide2 = 20
if(vel_asteroide>=25):
    print("WARNING:Meteoro cerca y rápido ¡Corran por sus vidas!")
else: 
    print("Que no cunda el pánico")
#Asi entendí yo el ejercicio
if vel_asteroide2>=19:
    print("Mira al cielo")
    if vel_asteroide2>=20:
        print("Disfruta el destello del meteoro")
else: 
    print("No corras no empujes, aqui no pasa nada")
#%%
vel_asteroide = 49
tamaño_asteroide = 26

if vel_asteroide> 25 and tamaño_asteroide> 25:
    print("WARNING:Meteoro cerca, rápido y peligroso ¡Corran por sus vidas!")
elif vel_asteroide >=20:
    print("Mira al cielo")
elif tamaño_asteroide <25:
    print("Mira al cielo")
else: 
    print("Que no cunda el pánico")