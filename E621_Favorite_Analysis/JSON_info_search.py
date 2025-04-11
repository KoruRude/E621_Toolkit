from term_image.image import from_url

for i in range(50):
    print("")

#BRANDING
print("      __        __   ___     __       __  ___  ___        __ ")
print("|__/ |__) |  | |  \ |__     /__  \ / /__   |  |__   |\/| /__ ")
print("|  \ |  \ \__/ |__/ |___    .__/  |  .__/  |  |___  |  | .__/")
print("https://krude-systems.net/furr.html")
print("")
print("E621 Favorite.JSON Array Search Utility")
print("")
print("Will scan for favorites in the format of ~favList/favorites_Page[page number].json")
print("Example filepath: ~favList/favorites_Page27.json")
print("")

#mail control system
def displayPost(postString):
    #display post number, post link, and immage or preview
    print("Entry POST ID: " + str(postString[6:postString.find(",")]))
    print("Link to post: https://e621.net/posts/" + str(postString[6:postString.find(",")]))

    urlTargetIndex1 = postString.find('"url":"') + 7
    urlTargetIndex2 = postString.find('"},"preview":')
    extractedUrl = postString[urlTargetIndex1:urlTargetIndex2]
    if (-1 == extractedUrl.find(".webm") and -1 == extractedUrl.find(".gif")):
        print("PostIMG:")
        print(from_url(extractedUrl))
    else:
        tmp = str(postString[postString.find('"preview":{') + 7::])
        urlTargetIndex1 = tmp.find('"url":"') + 7
        urlTargetIndex2 = tmp.find('"},"sample":')
        extractedUrl = tmp[urlTargetIndex1:urlTargetIndex2]
        print(from_url(extractedUrl))
        print("Preview is displayed because, original is animated.")
    print("Entry POST ID: " + str(postString[6:postString.find(",")]))
    print("Link to post: https://e621.net/posts/" + str(postString[6:postString.find(",")]))


print("Prgm will build array out of files specified by following range:")

pageStart = int(input("Enter page start range [ex: 1]: "))
pageEnd = int(input("Enter page End range [ex: 7]: ")) +1

#BEGIN LOGIC ARRAY BUILD
print("Loading main logic array...")

#MAIN ARRAY INDEX  [PageNumber][PostNumber]
mainArray = []

pageCheck = 0
faveCheck = 0

for pageNumber in range(pageStart, pageEnd):
    #print(pageNumber)
    pageCheck +=1
    #runs for every file 1-X (x=632)

    file_path = 'favList/favorites_Page' + str(pageNumber) + '.json'

    with open(file_path, 'r') as file:
        file_content = file.read()

    fileArr = []
    postNumPerFile = file_content.count('{"id":')
    #print("Number of posts in file []: " + str(postNumPerFile))
    #runs for every post in file
    while True:
        faveCheck +=1
        if (file_content.find('{"id":') == -1):
            break

        indexStart = file_content.find('{"id":')
        indexEnd = file_content.find(',"duration":') + 17

        fileArr.append(file_content[indexStart:indexEnd])

        #cut arrayed index range of string out
        file_content = file_content[(indexEnd+1):]

    #end file, append to main array
    mainArray.append(fileArr)


#END LOGIC ARRAY BUILD
print("Main logic array loaded!")
print("Loaded " + str(pageCheck) + " pages and " + str(faveCheck) + " favorites.")
#print(mainArray[5][5])

#Search functions

#get info by json string contents
#print how many results
#print json content by mainArray index from search index; call mainArray from search index
while True:
    searchArray = [["Why did you enter 0?", "why?"]]
    searchHits = 0
    print('Enter "exit" to exit program.')
    queryStr = input("Enter string to serach in JSON: ")
    if queryStr == "exit":
        for i in range(5):
            print("")
        break
    
    for x in range (len(mainArray)):
        for y in range (len(mainArray[x])):
            if (mainArray[x][y].find(queryStr) != -1):
                searchArray.append([x, y])
                searchHits +=1
    
    print(str(searchHits) + " results found!")

    while True:
        dataReturnSetting = input("Print just post ID, ID and IMG, or entire JSON [i/ii/j]?: ")
        if dataReturnSetting == "i" or dataReturnSetting == "j" or dataReturnSetting == "ii":
            break
        else:
            print('Please enter "i", "ii", or "j"')


    while True:
        print('Enter "exit" to go back to search settings or exit.')
        resultQuery = input("Enter the result # that you want to view (1-" + str(searchHits) + "): ")
        if (resultQuery == "exit"):
            for i in range(5):
                print("")
            break
        try:
            resultQuery = int(resultQuery)

            displayPost(str(mainArray[int(searchArray[resultQuery][0])][int(searchArray[resultQuery][1])]))
            print("Entry Number: " + str(resultQuery))
        except:
            print("=======UNKNOWN INPUT INT ERROR, PLEASE TRY AGAIN=======")
