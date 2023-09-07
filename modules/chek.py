from pyrogram import Client, filters
from . import group,congif,database_chanel

async def chekall(client,message):
    name = str(message.chat.type)
    if(name == "ChatType.PRIVATE"):
        print('private chat')
    elif(name == "ChatType.GROUP" or name == "ChatType.SUPERGROUP"):
        # print("group chat")
        await group.main(client,message)
    elif(name == "ChatType.CHANNEL"):
        chanel_id = message.chat.id
        if(chanel_id == congif.database):
            await database_chanel.main(client,message)
        else:
            pass
    else:
        # print(message)
        print("somthin wen wrong")
