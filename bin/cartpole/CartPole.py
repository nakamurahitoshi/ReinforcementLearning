# coding: UTF-8
# written in UTF-8
import numpy as np
import matplotlib.pyplot as plt
points = np.arange(-5,5,0.01)
xs, ys=np.meshgrid(points,points) # 行列ができた。範囲中の、各点に対応。
z = np.sqrt(xs**2+ys**2) # 範囲中の各点において計算される。
plt.imshow(z,cmap=plt.cm.gray)	# imshowで、グラフの可視化
plt.colorbar()
plt.title("image plot of $\sqrt{x^2 + y^2}$ for a grid of values") # $\~$で、Texみたいに書ける！