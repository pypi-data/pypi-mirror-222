# This is not a program, this is a Python package.

# Simplebase
# A simple Firebase wrapper for Python.
# It uses the firebase_admin package for requests to Firebase, and makes things WAY easier to use.

# To use the package, you must have Realtime Database and Storage enabled and a private key, stored in a JSON file.

# You can connect to Firebase like this:
# 'connect("dbkey.json", "https://xxxxxxx-default-rtdb.firebaseio.com", "xxxxxxx.appspot.com")

# Go to a path:
# 'refdb("/test/")'

# Get from the path:
# 'get()'

# Add to / create a nested path with a value:
# 'addToNest("/test/", "key", "value")'

# Add to a path with a value:
# 'add("key", "value")'

# Delete a nested path:
# 'deleteNest("/test/")'


import firebase_admin
from firebase_admin import credentials, storage
from firebase_admin import db

def connect(certificate, database, storagebukkit):
    cred_obj = firebase_admin.credentials.Certificate(certificate)
    default_app = firebase_admin.initialize_app(cred_obj, {
       'databaseURL':database,
	   'storageBucket':storagebukkit
	   })
    print("Connected to Firebase!")

def refdb(path):
    global refdb
    refdb = db.reference(path)

def get():
    return refdb.get()

def addToNest(path, key, value):
    ref = db.reference(path)
    ref.update({key:value})

def add(key, value):
    refdb.update({key:value})
    
def deleteNest(path):
    ref = db.reference(path)
    ref.set({})
