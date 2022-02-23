import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def plot_linear_regression():
	# The slope (a) and the interception with y-axis (bias) are defined.
    a = 0.5
    b = 2.0

    # x from 0 to 10
    x = 20 * np.random.random(500)

    # y = a * x + b with noise
    y = a * x + b + np.random.normal(size=x.shape)

    # Create a linear regression classifier
    clf = LinearRegression()
    clf.fit(x[:, None], y)

    # Predict y from the data
    x_new = np.linspace(0, 30, 100)
    y_new = clf.predict(x_new[:, None])

    # Plot the results
    ax = plt.axes()
    ax.scatter(x, y, s=1)
    ax.plot(x_new, y_new, c='k', linewidth=.5)

    ax.set_xlabel('x')
    ax.set_ylabel('y')

    ax.axis('tight')


if __name__ == '__main__':
    plot_linear_regression()
    plt.show()
