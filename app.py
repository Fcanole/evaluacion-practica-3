from funciones import agregar_producto, listar_productos, buscar_por_categoria, calcular_promedio, guardar_productos

def main():
    productos = []
    
    while True:
        print("1. ingrese productos")
        print("2. listado de todos los articulos")
        print("3. buscar producto en categorias")
        print("4. promediar precio de todos los productos")
        print("5. Salir")
        
        opcion = input("ingrese un numero para elegir una opcion: ")
        
        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            listar_productos(productos)
        elif opcion == "3":
            buscar_por_categoria(productos)
        elif opcion == "4":
            calcular_promedio(productos)
        elif opcion == "5":
            guardar_productos(productos)
            break
        else:
            print("opcion incorrecta, intente nuevamente.")


if __name__ == "__main__":
    main()
from funciones import agregar_producto, listar_productos, buscar_por_categoria, calcular_promedio, guardar_productos

def main():
    productos = []
    
    while True:
        print("1. ingrese productos")
        print("2. listado de todos los articulos")
        print("3. Buscar productos en categorias")
        print("4. promediar precios de todos los productos")
        print("5. Salir")
        
        opcion = input("ingrese un numero para elegir una opcion: ")
        
        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            listar_productos(productos)
        elif opcion == "3":
            buscar_por_categoria(productos)
        elif opcion == "4":
            calcular_promedio(productos)
        elif opcion == "5":
            guardar_productos(productos)
            break
        else:
            print("opcion incorrecta, intente nuevamente.")


if __name__ == "__main__":
    main()
