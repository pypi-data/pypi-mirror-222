from simplebase import *

connect("sneakyimdbkey.json", "https://xxxxxxx-default-rtdb.firebaseio.com", "xxxxxxxx.appspot.com")

refdb("/users/user")
getuser = get()
addToNest("/", "test", "var")
print(getuser['username'])

