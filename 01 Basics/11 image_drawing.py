# import necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="./Images/free-images.jpg",
                help="path to input image")
args = vars(ap.parse_args())

# load the input image from disk
image = cv2.imread(args["image"])

# draw a circle around face, two filled in circles covering
# eyes, and a rectangle over top of mouth
cv2.circle(image, (546, 259), 90, (0, 0, 255), 2)
cv2.circle(image, (512, 260), 10, (0, 0, 255), -1)
cv2.circle(image, (564, 260), 10, (0, 0, 255), -1)
cv2.rectangle(image, (515, 318), (564, 330), (0, 0, 255), -1)

# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)