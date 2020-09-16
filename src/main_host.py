from colorama import Fore
from dateutil import parser

from services import data_services as services 
from infrastructure import state, switchlang


def decorate(func):
  def wrapper(msg):
    print(f'''  
      ******************************************************************************************************
    ''', end='\n \t\t')
    func(msg)
    print('''
      ******************************************************************************************************
    ''')
  return wrapper


def show_options():
  print(f'''{Fore.LIGHTCYAN_EX}
    What do you wanna do ?

    [C]reate an account.
    [L]og in to your account.
    List [Y]our cages.
    [R]egister a cage.
    [U]pdate cage availability.
    [M]y bookings.
    [S]witch mode.
    e[X]it app.
    [?] Help
    {Fore.CYAN}''')


def get_option():
  text = '>'
  if state.active_account:
    text = f'{Fore.BLUE}{state.active_account.name}>{Fore.CYAN}'

  action = input(text)
  return action.strip().upper()


@decorate
def error_msg(msg):
  print(Fore.RED + msg + Fore.CYAN)


@decorate
def success_msg(msg):
  print(Fore.LIGHTGREEN_EX + msg + Fore.CYAN)


def exit():
  print('''
    ********** BYE **********
  ''')
  raise KeyboardInterrupt


def create_account():
  if state.active_account:
    error_msg("You already have an account")
    return
  print('\n       ********** Register **********    \n')
  name = input('Enter your name....')
  email = input('Enter your email....').strip().lower()
  if services.find_account_by_email(email):
    error_msg('!! This email is already in use !!')
    return
  state.active_account = services.create_account(name, email)
  success_msg(f'Successfully Created Account For {name} with ID >> {state.active_account.id}')


def login():
  if state.active_account:
    error_msg("You are already logged in")
    return
  print('\n       ********** Login **********   \n')
  email = input('Please Enter Your Email.... ')
  user = services.find_account_by_email(email)
  if not user:
    error_msg('This email is not registered yet, please create an account')
    return
  state.active_account = user
  success_msg(f'Welcome {user.name.upper()}') 


def register_cage():
  if not state.active_account:
    error_msg('Please Log In To Register')
    return
  print('       ********** Register Cage **********')
  name = input('Enter your cage name.... ')
  area = (float(input('Enter area for your cage.... [numbers only]')))
  assert type(area) == float, 'Should be Num'
  is_carpeted = (input('Is your cage carpeted [y/n] ?').strip().lower().startswith('y'))
  has_toys = (input('Does it has toys ? [y/n] ?').strip().lower().startswith('y'))
  
  cage = services.register_cage(state.active_account, name, area, is_carpeted, has_toys)

  state.reload_account()
  success_msg(f'Registered Cage Successfully With ID > {cage.id}')


def list_cages():
  if not state.active_account:
    error_msg('Please Log In To List Cage')
    return
  cages = services.user_cages(state.active_account)
  # bookings = services.user_bookings(state.active_account)
  if cages:
    print('\n       ********** Your Cages **********    \n')
    print(f"    You've total of {Fore.GREEN}{len(cages)}{Fore.CYAN} cages.")
    print()
    for i, cage in enumerate(cages):
      print(f'      {i+1}. {cage.name} - {cage.area}sq.ft')
      for booking in cage.bookings:
        isBooked = 'No'
        if booking.booked_date: 
          isBooked = 'Yes'   
        print(f'        * Booking : {booking.checked_in} {(booking.checked_out - booking.checked_in).days} days | Booked? {isBooked}')
    return

  error_msg('No Cages To Show')


def update_availability():
  if not state.active_account:
    error_msg('Please Log In To List Cage')
    return
  list_cages()
  cage_no = int(input('Enter cage no. to update.... '))
  cages = services.user_cages(state.active_account)
  selected_cage = cages[cage_no - 1]

  success_msg(f'Selected Cage - {selected_cage}')
  start_date = parser.parse(input('Enter available date [dd-mm-yyyy]: '))
  days = int(input('For how many days?:  ')) 
  services.update_cage(selected_cage, start_date, days)


def for_host():
  print('       ********** Welcome Host **********')

  while 1:
    show_options()
    action = get_option()

    with switchlang.switch(action) as s:
      s.case('C', create_account)
      s.case('L', login)
      s.case('R', register_cage)
      s.case('Y', list_cages)
      s.case('U', update_availability)
      s.case('S', lambda: 'mode_change')
      s.case(['X', 'exit', 'quit', 'exit()', 'quit()', 'bye'], exit)
      # s.case('L', log_into_account)
    state.reload_account()

    if s.result == 'mode_change':
      return




