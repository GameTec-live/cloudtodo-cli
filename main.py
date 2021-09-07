import discord
import os

client = discord.Client()


@client.event
async def on_ready():
  print("ready as {0.user}".format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=" for commands"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    
    if msg.startswith('$help'):
        await message.channel.send("help | show this text \nstatus | shows the status of the bot \ntodo | interact with the todolist (*todo help help* for more info)")

    if msg.startswith('$status'):
        await message.channel.send("{0.user} is online and ready!".format(client))
    
    if msg.startswith('$todo'):
        awnser = "Whoops! you shouldnt be seeing this message! Please check your syntax!"
        array = msg.split(" ", 3)
        try:
            array.remove('$todo')
        except:
            print("An error occured, while trying to array the command")
        
        if len(array) > 1:
            action = array[0]
            name = array[1]
            try:
             entry = array[2]
            except:
                print("no 3rd argument supplied")
            if action == "create":
                if os.path.exists(name + ".todolist"):
                    awnser = "todolist already exists"
                else:
                    todolist = open(name + ".todolist", "w")
                    todolist.close()
                    awnser = "todolist  created"
            if action == "add":
                if os.path.exists(name + ".todolist"):
                    todolist = open(name + ".todolist", "a")
                    todolist.write(entry + "\n")
                    todolist.close()
                    awnser = "entry added"
                else:
                    awnser= "todolist not found"
            if action == "list":
                if os.path.exists(name + ".todolist"):
                    todolist = open(name + ".todolist", "r")
                    awnser = todolist.read()
                    todolist.close()
                else:
                    awnser= "todolist not found"
            if action == "delete":
                if os.path.exists(name + ".todolist"):
                    os.remove(name + ".todolist")
                    awnser = "todolist deleted"
                else:
                    awnser= "todolist not found"
            if action == "remove":
                if os.path.exists(name + ".todolist"):
                    todolist = open(name + ".todolist", "r")
                    lines = todolist.readlines()
                    todolist.close()
                    todolist = open(name + ".todolist", "w")
                    for line in lines:
                        if line.strip("\n") != entry:
                            todolist.write(line)
                    todolist.close()
                    awnser = "entry removed"
                else:
                    awnser = "todolist not found"
            if action == "show":
                files = os.listdir()
                for x in files:
                    if x.endswith(".todolist"):
                        print(x)
                    else:
                        files.remove(x)
                if len(files) > 0:
                    lists = ""
                    for x in files:
                        if x.endswith(".todolist"):
                            lists = lists + x + "\n"
                    awnser = "todolists: \n" + lists
                else:
                    awnser = "No lists found! Create a todolist with *todo create*"
            if action == "help":
                awnser = "todo <create|add|list|delete|remove|show|help> <name> <entry>\n create | Creates a todolist \n add | adds an entry to a todolist \n delete | deletes an todolist \n remove | removes an entry \n list | list the entrys in a todolist \n show | shows the available todolists (todo show av) \n help | shows this screen \n"

        else:
            awnser = "invalid syntax"
        await message.channel.send(awnser)
    




client.run('ODQxMjE0MTc5ODkzNzA2Nzgy.YJjfwQ.w7S9wGXTCY5PtgjcfVsfsmTyeFM')