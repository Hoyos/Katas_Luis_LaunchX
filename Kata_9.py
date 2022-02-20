'''def reporte(tanque_1, tanque_2, tanque_3):
    return f"""
    Fuel Report:
    Total Average: {promedio([tanque_1, tanque_2, tanque_3])}%
    tanque_1: {tanque_1}%
    tanque_2: {tanque_2}%
    tanque_3: {tanque_3}%"""

def promedio(valores):
    suma = sum(valores)
    length = len(valores)
    prom = suma/length
    return prom

print(reporte(90,80,70))
'''
def reporte_2( destino, *tiempos, **tanques):
    return f"""
    Mision con destino a {destino}
    Tiempo total del viaje: {sum(tiempos)} minutos
    Combustible total: {sum(tanques.values())} litros
    """
print(reporte_2("Moon", 14, 51, interno=200000, externo=300000))
