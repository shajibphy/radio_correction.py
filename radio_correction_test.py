import cv2
import numpy as np

# Load the dark image, light image, and measurement image
dark_image_path = r"C:\Users\Shafiul\Desktop\img\capture_img\dark_5K.png"
light_image_path = r"C:\Users\Shafiul\Desktop\img\capture_img\light_5K.png"
measurement_image_path = r"C:\Users\Shafiul\Desktop\img\capture_img\measure_5K.png"

dark_image = cv2.imread(dark_image_path, cv2.IMREAD_UNCHANGED).astype(np.float32)
light_image = cv2.imread(light_image_path, cv2.IMREAD_UNCHANGED).astype(np.float32)
measurement_image = cv2.imread(measurement_image_path, cv2.IMREAD_UNCHANGED).astype(np.float32)

# Compute the difference between each pixel in the light and dark images
difference_image = light_image - dark_image

# Perform dark signal correction by subtracting the dark image from the measurement image
dark_corrected_image = measurement_image - dark_image

# Clip dark-corrected values to ensure they are non-negative
dark_corrected_image = np.maximum(dark_corrected_image, 0)

# Perform system response correction by dividing by the difference image
corrected_image = dark_corrected_image / difference_image

# Clip the pixel values to ensure they are within the valid range (0 to 1.0)
corrected_image = np.clip(corrected_image, 0, 1.0)

# Save the corrected image (you can change the file path as needed)
output_path = r"C:\Users\Shafiul\Desktop\img\capture_img\corrected_img.png"
cv2.imwrite(output_path, (corrected_image * 65535).astype(np.uint16))
