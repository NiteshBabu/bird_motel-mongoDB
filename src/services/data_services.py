import datetime

from data.owner import Owner
from data.birds import Bird
from data.cage import Cage
from data.booking import Booking

def create_account(name:str, email:str) -> Owner:
  owner = Owner()
  owner.name = name
  owner.email = email

  owner.save()

  return owner 


def find_account_by_email(email):
  owner = Owner.objects.filter(email=email).first()
  # shorthand to filter
  # owner = Owner.objects(email=email).first()
  return owner

def register_cage(user : Owner, name, area, is_carpeted, has_toys) -> Cage:
  cage = Cage()
  cage.name = name
  cage.price = 10.0
  cage.area = area 
  cage.is_carpeted = is_carpeted
  cage.has_toys = has_toys

  cage.save()

  user = find_account_by_email(user.email)
  user.cage_id.append(cage.id)
  user.save()

  return cage


def user_cages(user : Owner) -> list :
  # user = find_account_by_email(user.email)
  query = Cage.objects(id__in=user.cage_id)
  cages = list(query)

  return cages


def update_cage(selected_cage, start_date, days):
  booking = Booking()
  booking.checked_in = start_date
  booking.checked_out = start_date + datetime.timedelta(days=days)
  cage = Cage.objects(id=selected_cage.id).first()
  cage.bookings.append(booking)
  cage.save()

  return cage


def add_bird(owner, name, weight, species, can_fly) -> Bird:
  bird = Bird()
  bird.name = name
  bird.weight = weight
  bird.species = species
  bird.can_fly = can_fly
  bird.save()

  owner = find_account_by_email(owner.email)
  owner.bird_id.append(bird.id)
  owner.save()

  return bird


def user_birds(user : Owner) -> list:
  birds = list(Bird.objects(id__in=user.bird_id))

  return birds