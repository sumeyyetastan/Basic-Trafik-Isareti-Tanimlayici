import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt

def compare_images(imageA, imageB, title):
	
	s = ssim(imageA, imageB)
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle(" SSIM: %.2f" % (s))
	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
	# show the images
	plt.show()

	return s


num=input("Lütfen birden 5 e kadar numaralandırılmış olan levhalardan anlamını ögrenmek istediğiniz bir numara giriniz: ")
print("numara",num)

uzant=".jpg"
cropped=str(num)+uzant
cropped=cv2.imread(cropped)
cv2.imshow("Seçilen Resim",cropped)
#cv2.waitKey()

data_num=12

temp=0
tempname=" "
#The array that holds the names of the data
nameoftraficsign=["Dikkat Hiz Siniri 10 ","Saga Donus ","Duz ileri","Girilmez ","Yol yok "]
#The function we use to get data images  in the folder
for data_num in range(1,6):
    uzanti=".jpg"
    data=str(data_num)+uzanti
    data=cv2.imread(data)
    data = cv2.resize(data, (380,380)) #The picture has been resized.
	
    original= cv2.resize(cropped, (380,380))
    images = ("Original", original), ("Other", data)

    data = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    #Similarity Ratio function
    benzerlikorani = compare_images(original, data, "Original vs. Data")
    print("Data ile benzerlik oranı:", benzerlikorani)

    #Function to find which images in the data are most similar
    if benzerlikorani > temp:
        temp=benzerlikorani
        tempname=(data_num)-(1) #Bringing the meaning of the picture in the Array

print("Data ile benzerlik oranı:",temp)
print("Trafik işareti Anlamı:",nameoftraficsign[tempname])

cv2.imshow(nameoftraficsign[tempname],cropped)
cv2.waitKey()