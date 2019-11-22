import cv2
import matplotlib.pyplot as plt

car_cascade = cv2.CascadeClassifier('F:\Python\AI\CarManufacturer\Training\cascade.xml')
img = cv2.imread('car3.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect cars
cars = car_cascade.detectMultiScale(gray, 1.1, 1)

#Draw border
ncars = 0
for(x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 1)
    ncars = ncars + 1

#Show image
print("Number of car detected in image: ", ncars)
plt.figure(figsize=(10, 20))
plt.imshow(img)

plt.show()