# Running replicate padding

import numpy as np
import cv2
from fractions import Fraction



input_signal = np.array([[1,2,5,4,3],[4,3,2,0,0],[6,2,4,1,0],[4,3,6,2,1],[2,5,6,1,3]],dtype=np.float32)
print("Input signal: \n",input_signal)

mean_filter = np.ones((5,5),dtype=np.float32)
print("Mean filter: \n",mean_filter)

# Applying replicate padding
padded_signal = cv2.copyMakeBorder(input_signal,4,4,4,4,cv2.BORDER_REPLICATE)

print("Padded signal: \n",padded_signal)

# Applying convolution

output_signal = cv2.filter2D(padded_signal,-1,mean_filter)

print("Output signal: \n",output_signal)

# PLotting the results
import matplotlib.pyplot as plt



fig, axes = plt.subplots(1, 3, figsize=(10, 5))
# Plot data on the first subplot
axes[0].imshow(input_signal,label="Input signal",cmap="gray")
axes[0].set_title("Input signal")
# Plot data on the second subplot
axes[1].imshow(mean_filter, label="Mean filter",cmap="gray")
axes[1].set_title("Mean filter")
# Plot data on the third subplot
axes[2].imshow(output_signal, label="Output signal",cmap="gray")
axes[2].set_title("Output signal")
plt.show()
