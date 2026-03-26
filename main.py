import pandas as pd
import numpy as np

# Creación de nuestro ÚNICO dataframe principal de trabajo
datos_ventas = {
    'id_venta': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    'sucursal': ['Norte', 'Sur', 'Centro', 'Norte', 'Centro', 'Sur', 'Norte', 'Sur', 'Centro', 'Norte', 'Norte', 'Sur', 'Centro', 'Norte', 'Sur'],
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Laptop', 'Monitor', 'Teclado', 'Mouse', 'Monitor', 'Laptop', 'Mouse', 'Teclado', 'Monitor', 'Laptop', 'Monitor', 'Teclado'],
    'cantidad': [2, np.nan, 5, 1, 2, 4, np.nan, 3, 2, 5, 3, np.nan, 4, 1, 2],
    'precio_base': ['1200.50', '25.00', '45.00', '1200.50', '250.00', '45.00', '25.00', '250.00', '1200.50', '25.00', '45.00', '250.00', '1200.50', '250.00', '45.00'],
    'categoria': ['Computación', 'Accesorios', 'Accesorios', 'Computación', 'Periféricos', 'Accesorios', 'Accesorios', 'Periféricos', 'Computación', 'Accesorios', 'Accesorios', 'Periféricos', 'Computación', 'Periféricos', 'Accesorios'],
    'columna_basura': ['x', 'y', 'z', 'w', 'a', 'b', 'c', 'x', 'y', 'z', 'a', 'b', 'c', 'w', 'x']
}

df_ventas = pd.DataFrame(datos_ventas)

print("DataFrame original:")
print(df_ventas)
print("\n" + "="*50 + "\n")

# Reto 1: Mantenimiento y Orden (Limpieza Inicial)

# Eliminar columnas (drop)
df_ventas = df_ventas.drop('columna_basura', axis=1)

# Renombrar columnas (rename)
df_ventas = df_ventas.rename(columns={'precio_base': 'precio_unitario'})

# Ordenar datos (sort_values)
df_ventas = df_ventas.sort_values('id_venta', ascending=False).reset_index(drop=True)

print("Reto 1 completado:")
print(df_ventas)
print("\n" + "="*50 + "\n")

# Reto 2: Sondeo de Datos

# Valores únicos (unique y nunique)
sucursales_unicas = df_ventas['sucursal'].unique()
print("Sucursales únicas:", sucursales_unicas)
productos_distintos = df_ventas['producto'].nunique()
print("Total de productos distintos:", productos_distintos)

# Frecuencias (value_counts)
producto_mas_frecuente = df_ventas['producto'].value_counts()
print("\nFrecuencia de productos:")
print(producto_mas_frecuente)
print("\nProducto más frecuente:", producto_mas_frecuente.index[0])
print("\n" + "="*50 + "\n")

# Reto 3: Limpieza de Datos Profunda

# Manejo de nulos (fillna)
df_ventas['cantidad'] = df_ventas['cantidad'].fillna(1)

# Conversión de tipos (astype)
print("Tipos de datos antes:")
print(df_ventas.dtypes)

df_ventas['precio_unitario'] = df_ventas['precio_unitario'].astype(float)
df_ventas['sucursal'] = df_ventas['sucursal'].astype('category')

print("\nTipos de datos después:")
print(df_ventas.dtypes)
print("\n" + "="*50 + "\n")

# Reto 4: Filtrado Inteligente

# Filtro básico
ventas_fuertes = df_ventas[df_ventas['precio_unitario'] > 150.0]
print("Ventas fuertes (precio > 150):")
print(ventas_fuertes)

# Filtro combinado
ventas_norte_cantidad = df_ventas[(df_ventas['sucursal'] == 'Norte') & (df_ventas['cantidad'] >= 2)]
print("\nVentas en Norte con cantidad >= 2:")
print(ventas_norte_cantidad)
print("\n" + "="*50 + "\n")

# Reto 5: Inteligencia de Datos (Agrupación y Fusión)

# Creación de métricas
df_ventas['total_venta'] = df_ventas['cantidad'] * df_ventas['precio_unitario']

print("DataFrame con total_venta:")
print(df_ventas[['id_venta', 'sucursal', 'cantidad', 'precio_unitario', 'total_venta']])

# Agrupación (groupby y agg)
analisis_sucursal = df_ventas.groupby('sucursal')['total_venta'].agg(['sum', 'mean']).round(2)
print("\nAnálisis por sucursal:")
print(analisis_sucursal)

# Fusión de tablas (merge)
df_presupuestos = pd.DataFrame({
    'categoria': ['Computación', 'Accesorios', 'Periféricos'],
    'presupuesto_marketing': [5000, 1500, 2000]
})

df_integrado = df_ventas.merge(df_presupuestos, on='categoria', how='left')
print("\nDataFrame integrado con presupuestos:")
print(df_integrado[['id_venta', 'categoria', 'total_venta', 'presupuesto_marketing']])

