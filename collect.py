#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib
import time
from hashlib import sha1
import random
import string
import json

from models import *

CALLER_ID = "boolipredict"
API_KEY = "I726DsV6BtcVa1PUyHILq7FfMG1Fv9MiKiaaM21W"

# connect to Booli API and download data
def query(limit = 35, offset = 0):
    # construct URL
    timestamp = str(int(time.time()))
    unique = ''.join(random.choice(string.ascii_uppercase + string.digits)
        for x in range(16))
    hashstr = sha1(CALLER_ID+timestamp+API_KEY+unique).hexdigest()
    url = "/sold?areaId=2&objectType=lägenhet&limit="+str(limit)+\
        "&offset="+str(offset)+"&callerId="+CALLER_ID+"&time="+\
        timestamp+"&unique="+unique+"&hash="+hashstr
    # make request
    connection = httplib.HTTPConnection("api.booli.se")
    connection.request("GET", url)
    response = connection.getresponse()
    data = response.read()
    connection.close()   
    if response.status != 200:
        print "fail"
    return json.loads(data)



# query Booli
limit = 35
offset = 0
result = query(limit, offset)
totalCount = result['totalCount']

# read data and store in local database
db.connect()
while offset < totalCount:
    # store data locally
    for apt in result['sold']:
        # get or create sold object
        try:
            s = Sold.get(Sold.booliId == apt['booliId'])
        except Sold.DoesNotExist:
            s = Sold.create(
                booliId = apt['booliId'],
                listPrice = apt['listPrice'] if ('listPrice' in apt) else None,
                soldPrice = apt['soldPrice'],
                rent = apt['rent'] if ('rent' in apt) else None,
                floor = apt['floor'] if ('floor' in apt) else None,
                livingArea = apt['livingArea'] if ('livingArea' in apt) else None,
                rooms = apt['rooms'] if ('rooms' in apt) else None,
                soldDate = apt['soldDate']
                )
            s.save()
        # store area
        if ('namedAreas' in apt['location']):
            for areaName in apt['location']['namedAreas']:
                # get or create area object
                try:
                    a = Area.get(Area.name == areaName)
                except Area.DoesNotExist:
                    a = Area.create(name = areaName)
                    a.save()
                # get or create sold-area relationship
                try:
                    sa = SoldAreas.get(SoldAreas.sold == s, SoldAreas.area == a)
                except SoldAreas.DoesNotExist:
                    sa = SoldAreas.create(sold = s, area = a)
                    sa.save()
    print "Stored data from " + str(offset) + " to " + str(offset + limit) + \
        " of " + str(totalCount)
    # query for next batch of listings
    offset += limit
    result = query(limit, offset)

