from data.owner import Owner
import services.data_services as services 

active_account = None

def reload_account():
  global active_account
  if active_account:
    active_account = services.find_account_by_email(active_account.email) 