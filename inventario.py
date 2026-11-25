# ==========================   
# Fundamentos de Programación
# Problema 3 - Inventario
# Contexto: Desarrollar un programa que utilice una matriz con mínimo 5 artículos, incluyendo código, nombre, stock actual y stock mínimo. Mediante una función, se debe calcular cuántas unidades hacen falta para cada producto. Si el stock actual es menor al mínimo, se calcula la diferencia; de lo contrario, la cantidad a pedir será cero. Finalmente, se muestra un informe con los artículos y las cantidades que se deben solicitar.
# ==========================   

# (1) Función para calcular cantidad de productos en inventario:
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):

#Verificar si la cantidad es menor al stock:
    if stock_actual < stock_minimo:
        
# Calcular la cantidad necesaria a pedir :
        return stock_minimo - stock_actual
# Si todo está bien no se necesita pedir más productos:
    else:
        return 0
    
# (2) Función para mostrar los datos:
def procesar_inventario(matriz_inventario):
    
    # Titulo de la tabla
    print("INFORME DE REABASTECIMIENTO DE INVENTARIOS")
    
     # Nombres de las columnas del informe
    print(f"{'CODIGO':<10} {'ARTICULO':<18} {'STOCK ACTUAL':<14} {'STOCK MINIMO':<14} {'A PEDIR':<10}")
    print("-" * 65)
    
    # Recorrer la matriz de inventario y mostrar los datos:
    for articulo in matriz_inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        # Llamar a la funcion para saber cuantas unidades se necesitan:
        cantidad = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
        #Mostrar los datos en la tabla:
        print(f"{codigo:<10} {nombre:<18} {stock_actual:<14} {stock_minimo:<14} {cantidad:<10}")
        
    # Cerrar el informe:
    print("-" * 65)
    

# ==========================    
# UNAD - Fundamentos de Programación
# Grupo: 213022B_2204
# Estudiante: Kevin Stik Bernal Bacca
# Tutora: Yenny Carolina Rodriguez Vargas
# ==========================