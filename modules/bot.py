from pyrogram import Client, filters,enums
from pyrogram.types import ChatPermissions
from . import congif
from .database import connect
app = Client("my_bot", api_id=27376757, api_hash="", bot_token="")


#left message 
async def messafememleft(client,user_id,name,username):
    text = f"<u><h1><b>USER LEFT THE GROUP</b></h1></u>\n\nNAME : {name} \nUSER NAME : <a href='https://t.me/{username}'>{username}</a> \nUSER ID : {user_id}"
    if not client.is_initialized:
        await client.start()
    connect.left_delet(user_id)
    await client.send_message(chat_id=congif.logChanelId, text=text)

#add message
async def adduser(client,newId,newName,newUsername,addId,addName,olde_user,new_user):
    text = f"<u><h1><b>USER ADD NEW USER</b></h1></u>\n\nADD BY USER NAME : <a href='https://t.me/{olde_user}'>{addName}</a>\nADD BY USER ID : {addId} \n\n      NEW USER \n\nNEW USER NAME : <a href='https://t.me/{new_user}'>{newName}</a> \nNEW ID : {newId}\nNEW USER NAME : {newUsername} "
    if not client.is_initialized:
        await client.start()
    connect.addNewUser(addId,addName,newId,olde_user,new_user)
    await client.send_message(chat_id=congif.logChanelId, text=text)

#remove member
async def remove(groupid,userid,client):
    # await app.start()
    permissions = ChatPermissions()
    await client.ban_chat_member(chat_id=groupid, user_id=userid)
    # await app.stop()
