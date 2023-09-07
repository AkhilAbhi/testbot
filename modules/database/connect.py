from . import dbc


#add any users in new user detils for database 
def addNewUser(addeduserid,addeduserNAME,newuserid,olde_user_name,new_user_name):
    dt = dbc.db["users"]
    num=0
    lists = dt.find({'userId': addeduserid})
    for lists in lists:
        num =num+1
    if(num < 3):
        post ={"userId":addeduserid,"user name":addeduserNAME,"new_user_id":newuserid,"olde user name":olde_user_name,"new user name":new_user_name}
        dt.insert_one(post)
    else:
        pass



#chek this users added user list
def checkadded(uid):
    dt = dbc.db["users"]
    num=0
    lists = dt.find({'userId': uid})
    for lists in lists:
        num =num+1
    if (num>2):
        return True
    else:
        return False

def left_delet(uid):
    dt = dbc.db["users"]
    q = {"new_user_id":uid}
    dt.delete_one(q)