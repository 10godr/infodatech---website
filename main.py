from fastapi import FastAPI, Form
import aiosmtplib
from email.message import EmailMessage

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción luego lo limitamos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

EMAIL_HOST = "mail.infodatech.com"
EMAIL_PORT = 587
EMAIL_USER = "Support@infodatech.com"
EMAIL_PASS = "jgc$66y<(*w4"

@app.post("/enviar")
async def enviar(
    nombre: str = Form(...),
    email: str = Form(...),
    servicio: str = Form(...),
    mensaje: str = Form(...)
):

    contenido = f"""
Nueva solicitud desde la web

Nombre: {nombre}
Email: {email}
Servicio: {servicio}

Mensaje:
{mensaje}
"""

    correo = EmailMessage()
    correo["From"] = EMAIL_USER
    correo["To"] = EMAIL_USER
    correo["Subject"] = "Nuevo mensaje desde tu página web"
    correo.set_content(contenido)

    await aiosmtplib.send(
        correo,
        hostname=EMAIL_HOST,
        port=EMAIL_PORT,
        username=EMAIL_USER,
        password=EMAIL_PASS,
        start_tls=True,
    )

    return {"mensaje": "Enviado correctamente"}