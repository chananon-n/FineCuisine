import datetime
import random
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
if not hasattr(root, 'feedbacks'):
    root.feedbacks = BTrees.OOBTree.BTree()
if not hasattr(root, 'booking'):
    root.booking = BTrees.OOBTree.BTree()
if not hasattr(root,'DinnerBooking'):
    root.DinnerBooking = BTrees.OOBTree.BTree()
if not hasattr(root,'LunchBooking'):
    root.LunchBooking = BTrees.OOBTree.BTree()


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

def feedback_id():
    if not hasattr(root, 'feedback_id'):
        root.feedback_id = 0
    root.feedback_id += 1
    return root.feedback_id

def booking_id():
    if not hasattr(root, 'booking_id'):
        root.booking_id = 0
    root.booking_id += 1
    return root.booking_id

def getClient(username):

    for client in root.clients.values():
        if client.username == username:
            return client
    return None

def getAdmin(username):
    for admin in root.admins.values():
        if admin.username == username:
            return admin
    return None

def getClientInfo(clientID):
    for client in root.clients.values():
        if client.id == clientID:
            return client

def getAdminInfo(adminID):
    for admin in root.admins.values():
        if admin.id == adminID:
            return admin

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

def getAllBookings():
    return [booking.toJson() for booking in root.booking.values()]

def getUserBooking(clientID):
    return [booking.toJson() for booking in root.booking[clientID]]

def getBooking(bookingID):
    for booking in root.booking.values():
        if booking.bookingID == bookingID:
            return booking
    return "Booking not found"

def getMembership(clientID):
    for client in root.clients.values():
        if client.id == clientID:
            return client.membership
    return "Not found user"

# def registerMembership(clientID,membership):
#     root.clients[clientID].membership = membership.id
#     transaction.commit()

# def registerAdmin(admin):
#     root.admins[admin.id] = admin
#     transaction.commit()
        
def registerClient(client):
    root.clients[client.id] = client
    transaction.commit()


def checkMembership(clientID):
    for client in root.clients.values():
        if client.id == clientID and client.membership != False:
            return client.membership
    return "No membership"

def generateMealBooking(root, meal_type, t_time, t_left, num_bookings):
    # Get the current date
    current_date = datetime.datetime.now()

    # Find the latest existing date in the booking, if any
    latest_date_entry = max(getattr(root, f'{meal_type}Booking').values(), key=lambda x: datetime.datetime.strptime(x['T_DATE'], '%d/%m/%Y'), default=None)

    if latest_date_entry:
        latest_date = datetime.datetime.strptime(latest_date_entry['T_DATE'], '%d/%m/%Y') + datetime.timedelta(days=1)
    else:
        latest_date = current_date

    for i in range(num_bookings):
        # Set the date to the latest date plus i days
        t_date = latest_date + datetime.timedelta(days=i)

        # Create a unique key (number) for the booking
        booking_key = len(getattr(root, f'{meal_type}Booking')) + 1

        # Check if the key already exists
        while booking_key in getattr(root, f'{meal_type}Booking'):
            booking_key += 1

        # Create a new booking entry
        booking_data = {
            'T_ID': booking_key,
            'T_DATE': t_date.strftime('%d/%m/%Y'),  # Use dd/mm/yyyy format
            'T_TIME': t_time,
            'T_LEFT': t_left
        }

        # Store the data in the BTree
        getattr(root, f'{meal_type}Booking')[booking_key] = booking_data
        transaction.commit()

def getAllMealBookings(root, meal_type):
    # print data for each booking
    print(f'All {meal_type} bookings:')
    for booking_key in getattr(root, f'{meal_type}Booking'):
        print(getattr(root, f'{meal_type}Booking')[booking_key])
    # return [getattr(root, f'{meal_type}Booking')[booking_key] for booking_key in getattr(root, f'{meal_type}Booking')]

def clearMealBookings(root, meal_type):
    getattr(root, f'{meal_type}Booking').clear()
    transaction.commit()
    
def getMealBooking(root, meal_type, t_date, t_time):
    for booking in getattr(root, f'{meal_type}Booking').values():
        if booking['T_DATE'] == t_date and booking['T_TIME'] == t_time:
            return booking