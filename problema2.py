while True:
    opcion = int(input("Ingrese la opción que desea: "))
    if opcion == 1:
        cantidad = int(input("Digite la cantidad de productos que desea: "))
        if (cantidad > 0) and (cantidad <= 5):
            def sin_descuento(cantidad,x):
                return int(cantidad*x)
            print("Su valor a pagar es de",sin_descuento(cantidad,2000))
        elif (cantidad > 5) and (cantidad <= 10):
            def primer_descuento(cantidad,y):
                return int((cantidad*y)-(cantidad*y*0.05))
            print("Su valor a pagar es de",primer_descuento(cantidad,2000))
        elif (cantidad > 10) and (cantidad <= 20):
            def segundo_descuento(cantidad,z):
                return int((cantidad*z)-(cantidad*z*0.10))
            print("Su valor a pagar es de",segundo_descuento(cantidad,2000))
        elif (cantidad > 20):
            def tercer_descuento(cantidad,a):
                return int((cantidad*a)-(cantidad*a*0.20))
            print("Su valor a pagar es de",tercer_descuento(cantidad,2000))
        else:
            print("La cantidad digitada no es válida")
        break
    elif opcion == 2:
        cantidad = int(input("Digite la cantidad de productos que desea: "))
        if (cantidad > 0) and (cantidad <= 5):
            def sin_descuento(cantidad,x):
                return int(cantidad*x)
            print("Su valor a pagar es de",sin_descuento(cantidad,2500))
        elif (cantidad > 5) and (cantidad <= 10):
            def primer_descuento(cantidad,y):
                return int((cantidad*y)-(cantidad*y*0.05))
            print("Su valor a pagar es de",primer_descuento(cantidad,2500))
        elif (cantidad > 10) and (cantidad <= 20):
            def segundo_descuento(cantidad,z):
                return int((cantidad*z)-(cantidad*z*0.10))
            print("Su valor a pagar es de",segundo_descuento(cantidad,2500))
        elif (cantidad > 20):
            def tercer_descuento(cantidad,a):
                return int((cantidad*a)-(cantidad*a*0.20))
            print("Su valor a pagar es de",tercer_descuento(cantidad,2500))
        else:
            print("La cantidad digitada no es válida")
        break
    elif opcion == 3:
        cantidad = int(input("Digite la cantidad de productos que desea: "))
        if (cantidad > 0) and (cantidad <= 5):
            def sin_descuento(cantidad,x):
                return int(cantidad*x)
            print("Su valor a pagar es de",sin_descuento(cantidad,5000))
        elif (cantidad > 5) and (cantidad <= 10):
            def primer_descuento(cantidad,y):
                return int((cantidad*y)-(cantidad*y*0.05))
            print("Su valor a pagar es de",primer_descuento(cantidad,5000))
        elif (cantidad > 10) and (cantidad <= 20):
            def segundo_descuento(cantidad,z):
                return int((cantidad*z)-(cantidad*z*0.10))
            print("Su valor a pagar es de",segundo_descuento(cantidad,5000))
        elif (cantidad > 20):
            def tercer_descuento(cantidad,a):
                return int((cantidad*a)-(cantidad*a*0.20))
            print("Su valor a pagar es de",tercer_descuento(cantidad,5000))
        else:
            print("La cantidad digitada no es válida")
        break
    else: 
        print("El valor ingresado no es correcto, vuelva a intentarlo ")


    