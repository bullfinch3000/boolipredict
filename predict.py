import utils

# load SVM fit
clf = utils.getSVM()

# load scaler
scaler = utils.getScaler()

# predict
# soldPrice,livingArea,rooms,floor,rent,priceIndex
X = [[45, 2, 3, 2600, 64286]]
print X[0]
X = scaler.transform(X)
y_pred = clf.predict(X)
print y_pred[0]
