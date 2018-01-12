from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#random data list
#xs = [1,2,3,4,5,6]
#ys = [5,4,6,5,6,7]

#numpy array list and data type
xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([5,4,6,5,6,7], dtype=np.float64)

# liner line show
plt.plot(xs,ys)

# showing only plot point
plt.scatter(xs,ys)
#plt.show()

# function of m(slope) and b = y intercept
def best_fit_slop_and_intercept(xs,ys):
    m = ( ((mean(xs) * mean(ys)) - mean(xs * ys) ) /
          ((mean(xs)*mean(xs)) - mean((xs*xs))  )
        )
    b = mean(ys) - m * mean(xs)
    return  m, b

m,b = best_fit_slop_and_intercept(xs,ys)

regression_line = [ (m*xs) + b for  x in xs ]

# predict number 8
predict_x = 8
predict_y = (m*predict_x) + b

# print regression line
plt.scatter(xs,ys)
# print predict data 8 with color 8
plt.scatter(predict_x,predict_y, color='g')
plt.plot(xs,regression_line)
plt.show()