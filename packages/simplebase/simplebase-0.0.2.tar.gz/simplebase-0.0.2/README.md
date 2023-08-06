# Simplebase
A simple Firebase wrapper for Python.
It uses the firebase_admin package for requests to Firebase, and makes things WAY easier to use.

To use the package, you must have Realtime Database and Storage enabled and a private key, stored in a JSON file.

You can connect to Firebase like this:
> connect("dbkey.json", "https://xxxxxxx-default-rtdb.firebaseio.com", "xxxxxxx.appspot.com")

Go to a path:
> refdb("/test/")

Get from the path:
> get()

Add to / create a nested path with a value:
> addToNest("/test/", "key", "value")

Add to a path with a value:
> add("key", "value")

Delete a nested path:
> deleteNest("/test/")
