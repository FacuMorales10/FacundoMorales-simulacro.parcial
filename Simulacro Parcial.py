# Matriz para almacenar los productos
# Cada fila: [Nombre del producto, Precio del producto, Cantidad del producto]
inventario = [
    ["Laptop", 1500.00, 10],
    ["Silla", 200.00, 50],
    ["Libro", 15.00, 100],
    ["Monitor", 300.00, 30]
]

# Mensaje para cuando no hay productos 
MENSAJE_NO_PRODUCTOS = "No hay productos disponibles para la operación solicitada." 

def mostrar_menu():
    """
    Muestra el menú principal de opciones al usuario y retorna su elección.
    Maneja entradas no válidas para evitar errores.
    """
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Cargar producto/s")
    print("2. Buscar producto")
    print("3. Ordenar inventario")
    print("4. Mostrar producto más caro y más barato")
    print("5. Mostrar productos con precio mayor a 15000")
    print("6. Salir")
    print("----------------------")
    
    while True: # Bucle para seguir pidiendo la opción hasta que sea válida.
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opción no válida. Por favor, ingresá un número entre 1 y 6.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresá un número entero.")

def cargar_productos(inventario):
    """Permite al usuario cargar nuevos productos al inventario"""
    print("\n--- CARGAR PRODUCTOS ---")
     
    cantidad_productos = int(input("¿Cuántos productos desea cargar? "))
    if cantidad_productos <= 0:
        print("La cantidad de productos debe ser un número positivo.")
        return

    for i in range(cantidad_productos):
        
        nombre = input("Ingrese el nombre del producto: ").strip()

        precio = float(input(f"Ingrese el precio de '{nombre}': "))

        cantidad = int(input(f"Ingrese la cantidad de '{nombre}': "))

        inventario.append([nombre, precio, cantidad])
        print(f"Producto '{nombre}' cargado exitosamente.")

def buscar_producto(inventario): 
    """Busca un producto por su nombre y muestra sus datos.""" 
    print("\n--- BUSCAR PRODUCTO ---")

    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower() 
    encontrado = False
    for producto in inventario:
        if producto[0].lower() == nombre_buscar:
            print(f"\n Producto encontrado: Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}") 
            encontrado = True
            break
    if not encontrado:
        print(f"El producto '{nombre_buscar}' no se encontró.")

def ordenar_inventario(inventario):
    """
    Ordena el inventario por precio ascendente usando un algoritmo de burbuja
    y luego lo muestra.
    """
    print("\n--- ORDENAR INVENTARIO ---")

    n = len(inventario)
    
    # Implementación del algoritmo de ordenamiento
    for i in range(n - 1):
        # El último i elementos ya están en su lugar correcto
        for j in range(0, n - i - 1):
            # Comparamos por el precio (índice 1 del producto)
            if inventario[j][1] > inventario[j + 1][1]:
                # Intercambiar elementos si están en el orden incorrecto
                inventario[j], inventario[j + 1] = inventario[j + 1], inventario[j]

    print("\nInventario ordenado por precio (ascendente):")
    for producto in inventario:
        print(f"  Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}")

def mostrar_producto_mas_caro_y_barato(inventario):
    """
    Identifica y muestra el producto más caro y el más barato.
    """
    print("\n--- PRODUCTO MÁS CARO Y MÁS BARATO ---")

    # Inicializamos con el primer producto de la lista
    mas_caro = inventario[0]
    mas_barato = inventario[0]

    # Recorremos el resto del inventario para encontrar el más caro y el más barato

    for i in range(1, len(inventario)):
        producto_actual = inventario[i]

        # Comparamos por precio (índice 1 del producto)
        if producto_actual[1] > mas_caro[1]:
            mas_caro = producto_actual
        
        if producto_actual[1] < mas_barato[1]:
            mas_barato = producto_actual

    print(f"\nProducto más caro: Nombre: {mas_caro[0]}, Precio: {mas_caro[1]}, Cantidad: {mas_caro[2]}")
    print(f"Producto más barato: Nombre: {mas_barato[0]}, Precio: {mas_barato[1]}, Cantidad: {mas_barato[2]}")

def mostrar_productos_precio_mayor_a_15000(inventario):
    """
    Muestra productos con precio mayor a $15000
    """
    print("\n--- PRODUCTOS CON PRECIO MAYOR A $15000 ---")

    se_encontraron_productos = False # Bandera para saber si encontramos al menos uno

    for producto in inventario:
        if producto[1] > 15000:
            # Imprimimos directamente el producto si cumple la condición
            print(f"  Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}")
            se_encontraron_productos = True # Marcamos que sí se encontró al menos uno

    if not se_encontraron_productos:
        print("No se encontraron productos con precio mayor a $15000.") 

# --- Lógica principal del programa ---

def main():
    """Función principal que ejecuta el sistema de inventario."""
    # inventario ya está definido globalmente al inicio del archivo

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            cargar_productos(inventario)
        elif opcion == 2:
            buscar_producto(inventario)
        elif opcion == 3:
            ordenar_inventario(inventario)
        elif opcion == 4:
            mostrar_producto_mas_caro_y_barato(inventario)
        elif opcion == 5:
            mostrar_productos_precio_mayor_a_15000(inventario)
        elif opcion == 6:
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else: # Manejo simplificado para opciones inválidas
            print("Opción no válida. Por favor, intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
