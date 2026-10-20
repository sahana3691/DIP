import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("sample1.jpg")
res=cv2.resize(img,(300,300))
cv2.imshow("resize",res)
cv2.waitKey(0)
