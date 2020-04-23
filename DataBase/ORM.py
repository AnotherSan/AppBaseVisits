from peewee import *
import datetime

dbhandle = SqliteDatabase('LaterrsAndNot')

class BaseModel(Model):
    class Meta:
        database = dbhandle

class Workers(BaseModel):
        Number = PrimaryKeyField(null=False)
        FirstName = TextField(max_length=20)
        SecondName = TextField(max_length=20)
        Office = TextField()

class Control(BaseModel):
        Time = TimeField(max_length=10)
        Date = DateField(max_length=10)
        Workers_Number = ForeignKeyField(Workers, to_field='Number')
        Control_Number = PrimaryKeyField(null=False)

dbhandle.connect()
Control.create_table()
Workers.create_table()
