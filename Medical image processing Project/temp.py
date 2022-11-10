"""
from PIL import Image 
import matplotlib.pyplot as plt
import numpy as np 
import cv2

Input_im=np.array(Image.open('hand.png'))
output_im_med=cv2.medianBlur(Input_im,15)
output_im_avg=cv2.blur(Input_im,(15,15))
plt.gray()
plt.Figure()
plt.subplot(1,3,1)
plt.imshow(Input_im)
plt.subplot(1,3,2)
plt.imshow(output_im_med)
plt.subplot(1,3,3)
plt.imshow(output_im_avg)
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
input_image = np.array(Image.open('CT_Spine.png'))
plt.Figure()
plt.hist(input_image)

