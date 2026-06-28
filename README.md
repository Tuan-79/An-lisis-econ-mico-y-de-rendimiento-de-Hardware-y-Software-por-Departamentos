# 📊 IT Procurement & Software Asset Management (Power BI & Python)

## 🎯 Objetivo del Proyecto
Este proyecto es una solución integral de **Business Intelligence** diseñada para auditar y optimizar el gasto tecnológico de una empresa. El cuadro de mando permite a los departamentos de Compras TI (IT Procurement) tomar decisiones basadas en datos, cruzar el rendimiento del hardware con su precio de mercado y, sobre todo, **detectar y cuantificar el desperdicio económico en licencias de software sin uso**.

##  Stack Tecnológico:
* **Python (Pandas, NumPy):** Desarrollo de un script generador de datos sintéticos (`.csv`) que simula el ecosistema de compras B2B (Hardware y Software) de una corporación, resolviendo la falta de datasets públicos reales con este nivel de detalle corporativo.
* **Power BI:** Modelado relacional (Esquema en Estrella), limpieza de datos mediante Power Query y visualización de alto impacto.
* **DAX:** Creación de medidas y KPIs estadísticos y financieros (Tasas de adopción, Gasto desperdiciado, Coste total).

##  Estructura del Modelo y Dashboard:
El panel está diseñado con una estética oscura y sobria, enfocada en la claridad estadística y directiva, dividido en 3 fases analíticas:

1. **Visión Ejecutiva (Executive Overview):** Monitorización del presupuesto total de TI. Distribución del gasto por departamento (Ventas, IT, Logística, etc.) y control rápido de las fugas de capital.
2. **Inteligencia de Hardware (Market Intelligence):** Auditoría técnica de proveedores. Utiliza gráficos de dispersión (Scatter Plots) para cruzar el `Precio_Unitario` frente al `Rating_Rendimiento` de marcas reales (HP, Lenovo, Dell, Logitech), identificando la "compra inteligente" por categoría.
3. **Optimización de Licencias (Caza-Desperdicios):** Análisis de la Tasa de Adopción de software (Microsoft, AWS, SAP, etc.). Cruza los usuarios adquiridos frente a los usuarios activos para calcular el impacto financiero exacto del software no utilizado.

## 🚀 Cómo usar este repositorio:
1. Ejecuta el script `data_generator.py` para generar los archivos `hardware_procurement.csv` y `software_licenses.csv` actualizados.
2. Abre el archivo `.pbix` en Power BI Desktop.
3. Actualiza las fuentes de datos en Power Query para que apunten a tu directorio local.