import smtplib
from email.message import EmailMessage

mensaje = EmailMessage()
#leer archivo html
with open('Mensaje.html', 'r') as file:
    file_content = file.read()

asunto_correo = "Bienvenido a la fila virtual"
dirección_correo_remitente = ""
direccion_correo_receptor = ""

# Establecer encabezados del correo

mensaje['Subject'] = asunto_correo
mensaje['From'] = dirección_correo_remitente
mensaje['To'] = direccion_correo_receptor


# Agregar contenido del mensaje a tipo html
mensaje.set_content(file_content, subtype='html')

# Establecer servidor de correo y puerto
servidor_correo = "smtp.gmail.com"
servidor = smtplib.SMTP(servidor_correo, '587')

#Identificar el cliente en el servidor
servidor.ehlo()

# Asegurar la conexión SMTP
#servidor.starttls()

# Iniciar sesión en la cuenta de correo
dirección_correo_remitente = "automotriz.olivares@gmail.com"
contrasena_correo = ""
servidor.login(dirección_correo_remitente, contrasena_correo)


# Envío de correo
servidor.sendmail(to_addrs=direccion_correo_receptor, msg=mensaje.__str__(), from_addr=dirección_correo_remitente)

# Cerrar la conexión con el servidor de correo
servidor.quit()
