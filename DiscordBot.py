# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 00:06:51 2017

@author: Mateusz
"""

import discord
import asyncio
import random
import pickle
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run('MzY1NjE1NTcxMzg0OTI2MjE5.DLmRUw.Wk8wn_PmOyPzafvb2mUlPx-0qTA')