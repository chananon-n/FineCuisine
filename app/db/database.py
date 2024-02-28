import ZODB, ZODB.FileStorage
import BTrees.OOBTree
import transaction

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
    formatted_id = f'C{root.client_id:04d}'
    return formatted_id

def admin_id():
    if not hasattr(root, 'admin_id'):
        root.admin_id = 0
    root.admin_id += 1
    formatted_id = f'A{root.admin_id:04d}'
    return formatted_id

def checkUser(username, password):
    for client in root.clients.values():
        if client.username == username and client.password == password:
            return "client"
    for admin in root.admins.values():
        if admin.username == username and admin.password == password:
            return "admin"
    return "Incorrect username or password"

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

def clearDB():
    root.clients.clear()
    root.admins.clear()
    root.memberships.clear()
    transaction.commit()
            