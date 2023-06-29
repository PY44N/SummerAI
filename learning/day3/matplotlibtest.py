import numpy
import matplotlib.pyplot as plot

# numpy.random.seed(19680801)

N = 50
x = numpy.random.rand(N)
y = numpy.random.rand(N)
colors = numpy.random.rand(N)
area = (30 * numpy.random.rand(N)) ** 2

plot.scatter(x, y, s=area, c=colors, alpha=0.5)
plot.show()