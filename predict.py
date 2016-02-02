# usage: python predict.py livingArea rooms floor rent areaName
# example: python predict.py 48 2 2 2800 Abrahamsberg

import sys

from models import *
import utils

def main(args=None):
    # simple args parsing
    if args is None:
        args = sys.argv[1:]
    if len(args) != 5:
        print "Wrong number of arguments"
        sys.exit(2)
    try:
        livingArea = int(args[0])
        rooms = int(args[1])
        floor = int(args[2])
        rent = int(args[3])
        areaName = args[4]
    except:
        print "Wrong argument type"
        sys.exit(2)

    # read area price index from db
    try:
        area = Area.get(Area.name==areaName)
    except Area.DoesNotExist:
        print "Area not found"
        sys.exit(2)

    # load SVM fit
    clf = utils.getSVM()
    # load scaler
    scaler = utils.getScaler()

    # predict
    X = [[livingArea, rooms, floor, rent, area.priceIndex]]
    X = scaler.transform(X)
    y_pred = int(clf.predict(X)[0])

    # print prediction
    print "Input: %s rooms, %s m^2, floor %s, rent %s in %s" % (
        rooms, livingArea, floor, rent, areaName)
    print "Prediction: %s" % y_pred

    sys.exit(0)

if __name__ == '__main__':
    main()
