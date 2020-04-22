import requests
import sys

video = sys.argv[1]
download = requests.get(video)

# Comment two in three way merge - Master

if download.status_code == 200:
    print('video downloaded successfully')
elif download.status_code == 301:
    print('you got redirected!')
else:
    print('video not downloaded')
