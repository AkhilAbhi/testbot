from . import dbc

async def addfile(fid,fname,message,client):
    # print(fid)
    # print(fname)
    dt = dbc.db['data']
    datas ={"name":fname,"file_id":fid}
    try:
        dt.insert_one(datas)
    except:
        await message.reply_text("somthing rong")
