import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

#Create Positive Samples
# imgs = []
# pathPositive = "F:/Python/AI/CarManufacturer/TrainData/Positives/"
# valid_images = [".jpg",".gif",".png",".tga"]
# fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(3, 5))
# i = 0
# for f in os.listdir(pathPositive):
#     fullPath = pathPositive + f
#     img = cv2.imread(fullPath, 1)
#     #axs[0].imshow(img)
#     cv2.imwrite(fullPath, img)
#     width = img.shape[1]
#     height = img.shape[0]
#     with open("info.txt", "a") as info:
#         info.write(fullPath + " 1 0 0 " + str(width) + " " + str(height) + "\n")
#         i += 1
# print("Number of positive image: ", i) #3158 images

#Create Negative Samples: 3091 images
pathNegative = "F:/Python/AI/CarManufacturer/TrainData/Negatives/"
for f in os.listdir(pathNegative):
    fullPath = pathNegative + f
    print(fullPath)
    img = cv2.imread(fullPath, 1)
    #axs[0].imshow(img)
    cv2.imwrite(fullPath, img)
    width = img.shape[1]
    height = img.shape[0]
    with open("bg.txt", "a") as bg:
        bg.write(fullPath + "\n")