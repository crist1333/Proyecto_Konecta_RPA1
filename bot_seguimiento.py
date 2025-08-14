import pandas as pd

# 1️⃣ Cargar archivo Excel con datos de clientes
df = pd.read_excel("seguimiento_clientes.xlsx")

# 2️⃣ Filtrar clientes que no han recibido seguimiento
no_contactados = df[df["Seguimiento enviado"] == "No"]

# 3️⃣ Generar mensajes personalizados
for index, cliente in no_contactados.iterrows():
    mensaje = f"""
🔔 KONNECTA ATENCIÓN AL CLIENTE

Hola {cliente['Nombre']}, gracias por comunicarte con nosotros.

📝 Hemos registrado tu caso:
• Número de caso: #{cliente['Número de caso']}
• Estado: {cliente['Estado']}

📅 Tiempo estimado de respuesta: 24 horas

Si deseas consultar el estado en cualquier momento, responde con la palabra: ESTADO
"""
    print("📤 Mensaje enviado a:", cliente['Teléfono/Email'])
    print(mensaje)

    # 4️⃣ Marcar como enviado
    df.loc[index, "Seguimiento enviado"] = "Sí"

# 5️⃣ Guardar el archivo actualizado
df.to_excel("seguimiento_clientes_actualizado.xlsx", index=False)
print("✅ Archivo actualizado guardado como 'seguimiento_clientes_actualizado.xlsx'")
