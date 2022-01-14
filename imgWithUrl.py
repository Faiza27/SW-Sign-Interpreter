from PIL import Image, ImageFilter
# import urllib
import urllib.request as url
import numpy as np
import requests
from io import BytesIO
import cv2

# imageURL="https://i.ibb.co/D9TXbyH/a.jpg"
# url_response=urllib.request.urlopen(imageURL)
# print(url_response)
# img_array=np.array(bytearray(url_response.read()),dtype=np.uint8)
# img=cv2.imread(img_array,-1)
# cv2.imshow("response img",img)
# cv2.waitKey()

# with urllib.request.urlopen("https://i.ibb.co/D9TXbyH/a.jpg") as url:
#     s = url.read()
#     # I'm guessing this would output the html source code ?
#     print(s)






req=url.urlopen('https://i.ibb.co/D9TXbyH/a.jpg')
arr = np.asarray(bytearray(req.read()),dtype=np.uint8)
img = cv2.imdecode(arr, -1)
cv2.imshow('image',img)
cv2.waitKey()
"""Different approach"""
# response= requests.get('https://i.ibb.co/D9TXbyH/a.jpg')
# img= Image.open(BytesIO(response.content))
# cv2.imshow('image',img)
# cv2.waitKey()

