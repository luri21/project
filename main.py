

class Ilur:
    def init(self, name, list, ):
        self.name = name
        self.list = list
    def average(self):
        print(f"Averege: {sum(self.list) / len(self.list)}")

s1 = Ilur("ilur", [9, 12, 10, 8 ,5 , 10 , 4 , 7])
s1.average()