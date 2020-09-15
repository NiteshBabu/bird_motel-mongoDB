import mongoengine
from datetime import datetime
from .booking import Booking

class Cage(mongoengine.Document):
  date_registered = mongoengine.DateTimeField(default = datetime.now)
  name = mongoengine.StringField(required=True)
  price = mongoengine.DecimalField(required=True)
  area = mongoengine.FloatField(required=True)
  is_carpeted = mongoengine.BooleanField()
  has_toys = mongoengine.BooleanField()

  bookings = mongoengine.EmbeddedDocumentListField('Booking')

  meta = {
    'alias' : 'core',
    'collection' : 'cage'
  }