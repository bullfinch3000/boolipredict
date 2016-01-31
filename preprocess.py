from collections import namedtuple

from models import *

# read from database and put together data for training
apts = Sold\
        .select()\
        .join(SoldAreas)\
        .join(Area)\
        .where((Area.priceIndex != None) &
            (Sold.livingArea != None) &
            (Sold.rooms != None) &
            (Sold.floor != None) &
            (Sold.rent != None) &
            (Sold.soldDate > "2015-07-01"))

# store data as csv
datapoints = [(a.soldPrice, a.livingArea, a.rooms, a.floor, a.rent,
    a.soldareas_set[0].area.priceIndex) for a in apts]
with open("data.csv", "w") as csvFile:
    csvFile.write("soldPrice,livingArea,rooms,floor,rent,priceIndex\n")
    for d in datapoints:
        print d
        csvFile.write(",".join(str(v) for v in d) + "\n")
