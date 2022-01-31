from Controller import connectDb

# Establish connection with database
conn = connectDb.connect()


# Creating a cursor object using the cursor() method
my_cursor = conn.cursor()






"""
define the path of the sign image or gif
the binary data of the file will be matched against 
the blob stored in Photo column and 
will retrieve the label of the file 

"""
def convert_sign_to_text(filePath):

    """

    :param filePath: string
    :return: prints the converted text

    """

    with open(filePath, "rb") as File:
        binaryData = File.read()

# SQL command to search for the binary data in database that matches with user's file's binary data
    sqlMatch = "SELECT Label FROM images WHERE Photo = (%s)"
    my_cursor.execute(sqlMatch, (binaryData, ))


# Fetch the label assigned to the file from the database
    myResult = my_cursor.fetchone()
    return myResult
    #print(myResult)

# Input the filepath as string i.e directory_name/file_name_with_extension
print("To insert sign image")
userFilePath = input("Enter file path:")
convert_sign_to_text(userFilePath)



