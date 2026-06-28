import pandas as pd # type: ignore
import numpy as np # type: ignore
from datetime import datetime, timedelta
import random

# 0. Configuración inicial
num_registros_hw = 800
num_registros_sw = 300

def fechas_aleatorias(inicio, fin, n):
    formato = "%Y-%m-%d"
    inicio_dt = datetime.strptime(inicio, formato)
    fin_dt = datetime.strptime(fin, formato)
    rango = (fin_dt - inicio_dt).days
    return [(inicio_dt + timedelta(days=random.randint(0, rango))).strftime(formato) for _ in range(n)]

# 1. Dataset de Hardware (Periféricos y PCs)

marcas_pcs = ['HP', 'Lenovo', 'Dell']
marcas_perifericos = ['Logitech', 'Razer', 'HP', 'Lenovo', 'Dell']
departamentos = ['Ventas', 'IT', 'Marketing', 'Logistica', 'RRHH']

hw_data = {
    'ID_Compra_HW': [f'HW-{i+1000}' for i in range(num_registros_hw)],
    'Fecha': fechas_aleatorias("2025-01-01", "2026-05-31", num_registros_hw),
    'Departamento': np.random.choice(departamentos, num_registros_hw),
    'Categoria': np.random.choice(['Portatil', 'Monitor', 'Raton', 'Teclado'], num_registros_hw, p=[0.2, 0.3, 0.3, 0.2]),
}

df_hw = pd.DataFrame(hw_data)

# Asignar marcas, precios y ratings (rendimiento) con lógica según categoría
def asignar_detalles(row):
    if row['Categoria'] == 'Portatil':
        marca = np.random.choice(marcas_pcs)
        precio = round(np.random.uniform(700, 1500), 2)
    elif row['Categoria'] == 'Monitor':
        marca = np.random.choice(marcas_perifericos)
        precio = round(np.random.uniform(150, 400), 2)
    else:  # Raton o Teclado
        marca = np.random.choice(marcas_perifericos)
        precio = round(np.random.uniform(20, 120), 2) if marca in ['Razer', 'Logitech'] else round(np.random.uniform(10, 40), 2)
    
    base_rating = random.uniform(3.0, 4.8)
    if marca in ['Razer', 'Logitech']:
        base_rating = min(5.0, base_rating + 0.3)
    return pd.Series([marca, precio, round(base_rating, 1)])

df_hw[['Marca', 'Precio_Unitario', 'Rating_Rendimiento']] = df_hw.apply(asignar_detalles, axis=1)
df_hw['Cantidad'] = np.random.randint(1, 50, size=num_registros_hw)
df_hw['Coste_Total'] = round(df_hw['Precio_Unitario'] * df_hw['Cantidad'], 2)

# 2. Dataset de Software (Licencias)

sw_vendors = ['Microsoft', 'Adobe', 'SAP', 'AWS', 'Atlassian']

sw_data = {
    'ID_Licencia': [f'SW-{i+5000}' for i in range(num_registros_sw)],
    'Proveedor': np.random.choice(sw_vendors, num_registros_sw),
    'Departamento': np.random.choice(departamentos, num_registros_sw),
    'Usuarios_Comprados': np.random.randint(20, 500, size=num_registros_sw),
}

df_sw = pd.DataFrame(sw_data)

# Asignar productos y costes lógicos

def detalles_sw(row):
    if row['Proveedor'] == 'Microsoft':
        producto = 'Microsoft 365 E5'
        coste = 35.00 # mensual por user
    elif row['Proveedor'] == 'Adobe':
        producto = 'Adobe Creative Cloud'
        coste = 60.00 # mensual por user
    elif row['Proveedor'] == 'SAP':
        producto = 'ERP Cloud'
        coste = 120.00 # mensual por user
    elif row['Proveedor'] == 'AWS':
        producto = 'AWS Cloud Computing'
        coste = 200.00 # mensual por user
    else:  # Atlassian
        producto = 'Jira Software'
        coste = 15.00 # mensual por user
    
    # Se simula un problema de negocio -> se compran 100 licencias pero solo se usan 70
    usuarios_activos = int(row['Usuarios_Comprados'] * random.uniform(0.6, 0.95))
    return pd.Series([producto, coste, usuarios_activos])

df_sw[['Producto', 'Coste_Mensual_Licencia', 'Usuarios_Activos']] = df_sw.apply(detalles_sw, axis=1)

df_sw['Coste_Mensual_Total'] = round(df_sw['Coste_Mensual_Licencia'] * df_sw['Usuarios_Comprados'], 2)

# KPI ESTRELLA : Dinero gastado en licencias no utilizadas
df_sw['Gasto_Desperdiciado'] = round(df_sw['Coste_Mensual_Licencia'] * (df_sw['Usuarios_Comprados'] - df_sw['Usuarios_Activos']), 2)

# 3. Exportación de los datasets a CSV
df_hw.to_csv('dataset_hardware.csv', index=False)
df_sw.to_csv('dataset_software.csv', index=False)

print("Datasets generados y exportados correctamente, Listos para cargar en Power BI.")