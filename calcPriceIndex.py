from models import *

# calculate average sqm price for each area
areaDict = {}
apts = Sold\
        .select()\
        .join(SoldAreas)\
        .join(Area)\
        .where((Sold.soldDate > "2015-07-01") &
            (Sold.livingArea != None))

# iterate all sold apartments and calculate the price per sqm
for apt in apts:
    sqmPrice = apt.soldPrice / apt.livingArea
    for sa in apt.soldareas_set:
        if sa.area.name in areaDict:
            areaDict[sa.area.name][0] += sqmPrice
            areaDict[sa.area.name][1] += 1
        else:
            areaDict[sa.area.name] = [sqmPrice, 1]

# update area model with a price index given by the average price per sqm
for key, val in areaDict.items():
    area = Area.get(name = key)
    area.priceIndex = val[0] / val[1]
    area.save()
