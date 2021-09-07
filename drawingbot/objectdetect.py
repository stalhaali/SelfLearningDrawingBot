import cv2
import base64
from PIL import Image
from io import BytesIO
import numpy as np


def detect(data_url):
        """returns all the objects drawn in the drawing, data_url, as a list

        :param data_url: an html dataurl of an image. In this case, the drawing made by the user
        :type data_url: str
        :rtype: list
        """
        offset = data_url.index(',')+1
        img_bytes = base64.b64decode(data_url[offset:])
        img = Image.open(BytesIO(img_bytes))
        img  = np.array(img)
        grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grayscaled, (7,7), 1)
        #canny = cv2.Canny(blur, 50, 50)
        thresh = cv2.bitwise_not(grayscaled)
        #thresh = cv2.threshold(blur, 110 ,255, cv2.THRESH_BINARY_INV)[1]
        img1 = img.copy()
        all_pics = []
        height, width, channels = img.shape

        contours, Hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        i = 0
        for cnt in contours:
                i += 1
                #cv2.drawContours(img1, cnt, -1, (255, 0, 0), 3)
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
                x, y, w, h = cv2.boundingRect(approx)
                print(height)
                print(width)
                print(y-20)
                print(y+h+20)
                print(x-20)
                print(x+w+20)
                if (y-20 < 0) or (y+h+20 > height) or (x-20<0) or (x+w+20 > width):
                        img0 = thresh [y:y+h, x:x+w]
                        img2display = img [y:y+h, x:x+w]
                else:
                        img0 = thresh [y-20:y+h+20, x-20:x+w+20]
                        img2display = img [y-20:y+h+20, x-20:x+w+20]
                
                #img0 = thresh [y:y+h, x:x+w]
                new_img = cv2.resize(img0, (28, 28))
                all_pics.append(new_img)
                cv2.rectangle(img1, (x-20, y-20), (x+20+w, y+h+20), (0, 255, 0), 2)
                #cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.imwrite("drawingbot/static/picture" +str(i)+".jpg", img2display)

        #cv2.imshow("title", img1)
        #cv2.imshow("title2", thresh)
        #cv2.waitKey(0)
        return all_pics

def create_img(dic):
        """Writes text, in this case the prediction, on the image of each object and then 
        saves it as an image

        :param dic: dictionary mapping the prediction to the number it was predicted at
        :type dic: dictionary
        :rtype: None
        """
        for key in dic:
                img = cv2.imread('drawingbot/static/picture' + str(key) + '.jpg')
                cv2.putText(img, dic[key], (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.imwrite("drawingbot/static/picture" +str(key)+".jpg", img)