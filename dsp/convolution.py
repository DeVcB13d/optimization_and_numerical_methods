# Run convolution and correlation operation between 2 matrices

import numpy as np
from scipy.signal import correlate
from scipy.signal import convolve2d
import cv2 

# Assuming matrix1 and matrix2 are two 2D matrices of the same shape
# Perform 2D convolution between the two matrices
#input_matrix = np.array([[5,4,5],[3,2,3],[1,8,5]])
input_matrix = cv2.imread("images\image4.jpeg")
input_matrix = cv2.cvtColor(input_matrix, cv2.COLOR_BGR2GRAY)
# vertical edge detection
#kernel = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

# horizontal edge detection
#kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])

# Laplacian edge detection 1
kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])

# Laplacian edge detection 2
#kernel = np.array([[1,1,1],[1,-8,1],[1,1,1]])

# Sobel edge detection
#kernel = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

# Prewitt edge detection
#kernel = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

# Gaussian blur
#kernel = np.array([[1,2,1],[2,4,2],[1,2,1]])

# Moving average filter
#kernel = np.ones((5,5),np.float32)/25

# blur filter
kernel = np.array([[1,1,2,1],[2,1,1,2],[1,3,2,1],[2,1,2,1]])

result_conv_2d = convolve2d(input_matrix, kernel, mode='full', boundary='fill', fillvalue=0)

# For 2D correlation
result_corr_2d = correlate(input_matrix, kernel, mode='full')

print("Input matrix: \n",input_matrix)
print("Kernel: \n",kernel)
print("Convolution output: \n",result_conv_2d)
print("Correlation output: \n",result_corr_2d)

# plotting the input matrix and the output matrix

import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 3, figsize=(10, 5))
# Plot data on the first subplot
axes[0].imshow(input_matrix,label="Input Matrix",cmap="gray")
axes[0].set_title("Input Matrix")
# Plot data on the second subplot
axes[1].imshow(result_conv_2d, label="Convolution Output",cmap="gray")
axes[1].set_title("Convolution Output")
# Plot data on the third subplot
axes[2].imshow(result_corr_2d, label="Correlation Output",cmap="gray")
axes[2].set_title("Correlation Output")

plt.show()

