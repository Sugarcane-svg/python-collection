class WhenYouTurnHundred:

    def __init__(self, name= '', age = 0) -> None:
        
        self.name = name
        self.age = age

    def cal_turn_hundred(self)-> int:
        from datetime import date
        todays_date = date.today()
        return 100 - self.age + int(todays_date.year)

    def print_msg(self):
        return 'hello %s, you will turn 100 in %d year' %(self.name, self.cal_turn_hundred())

test = WhenYouTurnHundred('phoebe', 23)
print(test.print_msg())