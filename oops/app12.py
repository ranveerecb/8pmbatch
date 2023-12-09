class Rbi:
    def timings(self):
        print('Open@10am & Close@4pm')
    def holidayslist(self):
        print('weekly 5 day+All Govt+1 month vac')
    def rateofinterest(self):
        print('Rbi decides roi is : 18%')
class Sbi(Rbi):
    def rateofinterest(self):
        print('Sbi decides roi is : 10%')

class Hdfc(Rbi):
    def rateofinterest(self):
        print(' Hdfc decides roi is : 8%')

class Icici(Rbi):
    def rateofinterest(self):
        print('Icici decides roi is : 6%')

bank1,bank2,bank3=Sbi(),Hdfc(),Icici()
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
bank1.timings()
bank1.holidayslist()
bank1.rateofinterest()
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
bank2.timings()
bank2.holidayslist()
bank2.rateofinterest()
print('#############################################')
bank3.timings()
bank3.holidayslist()
bank3.rateofinterest()
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')