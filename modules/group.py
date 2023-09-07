from . import bot,groupM,congif
from .database import connect

# async def left(client,message):
#     await bot.messafememleft(client,message)

async def main(client, message):
    # print(message)
    # ss=message.document.file_id
    # await client.send_document(chat_id=congif.logChanelId,document=message.document.file_id)
    chek = str(message.service)
    grpID = message.chat.id
    if chek == "MessageServiceType.LEFT_CHAT_MEMBERS":
        # Handle left chat members (if needed)
        user_name = message.left_chat_member.username
        user_id = message.left_chat_member.id
        name = message.left_chat_member.first_name
        print(name)
        if not client.is_initialized:
            await client.start()
        await bot.messafememleft(client,user_id,name,user_name)

        # for user in message.left_chat_member:
        #     name = user.first_name
        #     user_id = user.id
        #     user_name = user.username
    elif chek == "MessageServiceType.NEW_CHAT_MEMBERS":
        # userid
        olde_id = message.from_user.id
        olde_name = message.from_user.first_name
        olde_username = message.from_user.username
        for user in message.new_chat_members:
            global userid
            global Nname
            global uname
            global isbot
            isbot = user.is_bot
            userid = user.id
            Nname = user.first_name
            print(isbot)
            uname = user.username
            isbot = bool(isbot)
            if(isbot):
                await bot.remove(grpID,userid,client)
            else:
                pass
            welcom = f"""Hay {Nname}
🌟<b> Welcome to our amazing Telegram group! </b>🌟

We are thrilled to have you join us in this wonderful community of series enthusiasts. 
Get ready to embark on an exciting journey filled with all your favorite series!
            """
            if(userid != olde_id and isbot != True):
                #print(Nname)
                await bot.adduser(client,userid,Nname,uname,olde_id,olde_name,olde_username,uname)
                Nname = ''
            else:
                pass
            if(isbot != True):
                await message.reply_text(welcom)
            else:
                await message.reply_text(f"<b>Hello {olde_name} </b> \n\n<i>you tried to add a bot to the group, so I removed that bot, this is your 1st warning, if you do this again, you will be removed from the group.</i>")
                
            # if(userid == chatuserid):
            #     pass
            # else:
            #     print("add  : "+chatusername)
            #     print("add  : "+Nname)
            #     #await bot.adduser(client,userid,Nname,uname,chatuserid,chatusername)
    else:
        uid = message.from_user.id
        un = message.from_user.first_name
        result = connect.checkadded(uid)
        if(result):
            pass
        else:
            await message.reply_text(f"Hello {un} \nif you want to get any series or animes from this group then you should add your 3 friends in this group")
