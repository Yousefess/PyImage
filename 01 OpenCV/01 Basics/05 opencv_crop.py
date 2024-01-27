# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="01 OpenCV/01 Basics/Images/free-images.jpg",
                help="path to the input image")
args = vars(ap.parse_args())

# load the input image and display it to our screen
image = cv2.imread(args['image'])
cv2.imshow("Original", image)

# cropping an image with OpenCV is accomplished via simple NumPy
# array slices in startY:endY, startX:endX order -- here we are
# cropping the face from the image (these coordinates were
# determined using photo editing software such as Photoshop,
# GIMP, Paint, etc.)
face = image[163:352, 402:660]
cv2.imshow("Face", face)
cv2.waitKey(0)

# apply another image crop, this time extracting the body
body = image[163:649, 377:680]
cv2.imshow("Body", body)
cv2.waitKey(0)