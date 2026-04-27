
    
class PasswordTooSmallError(Exception):
    """raised when the input value is too small"""
    pass
class PasswordTooLargeError(Exception):
    """raised when the input value is too large"""
    pass
number=8
while True:
    try:
        i_num=int(input("enter a number:"))
        if i_num < number:
            raise PasswordTooSmallError
        elif i_num > number:
            raise PasswordTooLargeError
        break
    except PasswordTooSmallError:
        print("this value is too small,try again!")
        print()
    except PasswordTooLargeError:
        print("this value is too large,try again!")
        print()
print("Congratulations! you guessed it correctly.")
