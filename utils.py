import numpy as np
from sklearn import preprocessing
from sklearn.externals import joblib

def writeCsv(apts):
    # construct array of observations
    datapoints = [(a.livingArea, a.rooms, a.floor, a.rent,
        a.soldareas_set[0].area.priceIndex) for a in apts]
    # standardize data
    scaler = preprocessing.StandardScaler().fit(datapoints)
    datapoints = scaler.transform(datapoints)
    # write scaler object to file
    joblib.dump(scaler, 'scaler.pkl', compress=3)
    # write data to csv file
    with open("data.csv", "w") as csvFile:
        csvFile.write("soldPrice,livingArea,rooms,floor,rent,priceIndex\n")
        for i, d in enumerate(datapoints):
            csvFile.write(str(apts[i].soldPrice) + "," +
                ",".join(str(v) for v in d) + "\n")

def readCsv():
    # read data from csv
    with open('data.csv', 'r') as csvFile:
        X = [line.split(',')[1:] for line in csvFile][1:]
        csvFile.seek(0)
        y = [line.split(',')[0] for line in csvFile][1:]
    X = np.array([[float(n) for n in x] for x in X])
    y = np.array([float(n) for n in y])
    return (X, y)

def getScaler():
    return joblib.load('scaler.pkl')

def writeSVM(clf):
    joblib.dump(clf, 'svm.pkl', compress=3)

def getSVM():
    return joblib.load('svm.pkl')
