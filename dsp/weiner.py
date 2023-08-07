# Python program to implement weiner filter

import numpy as np

blur_filter = np.array([[1,1,2,1],[2,1,1,2],[1,3,2,1],[2,1,2,1]])
print("Blur filter: \n",blur_filter)

# Calculating the fourier transform of the blur filter

from scipy.fftpack import fft2, fftshift

ft_blur_filter = np.fft.fft2(blur_filter)

print("Fourier transform of the blur filter: \n",ft_blur_filter)

# conjugate of the fourier transform of the blur filter
conj_fft_blur_filter = np.conj(ft_blur_filter)
print("Conjugate of the fourier transform of the blur filter: \n",conj_fft_blur_filter)

# calculating the magnitude of the fourier transform of the blur filter
magnitude_fft_blur_filter = np.abs(ft_blur_filter)**2
print("Magnitude of the fourier transform of the blur filter: \n",magnitude_fft_blur_filter)

K = 2 # Noise to signal ratio
# Calculating the weiner filter

weiner_filter = conj_fft_blur_filter/(magnitude_fft_blur_filter + K)

print("Weiner filter: \n",weiner_filter)



# Reading an image
import cv2
image = cv2.imread("images\image5.jpeg")
# Converting image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Applying the blur filter in frequency domain
blurred_image = cv2.filter2D(gray,-1,blur_filter)

# Calculating the fourier transform of the blurred image
ft_blurred_image = np.fft.fft2(blurred_image)



#plying the weiner filter
weiner_image = blurred_image * weiner_filter

# Converting the weiner image to spatial domain
weiner_image = np.fft.ifft2(weiner_image)

# Displaying the original image and the weiner filtered image
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 3, figsize=(10, 5))
# Plot data on the first subplot
axes[0].imshow(blurred_image,label="Original Image",cmap="gray")
axes[0].set_title("Original Image")
# Plot data on the second subplot
axes[1].imshow(weiner_image, label="Weiner Filtered Image",cmap="gray")
axes[1].set_title("Weiner Filtered Image")

# Plot data on the third subplot
axes[2].imshow(gray, label="Gray Image",cmap="gray")
axes[2].set_title("Gray Image")
plt.show()


