import ZODB, ZODB.FileStorage
import BTrees.OOBTree

# from app.db.user_model import *
# from app.db.course_model import *

storage = ZODB.FileStorage.FileStorage('app/db/data.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

if not hasattr(root, 'clients'):
    root.clients = BTrees.OOBTree.BTree()
if not hasattr(root, 'admins'):
    root.admins = BTrees.OOBTree.BTree()
if not hasattr(root, 'memberships'):
    root.memberships = BTrees.OOBTree.BTree()

def client_id():
    if not hasattr(root, 'client_id'):
        root.client_id = 0
    root.client_id += 1
    return root.client_id

def admin_id():
    if not hasattr(root, 'admin_id'):
        root.admin_id = 0
    root.admin_id += 1
    return root.admin_id

def check_user(username, password):
    for user in root.users.values():
        if user.username == username and user.password == password:
            return user
    return None

def checkAdmin(username):
    for user in root.users.values():
        if user.username == username:
            if user.email.endswith("@finecuisine.ac.th"):
                return True
    return False

#regitser user
def assignRole(email):
    if email.endswith("@finecuisine.ac.th"):
        return "admin"
    else:
        return "client"


# check database
def getAllClients():
    return [client.toJson() for client in root.clients.values()]

def getAllAdmins():
    return [admin.toJson() for admin in root.admins.values()]


            