def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6 and any(char.isdigit() for char in newpassword):
        return True
    else:
        return False

print(new_password('test', 'testtest123'))
