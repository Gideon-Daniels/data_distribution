import numpy
test_scores = [12, 99, 86, 87, 88, 45, 87, 94, 78, 77, 85, 86]
x = numpy.percentile(test_scores, 75)
print("The 75% percentile for the marks is ", x)
