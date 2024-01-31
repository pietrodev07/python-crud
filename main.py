from services.users import get_users, get_user
from utils.view import show_users, show_user

while (True):
  print("Choice the operation that you would to execute")

  print("Digit <1> to view all users")
  print("Digit <2> to view a specific user (by id)")
  print("Digit <3> to exit")

  choice = 0

  try:
    choice = int(input())
  except ValueError:
    print("Inserire solo numeri")

  match choice:
    case 1:
      users = get_users()
      show_users(users)
    case 2:
      id = int(input("Inserisci l'id dell'utente: "))
      user = get_user(id)

      if user is not None:
        show_user(user)
    case 3:
      break