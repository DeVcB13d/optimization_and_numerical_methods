import cv2
import numpy as np
import matplotlib.pyplot as plt

# function to plot two images side by side for comparison
def plot(img1,img2,title1="",title2=""): 
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    # Plot data on the first subplot
    axes[0].imshow(img1,label=title1,cmap="gray")
    axes[0].set_title(title1)
    # Plot data on the second subplot
    axes[1].imshow(img2, label=title2,cmap="gray")
    axes[1].set_title(title2)
    plt.show()

# Function to apply fourier transform on an image
def fourier_transform(image_path):
    # Reading the image
    image = cv2.imread(image_path)
    # Converting image to grayscale"
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Taking the fourier transform of the image4
    fourier = np.fft.fft2(gray,norm='ortho')
    # Shift the zero-frequency component to the center of the spectrum
    fourier_shift = np.fft.fftshift(fourier)
    # Calculating the magnitude of the fourier transform for shifted and unshifted
    magnitude_shift = np.abs(fourier_shift)

    # Scaling magnitude to lie between 0 and 255
    log_magnitude_spectrum = 20 * np.log10(1 + magnitude_shift)

    # Calculating the image energy
    img_energy = np.linalg.norm(gray,2,keepdims=False)
    # Calculating the fourier transform energy
    fourier_energy = np.linalg.norm(fourier_shift,2,keepdims=False)
    return log_magnitude_spectrum,img_energy,fourier_energy

def main():
    image_path = "images\image3.png"
    image = cv2.imread(image_path)
    ft_img,img_energy,fourier_energy = fourier_transform(image_path)
    # PLotting original image and shifted image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plot(image,ft_img,"Original Image","Fourier shifted Image")

    print("Energy in the spatial (time) domain: ",img_energy)
    print("Energy in the frequency domain: ",fourier_energy)

    normalization_factor = image.shape[0] * image.shape[1]
    # Verify Parseval's theorem
    tolerance = 1e-5
    if np.abs(img_energy - fourier_energy) < tolerance:
        print("Energy conserved")
    else:
        print("Energy not conserved")

if __name__ == "__main__":
    main()