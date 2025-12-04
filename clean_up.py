import os

myfile = "./db/netflix1.db"

# If file exists, delete it.
if os.path.isfile(myfile):
    os.remove(myfile)
else:
    # If it fails, inform the user.
    print("Error: %s file not found" % myfile)
