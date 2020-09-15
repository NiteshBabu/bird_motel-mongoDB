import mongoengine


class Owner(mongoengine.Document):
  name = mongoengine.StringField(required=True)
  email = mongoengine.StringField(required=True)

  bird_id = mongoengine.ListField()
  cage_id = mongoengine.ListField()

  meta = {
    'alias' : 'core',
    'collection' : 'owner'
  }


