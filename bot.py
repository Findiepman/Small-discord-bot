import discord
import requests
import json
import random
import math

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

qoutes = ['Fin is tuff', 'Shamil is tuff', 'Help ik leef', 'Johannes 15:18']

def get_quote():
  quote = random.choice(qoutes)
  return quote
  

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('!meme'):
      await message.channel.send(get_meme())
    if message.content.startswith('!quote'):
      await message.channel.send(get_quote())
    if message.content.startswith('ping'):
      await message.channel.send('Pong')
    if message.content.startswith('ding'):
      await message.channel.send('dong')
    if message.content.startswith('!help'):
      await message.channel.send('List of possible commands:')
      await message.channel.send('#1)  !meme. Shows a meme!')
      await message.channel.send('#2)  !quote. Picks a random quote!')
      await message.channel.send('#3)  !say [text] Says what you input as argument!')
      await message.channel.send('#4)  !calc [num1] +,-,x,/ [num2] Calculates what you input!')
      await message.channel.send('')
    if message.content.startswith('!say'):
    # Split off the command part ("!say ") to get the rest
      args = message.content.split(' ', 1)
      if len(args) > 1:
          await message.channel.send(args[1])
      else:
          await message.channel.send('You need to tell me what to say!')


    if message.content.startswith('!calc'):
      expression = message.content[6:]
      allowed = "0123456789+-*/(). "
      if all(ch in allowed for ch in expression):
          try:
              result = eval(expression)
              await message.channel.send(f'Result: {result}')
          except:
              await message.channel.send('⚠️ Fout bij berekening!')
      else:
          await message.channel.send('❌ Alleen cijfers en + - * / ( ) zijn toegestaan!')


    

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTQyNTU1NzY3NjQ1NjE0OTIxNA.G0mhsB.jH9-PYEWJ5lBN7PRIkvgEVCx5cG-fjhcukgH7g')


