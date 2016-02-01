import numpy as np
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import mean_squared_error

import utils

# read csv data
X, y = utils.readCsv()

# split data in train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=0)

# grid search parameter settings
param_grid = [
    {'C': [50000000, 100000000, 500000000],
     'gamma': [0.05, 0.01, 0.001],
     'epsilon': [200000],
     'kernel': ['rbf']},
]

print "# Tuning hyper-parameters for mean squared error"
print ""

clf = GridSearchCV(svm.SVR(C=1, max_iter=10000),
    param_grid,
    cv=5,
    scoring='mean_squared_error')
clf.fit(X_train, y_train)

print "Best parameters set found on development set:"
print ""
print clf.best_params_
print ""
print "Grid scores on development set:"
print ""
for params, mean_score, scores in clf.grid_scores_:
    print("%0.3f (+/-%0.03f) for %r"
          % (mean_score, scores.std() * 2, params))
print ""

print "Root mean squared error report:"
print ""
print "The model is trained on the full development set."
print "The scores are computed on the full evaluation set."
print ""
y_true, y_pred = y_test, clf.predict(X_test)
print np.sqrt(mean_squared_error(y_true, y_pred))
print ""    
