import math
r = int((input("Ingrese el radio para calcular el área, perímetro y volumen:")))
def area(r):
    area_circulo = math.pi * r ** 2
    return area_circulo
def perimetro(r):
    perimetro_circulo = math.pi * (2*r)
    return perimetro_circulo
def volumen(r):
    volumen_esfera = (4/3) * math.pi * r ** 3
    return volumen_esfera
print("Su área es: ",area(r))
print("Su perímetro es: ",perimetro(r))
print("Su volumen es: ",volumen(r))
