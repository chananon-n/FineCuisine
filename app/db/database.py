import ZODB, ZODB.FileStorage
import BTrees.OOBTree

# from app.db.user_model import *
# from app.db.course_model import *

storage = ZODB.FileStorage.FileStorage('app/db/data.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

if not hasattr(root, 'users'):
    root.users = BTrees.OOBTree.BTree()
if not hasattr(root, 'courses'):
    root.courses = BTrees.OOBTree.BTree()
if not hasattr(root, 'memberships'):
    root.memberships = BTrees.OOBTree.BTree()

#or
"""
if not hasattr(root, 'clients'):
    root.clients = BTrees.OOBTree.BTree()
if not hasattr(root, 'admins'):
    root.admins = BTrees.OOBTree.BTree()
if not hasattr(root, 'courses'):
    root.courses = BTrees.OOBTree.BTree()
if not hasattr(root, 'memberships'):
    root.memberships = BTrees.OOBTree.BTree()
"""

def user_id():
    if not hasattr(root, 'user_id'):
        root.user_id = 1
    else:
        root.user_id += 1
    return root.user_id

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

def getAllUsers():
    return [user.toJson() for user in root.users.values()]


            