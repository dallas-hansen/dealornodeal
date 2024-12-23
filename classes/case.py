class Case:
    def __init__(self, case_number, prize):
        self.case_number = case_number
        self.prize = prize
        self.opened = False
    
    def open(self):
        self.opened = True
        return self.prize