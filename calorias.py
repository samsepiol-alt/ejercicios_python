import math
def calorias():
    

    proteina = float(input("Ingrese los gr de proteínas: \n"))
    carbohidratos = float(input("Ingrese los gr de carbohidratos: \n"))
    grasa = float(input("Ingrese los gramos de grasas: \n"))
    grado = float(input("Ingrese la graduacion alcoholica: \n"))

    # calorias = 4 * (proteina + carbohidratos) + 9 * grasa
    calorias = 4 * (proteina + carbohidratos) + 9 * grasa + (7 * grado)

    print(f'Las calorías totales del producto son: {math.ceil(calorias)}')
    return calorias


def calculadora(ingesta):
    cal = 0
    quit = False
    comida = [{
        "nombre":"",
        "calorias": 0
        }]
    i=0
    print("CALCULADORA DE COMIDA")
    print("----------------------")
    while(not quit):
        nombre = input("Nombre: \n")
        c = calorias()
        comida.insert(i,{"nombre": nombre, "calorias":c})
        cal = cal+c
        i = i+1
        print(f'{cal}  {ingesta}')
        if (ingesta <= cal):
            print("Ha alcanzado el limite recomendado: ")
        resp = input('Agregar otro? y/n: ')
        if(resp == "n"):
            quit = True
    
    
    print(f'CALORIAS TOTALES: {cal}')
    return comida




def datos():
    nombre = input("Ingrese su nombre: \n")
    edad = int(input("Ingrese su edad: \n"))
    altura = int(input("Ingrese su altura en cm: \n"))
    peso = int(input("Ingrese su peso en kg: \n"))
    sexo = input("Ingrese su sexo h/m: \n")
    if(sexo == "m"):
        valor = 665 + ((peso * 9.6) + (1.8 * altura) - (4,7 * edad))
            
    else:
        valor = 66.5 + (peso * 13.8) + (5 * altura) - (6.8 * edad)

    imc = peso/((altura/100)*2)

    
    return [nombre, edad, math.ceil(valor), math.ceil(imc)]


def imprime_menu(menu):
    print("--------MENU---------")
    for item in menu:
        print(f'''Nombre:{item["nombre"]}''' )
        print(f'Calorias: {item["calorias"]}')




def main():
    data = datos()
    print(f'Su ingesta diaria recomendada es de {data[2]} y su IMC {data[3]}')
    ans = input('Agregar menú? y/n: ')
    if(ans == 'y'):
        menu = calculadora(data[3])
        imprime_menu(menu)
    
    
#llamar a la funcion main para hacer funcionar esto
main()
