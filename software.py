import requests
import sys

video = sys.argv[1]
download = requests.get(video)

# Comment two in three way merge - Master
# this is feature number one for three way merge
# adding comment for first change in Fast Forward Merge
# adding comment for second change in Fast Forward merge

# adding comment for Fast Forward Merger lesson


if download.status_code == 200:
    print('video downloaded successfully')
elif download.status_code == 301:
    print('you got redirected!')
else:
    print('video not downloaded')
