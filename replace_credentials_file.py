import os
from shutil import move


creds = os.path.expanduser('~/.aws/credentials')
creds_bak = os.path.expanduser('~/.aws/credentials.python.backup')

# move backup credentials file if it exists
if os.path.isfile(creds_bak):
    move(creds_bak, creds)
    print('Default credentials moved back')
else:
    print('No backup credentials found')
