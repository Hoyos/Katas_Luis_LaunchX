#%%
new_planet = ""
Planets =[]
while(new_planet!="done"):
    if new_planet:
        Planets.append(new_planet)
    new_planet = input("Ingrese un nuevo planeta:")
#%% 
for i in Planets:
    print(i)
