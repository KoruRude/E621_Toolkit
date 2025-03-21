import subprocess
for i in range(50):
    print("")

print("      __        __   ___     __       __  ___  ___        __ ")
print("|__/ |__) |  | |  \ |__     /__  \ / /__   |  |__   |\/| /__ ")
print("|  \ |  \ \__/ |__/ |___    .__/  |  .__/  |  |___  |  | .__/")
print("https://krude-systems.net/redirect.html")
print("Unified E621 Toolkit Controller - 21Mar2025")
print("")
print("Dependencies: wget, python3")

while True:
    print('Enter "exit" to exit.')
    menuInput = input(" - Would you like to download or search E6 JSON files [d/s]? ")
    if menuInput == "exit":
        break
    elif menuInput == "d":
        #run download controller
        print('THIS PROCESS WILL REMOVE EXISTING "jsonGrabber.sh" AND WILL OVERWRITE "favList" FILES')
        print('Username, API key, and target user ID are required in lines 9-11 in "generateGrabber.py"')
        if "y" == input('Enter "y" if you understand, have complied, and are ready to continue: '):
            subprocess.run("./grabberControlScript.sh")
        else:
            print('User did not input "y"')
    elif menuInput == "s":
        subprocess.run(["python3", "JSON_info_search.py"])
    else:
        print("Logic Error: Menu entry not recognized.")