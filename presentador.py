from calorias import *
data = datos()
def info(data):

    vive = input("Donde vives?: \n")
    ocupacion = input("Ingrese su ocupacion: \n")
    lugar = input("En donde?: \n")
    print("Ingrese 3 caracteristicas")
    car_1 = input("N° 1: \n")
    car_2 = input("N° 2: \n")
    car_3 = input("N° 3: \n")
    pasatiempo= input("Cual es tu pasatiempo?\n")
    hacer = input("Que quieres hacer?: \n")
    objetivo = input("cual es tu objetivo?: \n")

    string = f'''
    Soy {data[0]}, tengo {data[1]} años, mi casa está en {vive}, donde están las casas grandes y {car_3}. Trabajo como {ocupacion} en {lugar}  y llego a casa todos los días a más tardar 8 p.m. {car_1} y {car_2}. Duermo a las 11 p.m. y siempre procuro dormir 8 horas. Después de beber un vaso de leche tibia y hacer 20 minutos de calistenia, antes de ir a la cama, suelo dormir hasta la mañana. Despierto sin fatiga, ni estrés como un bebé. En mi último chequeo me dijeron que estoy sano.
    Mi pasatiempo es {pasatiempo} y me gustaria poder { hacer}.
    Mi ingesta diaria deberia ser {data[2]}
    Mi IMC es de {data[3]}
    Mi objetivo para el bootcamp es {objetivo}
    '''
    print(string)








info(data)