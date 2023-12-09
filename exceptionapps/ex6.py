class AgeAboveException(Exception):
    def __str__(self):
        return 'Age must be below 100'
class AgeBelowException(Exception):
    def __str__(self):
        return 'Age must be abpve 18'
def check_age():
    age=55
    try:
        if age>100:
            raise AgeAboveException()
        elif age>18:
            print('Valide age for voting')
        else:
            raise AgeBelowException()
    except AgeAboveException as e:
        print(e)
    except AgeBelowException as e:
        print(e)
check_age()

check_age()