import numpy
from scipy import stats

test_scores =[12, 99, 86, 87, 88, 45, 87, 94, 78, 77, 85, 86]
my_mode = stats.mode(test_scores)
print("The mode is ", my_mode)