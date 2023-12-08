
#Importando librerías (se modifica al gusto)

import discord
import requests  #Asegúrese de que tiene instalada la biblioteca requests. Si no es así, ¡instálala con pip install!
from discord.ext import commands
import os
import random
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np


# Las sugerencias de comida asociadas a cada clase
sugerencias_comida = {
    "Gorrion": "Tu animal puede comer Semillas y frutas, recuerda que es importante para su supervivencia :hatching_chick:",
    "Buhos": "A los Buhos les encanta comer Ratones pequeños y aves (LOL) :hatching_chick:",
    "Tucanes": "A los tucanes, un animal hermoso, les encanta comer Frutas tropicales :hatching_chick:",
    "Mirlas": " A las mirlas, un pajarito nativo de Colombia les encanta comer Insectos y frutas :hatching_chick:",
    "Palomas": "Las palomas les encanta comer Semillas y granos :hatching_chick:",
    "Aguilas": "Las aguilas son fáciles: Comen Carne fresca :hatching_chick:",
    "Condor": "El cóndor, el ave representativa de Colombia come Carroña y animales pequeños :hatching_chick:",
}


def get_class(model_path, labels_path, image_path):
    np.set_printoptions(suppress=True)
    model = load_model(model_path, compile=False)
    class_names = open(labels_path, "r", encoding="utf-8").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_path).convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return(class_name[2:], confidence_score)

#NO BORRAR 
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

# Activar el privilegio de lectura de mensajes
intents.message_content = True

# Crear un bot en la variable cliente y transferirle los privilegios, también se define que el bot funcione con ! 
bot = commands.Bot(command_prefix='!', intents=intents) 

#Para saber si hemos iniciado sesión
@bot.event
async def on_ready():
    print(f"Hemos iniciado sesión como {bot.user}")

#Así se hacen los comandos para que el bot opere
@bot.command()  
async def Help(ctx):   #De aquí depende el comando, el nombre que se pone aquí es el comando que el bot usará (!Micomando)
    #AQUÍ VA EL FUNCIONAMIENTO DEL BOT, dependiendo de lo que quieran que haga
    await ctx.send("Hola, Soy un bot para generar sugerencias de comida dependiendo del tipo de animal que tengas! Envíame una foto de cualquier de estos animales junto al comando !Revisar y mira la magia: (Gorrion, Buhos, Tucanes ,Mirlas, Palomas, Aguilas, Condor)") #acá es lo que el BOT va a responderte cuando escribas !Micomando

@bot.command()
async def Revisar(ctx):
    if ctx.message.attachments: 
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url

            await attachment.save(f"./{file_name}")
            
            # Obtener la clase inferida y la puntuación de confianza
            class_name, confidence_score = get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{file_name}")
           
            class_name = class_name.strip()
            # Obtener la sugerencia de comida asociada a la clase inferida
            sugerencia = sugerencias_comida.get(class_name, "No hay sugerencia de comida para esta clase")

            # Enviar el resultado al canal de Discord
            await ctx.send(f"Este es un pájaro de la clase: {class_name}\n\n Estoy seguro en un: {confidence_score:.2f}\n {sugerencia}")

    else:
        await ctx.send("Olvidaste subir tu imagen :( ") 
  
        
bot.run("AQUI VA TU TOKEN")
