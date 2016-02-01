import numpy as np
from sklearn import svm
from sklearn.metrics import mean_squared_error

import utils

# read csv data
X, y = utils.readCsv()

# train svm
clf = svm.SVR(C=100000000, gamma=0.01, epsilon=200000, kernel='rbf')
clf.fit(X, y)

# evaluate fit on training data
y_pred = clf.predict(X)
score = np.sqrt(mean_squared_error(y, y_pred))
print "RMSE: %s" % score

# # Output
# RMSE: 545770.525711

# store svm
utils.writeSVM(clf)
