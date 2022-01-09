import mysql.connector

#establish connection with db
myDb = mysql.connector.connect(
    host = "localhost",
    user = "phpmyadmin",
    password = "naZma13",
    database = "signToText"
)

#Creating a cursor object using the cursor() method
myCursor = myDb.cursor()

"""
define the path of the sign image or gif
the binary data of the file will be matched against 
the blob stored in Photo column and 
will retrieve the label of the file 

"""
def convertSignToText(filePath):
    with open(filePath, "rb") as File:
        binaryData = File.read()

    sqlMatch = "SELECT Label FROM Images WHERE Photo = (%s)"
    myCursor.execute(sqlMatch, (binaryData, ))
    myResult = myCursor.fetchone()
    print(myResult)


print("To insert sign image")
userFilePath = input("Enter file path:")
convertSignToText(userFilePath)



