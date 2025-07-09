from peewee import Model, SqliteDatabase

db = SqliteDatabase('cerrajeria2.db')

class BaseModel(Model):
    class Meta:
        database = db
