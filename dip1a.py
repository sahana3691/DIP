import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("sample1.jpg")
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
