# -*- coding: utf-8 -*-
"""rainy_sunny_road .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iXVOW_-a49-eWV3MJ3BaUg9eCDb2xxBb
"""

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

"""# **Rainy Road **

"""

from google.colab.patches import cv2_imshow

image_path = "/content/istockphoto-1084242954-170667a (1).jpg"
image = cv2.imread(image_path) #converts the image into multidimensional numpy array
cv2_imshow(image)
#cv2.waitKey(0)
plt.imshow(image)

from google.colab import drive
drive.mount('/content/drive')

#Grayscale
lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
print("GRAY-SCALE")
cv2_imshow(gray)
cv2.waitKey(0)



#Gaussian blur
blur = cv2.GaussianBlur(gray, (5,5), 2)
print("GAUSSIAN BLUR")
cv2_imshow(blur)
cv2.waitKey(0)



#applying canny edge function
c = cv2.Canny(blur, 50,80)
print("CANNY EDGE DETECTION")
cv2_imshow(c)
cv2.waitKey(0)

import cv2
import numpy as np
from google.colab.patches import cv2_imshow  # Import cv2_imshow for displaying images in Colab

def detect_white_lanes(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define a lower and upper range for white color detection in HSV
    lower_white = np.array([0, 0, 200], dtype=np.uint8)
    upper_white = np.array([180, 30, 255], dtype=np.uint8)

    # Create a mask for white color
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Bitwise AND to extract white lanes
    white_lanes = cv2.bitwise_and(image, image, mask=mask)

    return white_lanes

# Path to the road image file
image_path = '/content/istockphoto-1084242954-170667a (1).jpg'

# Detect and display only the white lanes in the road image
result_white_lanes = detect_white_lanes(image_path)

# Display the white lanes only using cv2_imshow for Colab
cv2_imshow(result_white_lanes)

import cv2
import numpy as np
import os
from PIL import Image

def detect_white_lanes(image):
    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define a lower and upper range for white color detection in HSV
    lower_white = np.array([0, 0, 200], dtype=np.uint8)
    upper_white = np.array([180, 30, 255], dtype=np.uint8)

    # Create a mask for white color
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Bitwise AND to extract white lanes
    white_lanes = cv2.bitwise_and(image, image, mask=mask)

    return white_lanes

def calculate_accuracy(detected_image, ground_truth_image):
    # Resize both images to a common size
    common_size = (min(detected_image.shape[1], ground_truth_image.shape[1]),
                   min(detected_image.shape[0], ground_truth_image.shape[0]))
    detected_resized = cv2.resize(detected_image, common_size)
    ground_truth_resized = cv2.resize(ground_truth_image, common_size)

    # Convert both resized images to grayscale
    detected_gray = cv2.cvtColor(detected_resized, cv2.COLOR_BGR2GRAY)
    ground_truth_gray = cv2.cvtColor(ground_truth_resized, cv2.COLOR_BGR2GRAY)

    # Calculate absolute difference between the two grayscale images
    diff = cv2.absdiff(detected_gray, ground_truth_gray)

    # Calculate accuracy by counting non-zero pixels (pixels that are different)
    accuracy = 1 - (np.count_nonzero(diff) / float(detected_gray.size))
    return accuracy

# Path to the road image file
image_path = '/content/istockphoto-1084242954-170667a (1).jpg'

# Read the detected white lanes image
result_white_lanes = detect_white_lanes(cv2.imread(image_path))

# Path to the ground truth image file
ground_truth_path = '/content/istockphoto-1084242954-170667a (1).jpg'

# Read the ground truth image
ground_truth_image = cv2.imread(ground_truth_path)

# Display the detected white lanes and ground truth images using PIL
Image.fromarray(result_white_lanes).show()
Image.fromarray(cv2.cvtColor(ground_truth_image, cv2.COLOR_BGR2RGB)).show()

# Calculate accuracy
accuracy = calculate_accuracy(result_white_lanes, ground_truth_image)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Check if the ground truth image file exists
if os.path.exists(ground_truth_path):
    print("Ground truth image file exists.")
else:
    print("Ground truth image file does not exist. Please check the path.")

import cv2
from google.colab.patches import cv2_imshow
import numpy as np

# Assuming c1 is your image variable
c1 = cv2.imread('/content/istockphoto-1084242954-170667a (1).jpg')

# Bitwise on the canny edge image
def region_of_int(image):
    height = image.shape[0]
    # Coordinates of the triangular region
    polygons = np.array([
        [(600, height), (150, height), (200, 100)]
    ])
    # Create a black image with the same dimensions as the original image
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

cropped_image = region_of_int(c1)
cv2_imshow(cropped_image)
cv2.waitKey(0)

import cv2
import numpy as np
from google.colab.patches import cv2_imshow  # Import cv2_imshow for displaying images in Colab

def detect_white_lanes(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define a lower and upper range for white color detection in HSV
    lower_white = np.array([0, 0, 200], dtype=np.uint8)
    upper_white = np.array([180, 30, 255], dtype=np.uint8)

    # Create a mask for white color
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Bitwise AND to extract white lanes
    white_lanes = cv2.bitwise_and(image, image, mask=mask)

    return white_lanes

# Path to the road image file
image_path = '/content/istockphoto-1084242954-170667a (1).jpg'

# Detect and display only the white lanes in the road image
result_white_lanes = detect_white_lanes(image_path)

# Display the white lanes only using cv2_imshow for Colab
cv2_imshow(result_white_lanes)

import cv2
import numpy as np
from google.colab.patches import cv2_imshow  # Import cv2_imshow for displaying images in Colab

def detect_and_display_blue_lanes(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define a lower and upper range for white color detection in HSV
    lower_white = np.array([0, 0, 200], dtype=np.uint8)
    upper_white = np.array([180, 30, 255], dtype=np.uint8)

    # Create a mask for white color
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Bitwise AND to extract white lanes
    white_lanes = cv2.bitwise_and(image, image, mask=mask)

    # Set green and red channels to zero in the white lanes region, turning them blue
    white_lanes[:, :, 1] = 0  # Green channel
    white_lanes[:, :, 2] = 0  # Red channel

    return white_lanes

# Path to the road image file
image_path = '/content/istockphoto-1084242954-170667a (1).jpg'

# Detect and display only the white lanes in the road image in blue color
result_blue_lanes = detect_and_display_blue_lanes(image_path)

# Display the blue lanes using cv2_imshow for Colab
cv2_imshow(result_blue_lanes)

import cv2
import numpy as np
from google.colab.patches import cv2_imshow  # Import cv2_imshow for displaying images in Colab

def detect_and_display_blue_lanes(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define a mask for the sky region based on color (you may need to adjust these values)
    lower_sky = np.array([0, 0, 150], dtype=np.uint8)
    upper_sky = np.array([180, 100, 255], dtype=np.uint8)
    sky_mask = cv2.inRange(hsv, lower_sky, upper_sky)

    # Define a lower and upper range for white color detection in HSV
    lower_white = np.array([0, 0, 200], dtype=np.uint8)
    upper_white = np.array([180, 30, 255], dtype=np.uint8)

    # Create a mask for white color
    lane_mask = cv2.inRange(hsv, lower_white, upper_white)

    # Bitwise AND to extract white lanes
    white_lanes = cv2.bitwise_and(image, image, mask=lane_mask)

    # Set green and red channels to zero in the white lanes region, turning them blue
    white_lanes[:, :, 1] = 0  # Green channel
    white_lanes[:, :, 2] = 0  # Red channel

    # Invert the lane mask to get the sky mask
    sky_mask_inv = cv2.bitwise_not(lane_mask)

    # Set green and red channels to zero in the sky region, keeping them black
    image_sky_black = cv2.bitwise_and(image, image, mask=sky_mask_inv)

    # Combine the sky and lanes images to get the final result
    result = cv2.add(image_sky_black, white_lanes)

    return result

# Path to the road image file
image_path = '/content/istockphoto-1084242954-170667a (1).jpg'

# Detect and display only the white lanes in the road image in blue color (excluding sky)
result_blue_lanes = detect_and_display_blue_lanes(image_path)

# Display the blue lanes using cv2_imshow for Colab
cv2_imshow(result_blue_lanes)

"""**# Autumn season**"""

#AUTUMN SEASON

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img = cv2.imread('/content/Road.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)
mask = np.zeros_like(edges)
height, width = mask.shape
polygon = np.array([[
    (0, height),
    (width, height),
    (width // 2, height // 2)
]])
cv2.fillPoly(mask, polygon, 255)
masked_edges = cv2.bitwise_and(edges, mask)

lines = cv2.HoughLinesP(masked_edges, rho=6, theta=np.pi/60, threshold=160, lines=np.array([]), minLineLength=40, maxLineGap=25)

line_img = np.zeros_like(img)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(line_img, (x1, y1), (x2, y2), (0, 0, 255), 10)

result = cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)

cv2_imshow(result)