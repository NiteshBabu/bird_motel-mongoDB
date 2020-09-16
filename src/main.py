from colorama import Fore

from data import mongo_setup
import main_host as host
from main_guest import for_guest  

def main():
  mongo_setup.global_init()
  print(Fore.CYAN + '''
            ********** Welcome To The Birds Motel **********
    Here You Can :- 

    [B]ook a cage for your bird.
    [O]ffer a cage for bird.
  ''')

  try :
    while 1:
      choice = input('''
        I'm a bird owner looking for a cage, press [B],
        I'm a cage owner renting a cage, press [O] 
>''')
      if choice.upper() == 'B':
        for_guest()
      elif choice.upper() == 'O':
        host.for_host()
      else:
        host.error_msg(' Wrong Input, Please Select The Correct One ')
  except KeyboardInterrupt:
    print('''
    ********** BYE **********
    ''')
    return


if __name__ == '__main__':
  main()
