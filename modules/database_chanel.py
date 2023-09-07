from .database import add_file




async def main(client,message):
    if (message.document):
        doc = message.document
        file_id = doc.file_id
        file_name = doc.file_name
        await add_file.addfile(file_id,file_name,message,client)

    else:
        print("no")