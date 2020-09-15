import mongoengine
from datetime import datetime

class Bird(mongoengine.Document):
  date_registered = mongoengine.DateTimeField(default = datetime.now)
  species = mongoengine.StringField(required=True)
  weight = mongoengine.FloatField(required=True)
  name = mongoengine.StringField(required=True)
  can_fly = mongoengine.BooleanField(required=True)

  meta = {
    'alias' : 'core',
    'collection' : 'bird'
  }
