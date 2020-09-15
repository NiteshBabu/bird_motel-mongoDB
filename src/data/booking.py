import mongoengine

class Booking(mongoengine.EmbeddedDocument):
  guest_user_id = mongoengine.ObjectIdField()
  guest_bird_id = mongoengine.ObjectIdField()
  booked_date = mongoengine.DateTimeField()
  checked_in = mongoengine.DateTimeField(required=True)
  checked_out =mongoengine.DateTimeField(required=True)

  ratings = mongoengine.IntField(default=0)
  reviews = mongoengine.StringField()