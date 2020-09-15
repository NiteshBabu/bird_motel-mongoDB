from colorama import Fore
from dateutil import parser

from services import data_services as services 
from infrastructure import state, switchlang
import main_host as host 

def show_options():
  print(f'''{Fore.LIGHTCYAN_EX}
    What do you wanna do ?

    [C]reate an account.
    [L]og in to your account.
    [B]ook a cage.
    [A]dd your bird.
    [Y]our birds.
    [L]ist your bookings.
    [M]ain menu.
    e[X]it app.
    [?] Help
    {Fore.CYAN}''')

def book_cage():
  if not state.active_account:
    host.error_msg("Please log in to continue")
    return
  print('\n       ********** Book Cage **********   \n')


def add_bird():
  if not state.active_account:
    host.error_msg("Please log in to continue")
    return
  print('\n       ********** Add Bird **********   \n')
  name = input("What's your bird's name? ")
  weight = float(input("What's it weight? "))
  species = input("Which species is it? ")
  can_fly = input("Can it fly? [y/n] ").strip().lower().startswith('y')

  bird = services.add_bird(state.active_account, name, weight, species, can_fly)
  host.success_msg(f"Successfully added bird with id > {bird.id}")


def list_birds():
  if not state.active_account:
    host.error_msg("Please log in to continue")
    return
  print('\n       ********** My Birds **********   \n')
  birds = services.user_birds(state.active_account)
  if not birds:
    host.error_msg("No birds to show")
    return
  print(f"  You've total of {len(birds)} birds")
  for i, bird in enumerate(birds):
    print(f"    {i+1}. {bird.name} from {bird.species} species")

def for_guest():
  print('       ********** Welcome Guest **********')

  while 1:
    show_options()
    action = host.get_option()

    with switchlang.switch(action) as s:
      s.case('C', host.create_account)
      s.case('L', host.login)
      s.case('B', book_cage)
      s.case('A', add_bird)
      s.case('Y', list_birds)
      # s.case('L', my_bookings)
      s.case('M', lambda: 'mode_change')
      s.case(['X', 'exit', 'quit', 'exit()', 'quit()', 'bye'], exit)
    state.reload_account()

    if s.result == 'mode_change':
      return
