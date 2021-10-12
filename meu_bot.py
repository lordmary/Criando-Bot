import discord
import os 

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        
        if message.content == '!regras':
            await message.channel.send(f'{message.author.name} as regras do servidor são:{os.linesep} 1- Proibido qualquer apoio ou menção à Rebelião/Resistência {os.linesep} 2- Sente-se, pegue uma pipoca e aproveite o servidor')
        
        elif message.content == '!oi':
            await message.channel.send(f'Olá {message.author.name}')
            
        elif message.content == '!que a força esteja com você':
            await message.channel.send(f'A capacidade de destruir um planeta é insignificante perto do poder da Força')
       
      elif message.content == '!codigo':
             await message.channel.send(f'Paz é uma mentira, só existe paixão.{os.linesep}Através da paixão, ganho força.{os.linesep}Através da força, ganho poder.{os.linesep}Através do poder, ganho a vitória.{os.linesep}Através da vitória, minhas correntes se rompem.{os.linesep}A Força me libertará.')
             

    async def on_member_join(self,member):
        guild = member.guild
        
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de aterrissar em {guild.name}. Bem vindo ao lado sombrio da Força!'
            await guild.system_channel.send(mensagem)

intents = discord.Intents.default()

intents.members = True

client = MyClient(intents = intents)

client.run('Aqui vai o token do meu bot')
