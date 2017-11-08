def new_password(oldpassword, newpassword):
    'controleert het nieuwe opgegeven wachtwoord op lengte en gelijkheid met het oude wachtwoord en past het oude wachtwoord aan'
    if newpassword != oldpassword and len(newpassword) >= 6 and any(char.isdigit() for char in newpassword):
        return True
    else:
        return False

print(new_password('test', 'testtest123'))
