import os 
import discord
from src import keep_alive
import random
keep_alive.keep_alive()


token = os.environ.get("token")

nonowords = ['pussy', 'psy', 'nigg', 'nigger', 'nigga']
pie_crust = ['Nou', 'hair', 'ice cream(how tf does that work)', 'nerd soup', 'ur mom']

pie_fillings = ['ice cream', 'cherries', 'toenails', 'belly buttons', 'no u']

pie_toppings = ['Cream', 'Noice Sauce', 'nou', 'snails', 'slimy long fingers']
commands_list = ['help', 'pie','deliverpie', 'summon','about','work']

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('--help'):
        
        msg = 'Cmds:\nPrefix: `--`\nHelp: `--help`\nGenerate a Random Pie: `--pie`\nSummon. `--summon`\nDeliver a pie to you! `--deliverpie`'.format()
        await message.channel.send(msg)
    elif message.content.startswith('--pie'):
        randtop = random.choice(pie_toppings)
        randfill = random.choice(pie_fillings)
        randcrust = random.choice(pie_crust)

        msg = ('Your bootiful pie is:\nCrust: '+randcrust+'\nFilling: '+randfill+'\n And Topping: '+ randtop).format()
        await message.channel.send(msg)
    elif message.content.startswith('--summon'):
      msg = '**WHO SUMMONED THE ALMIGHTY PIEBOT!**'.format()
      await message.channel.send(msg)
    elif message.content.startswith('nerd'):
      msg = 'no u'.format()
      await message.channel.send(msg)
    elif message.content.startswith('--deliverpie'):
      msg = 'Hey nerd, look this command is still under development by the almighty elipie'.format()
      await message.channel.send(msg)
    elif message.content.startswith('no u'):
      msg = 'no u times 2'.format()
      await message.channel.send(msg)
    elif message.content.startswith('idiot'):
      msg = 'Hey man, lets not call people idiots, because you only say it because you, truthfully, know that *you* are the idiot.'.format()
      await message.channel.send(msg)
    elif message.content in nonowords:
      msg = 'OH HELL NO BITCH KEEP IT SFW'
      

      await message.channel.send(msg)
      await message.delete()
    elif message.content.startswith('--about'):
      msg = 'Hello! I am pie bot\nI was made by the epico user elipie! He is *really* good at coding, so he eventually made me!  While I am only a bot I can do a lot of stuff!  **More updates soon!** '.format()
      await message.channel.send(msg)
    elif message.content.startswith('die'):
      msg = 'no u'
      await message.channel.send(msg)
    elif message.content.startswith('--work'):
      msg = 'Hey man I get it, your impatient. Just wait until this command is *actually* out.'
    elif message.content[0:2] == '--' and message.content[3:] not in commands_list:
      msg = 'this damn idiot. smh. **ENTER A FUCKING COMMAND**'
      await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)
