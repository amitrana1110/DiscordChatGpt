# App id: 1201782533818163230
# public key: 3d6694fce9a7692787261b4c0c44dd49dfb0c6482eca267f5d798e93669224be
# This example requires the 'message_content' intent.
# model="gpt-3.5-turbo-instruct-0914",

import discord
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("SECRET_KEY")


class MyClient(discord.Client):

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    
      print(f'Message from {message.author}: {message.content}')
      if self.user != message.author:
        if self.user in message.mentions:
          response = openai.Completion.create(
              model="gpt-3.5-turbo-instruct",
              prompt=message.content,
              temperature=1,
              max_tokens=256,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
          )
          channel = message.channel
          messageToSend = response.choices[0].text
          await channel.send(messageToSend)
    


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
