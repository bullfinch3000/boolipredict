from peewee import *

# create a peewee database instance -- our models will use this database to
# persist information
db = SqliteDatabase('apts.db')

# model definitions -- the standard "pattern" is to define a base model class
# that specifies which database to use.  then, any subclasses will automatically
# use the correct storage.
class BaseModel(Model):
    class Meta:
        database = db

class Sold(BaseModel):
    booliId = IntegerField()
    listPrice = IntegerField(null = True)
    soldPrice = IntegerField()
    rent = IntegerField(null = True)
    floor = IntegerField(null = True)
    livingArea = IntegerField(null = True)
    rooms = IntegerField(null = True)
    soldDate = DateTimeField()

    class Meta:
        order_by = ('soldDate',)

class Area(BaseModel):
    name = CharField()

    class Meta:
        order_by = ('name',)

class SoldAreas(BaseModel):
    sold = ForeignKeyField(Sold)
    area = ForeignKeyField(Area)
