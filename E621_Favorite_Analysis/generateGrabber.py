print

def append(input):
	with open("jsonGrabber.sh", "a") as myfile:
		myfile.write(input)
		myfile.write("\n")

#SET ENVIORMENT VARIABLES your LOGIN_USERNAME and your API_KEY followed by the TARGET_USER_ID
LOGIN_USERNAME = ""
API_KEY = ""
TARGET_USER_ID = ""
#NOTE: If your login username does not have access to view the targets favorites you will not be able to download them.

append('mkdir favList')
#632 faveorites pages
for i in range(int(input("Enter number of pages to download (pages that do not exist may error): "))):
	append('echo "' + str(i+1) + '"')
	append('wget "https://e621.net/favorites.json?user_id=' + TARGET_USER_ID + '&page=' +  str(i+1) + '&login=' + LOGIN_USERNAME + '&api_key=' + API_KEY + '" --user-agent "testD"')
	append('mv "favorites.json?user_id=' + TARGET_USER_ID + '"* favorites_Page' + str(i+1) + '.json')
	append('mv favorites_Page' + str(i+1) + '.json favList/')
	append('sleep 1')
