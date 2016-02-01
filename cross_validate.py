import numpy as np
from sklearn import svm
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error

import utils

# read csv data
X, y = utils.readCsv()

# 10 folds cross validation svm training
rmse = []
kf = KFold(len(X), n_folds=10)
for train, test in kf:
    clf = svm.SVR(C=100000000, gamma=0.01, epsilon=200000, kernel='rbf')
    clf.fit(X[train], y[train])
    y_pred = clf.predict(X[test])
    score = np.sqrt(mean_squared_error(y[test], y_pred))
    rmse.append(score)
    print "RMSE: %s" % score

print "Min RMSE: %s\nMax RMSE: %s\nMean RMSE: %s" % (
	np.min(rmse), np.max(rmse), np.mean(rmse))

# # Output
# RMSE: 464307.13222
# RMSE: 580966.456102
# RMSE: 519024.052988
# RMSE: 608102.489362
# RMSE: 606586.000127
# RMSE: 600282.364792
# RMSE: 613677.288467
# RMSE: 566937.13678
# RMSE: 516115.77492
# RMSE: 514819.93112
# Min RMSE: 464307.13222
# Max RMSE: 613677.288467
# Mean RMSE: 559081.862688
