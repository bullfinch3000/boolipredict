from collections import namedtuple

from models import *
import utils

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
            (Sold.livingArea > 0) &
            (Sold.rooms > 0) &
            (Sold.floor > 0) &
            (Sold.rent > 0) &
            (Sold.soldDate > "2015-07-01"))

# store data as csv
utils.writeCsv(apts)
