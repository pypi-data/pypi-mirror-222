import cv2
import numpy as np
import matplotlib.pyplot as plt

def Image_segmentation(num_clusters, image_path):
    # Read the image using OpenCV
    input_image = cv2.imread(image_path)

    # Convert the image from BGR to RGB (OpenCV uses BGR by default)
    image_rgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

    # Reshape the image to a 2D array of pixels (rows represent pixels, columns represent color channels)
    pixels = image_rgb.reshape(-1, 3).astype(np.float32)

    # Perform k-means clustering on the pixels
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixels, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convert the centers back to 8-bit integers (RGB color values)
    centers = np.uint8(centers)

    # Map the labels to the center values to get the segmented image
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(image_rgb.shape)

    return segmented_image

def display_original_gray_images(image_path):
    # ... Your existing code ...

    # Convert the input image to grayscale
    grayscale_image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)

    # Display the original, segmented, and grayscale images side by side
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.imread(image_path))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(grayscale_image, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')

    plt.show() 


def display_original_segmented_images(image_path):
    # Replace 'image_path' with the actual path to your image file

    # Define the number of clusters for k-means clustering
    num_clusters = int(input("Enter the number of clusters: "))  # You can adjust this value based on your requirement

    # Perform image segmentation using k-means clustering
    segmented_image = Image_segmentation(num_clusters, image_path)

    # Convert the input image to grayscale
    grayscale_image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)

    # Display the original, segmented, and grayscale images side by side
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.imread(image_path))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(segmented_image)
    plt.title('Segmented Image (K = {})'.format(num_clusters))
    plt.axis('off')



    plt.show() 


    