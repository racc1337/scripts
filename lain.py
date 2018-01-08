#!/usr/bin/env python3
import discord
import praw
from discord.ext.commands import Bot
import pprint
import datetime
import asyncio 
import time
import config

CLIENT_ID = config.discordID
CLIENT_SECRET = config.discordSecret
BOT_TOKEN = config.discordToken

reddit = praw.Reddit(
						client_id=config.redditID,
						client_secret=config.redditSecret,
						user_agent=config.redditUser
					)

lain = Bot(command_prefix="$")

@lain.event
@asyncio.coroutine
def on_ready():
	print('Ready!')

async def my_background_task():
	await lain.wait_until_ready()
	channel = discord.Object(id=config.discordChannel)
	while not lain.is_closed:
		subreddit=reddit.subreddit('Dankmemes')
		hotmemes=subreddit.top('hour')
		i = 0;
		await lain.send_message(channel,time.strftime("%H:%M:%S")+'\n'+time.strftime("%d/%m/%Y"))
		for submission in hotmemes:
			if not submission.stickied:
				i=i+1
				if i>5:
					break
				await lain.send_message(channel,'-----'+'\n'+submission.title+'\n'+submission.url)
		await asyncio.sleep(3600)

@lain.command()
async def hello(*args):
	return await lain.say("Hello World")

@lain.command()
async def moyai(args):
	await lain.say(":moyai:"*int(args))

@lain.command()
async def fetch(arg2=None):
	if arg2 is None:
		arg2='Dankmemes'
	subreddit=reddit.subreddit(arg2)
	hotmemes=subreddit.top('day')
	i = 0;
	for submission in hotmemes:
		if not submission.stickied:
			i=i+1
			if i>5:
				break
			await lain.say('-----'+'\n'+submission.title+'\n'+submission.url)
			pprint.pprint(vars(submission))

lain.loop.create_task(my_background_task())
lain.run(BOT_TOKEN)