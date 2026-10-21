from numpy import random
from statsmodels.api import qqplot
from matplotlib.pyplot import show as show_plot

data = random.normal(0, 1, 100)
qqplot(data, line="45")
show_plot()
