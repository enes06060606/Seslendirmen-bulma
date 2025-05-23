import discord
from discord.ext import commands
import os 
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
       for attachment in  ctx.message.attachments:
           file_name=attachment.filename
           file_path=os.path.join(IMAGE_DIR, file_name)

           try:
                await attachment.save(file_path)
                await ctx.send(f"{file_name} kaydedildi.")
                class_name, confidence_score = get_class(file_path)
                await ctx.send(f"Bu resim {class_name} sınıfına ait ve güven puanı {confidence_score:.2f} olarak tahmin edildi.")

                mesajlar={
                    "Sezaı AYDIN-FRED CAKMAKTAS":"Sezai AYDIN fred çakmaktaş başka John Rambo, Rocky Balboa, Bill Cosby, Joe Dalton gibi seslendirmelerde yapmıstır",
                    "Atılla OLTAC-GARGAMEL":"Atilla OLTAÇ Gargamel karakterinden başka Şirinler dizisinde Şirin Baba, Şirinler 2 filminde Gargamel, Şirinler 3 filminde Gargamel, Şirinler 4 filminde Gargamel gibi seslendirmelerde yapmıstır",
                    "Serkan ALTUNORAK-BUGS BUNNY":"Serkan ALTUNORAK Bugs Bunny karakterindeen baaska Richie,Clark Kent,Will Turner gibi karakterlerde seslendirmiştir",
                    "Harun CAN-MORDEKAI":"Harun CAN Mordekai karakterinden başka  Kaptan Tsubasa,FİNN,Örümcek adam gibi karakterlerde seslendirmiştir",
                    "Berrak KUS-TWEETY":"Berrak KUŞ Tweety karakterinden başka 2005 yılında vizyona giren V for Vendetta filminde Natalia Portman'ın Evey karakterinin seslendirmesini yapmıştır. ",
                    "Koksal ENGUR-RED KIT":"Köksal ENGÜR Red Kit karakterinden başka Robert de Niro, Al Pacino, Dustin Hoffman ve Robin Williams'ın yanı sıra Susam Sokağı'ndaki 'Büdü' karakterini seslendirmiştir",
                    
                    }
                mesaj=mesajlar.get(class_name, "Bu karakter hakkında bilgi bulunamadı.")
                await ctx.send(f"BUNLAR HEP BİLGİ ÖĞREN:{mesaj}")

           except:
              await ctx.send(f"{file_name} kaydedilemedi.")
    else:
        await ctx.send("Mesajda ek yok.")
        
bot.run("TOKEN")