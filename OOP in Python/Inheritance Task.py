class Cricketer:
    def __init__(self,name,age,num_matches):
        self.name = name
        self.age = age
        self.num_matches = num_matches
    def get_info(self):
        return f'This is {self.name}, who is {self.age} years old and has played {self.num_matches} matches.'



class BatsMan(Cricketer):

    def __init__(self,name,age,num_matches,num_runs,num_centuries):
        self.num_runs = num_runs
        self.num_centuries = num_centuries
        super().__init__(name,age,num_matches)

    def get_info(self):
        super().get_info()
        print(f'This is {self.name}, who is {self.age} years old and has played {self.num_matches} matches.')
        print ( f'The batsman has made {self.num_runs} runs and {self.num_centuries} centuries over the span of his career.')


class Bowler(Cricketer):
    def __init__(self,name,age,num_matches,num_wickets):
        self.num_wickets =num_wickets
        super().__init__(name, age, num_matches)

    def get_info(self):
        super().get_info()
        print(f'This is {self.name}, who is {self.age} years old and has played {self.num_matches} matches.')
        print(f'The bowler has taken out{self.num_wickets} wickets over the span of his career.')



p1 = BatsMan('Nobel',21,113,720,4)
p2 = Bowler('Gabriel',22,110,67)

p1.get_info()
p2.get_info()
