class GamePerson(object):
    def __init__(self,_hp):
        self.hp=_hp
s1=GamePerson(100)
print(s1.hp)
GamePerson.name="残月"
print(s1.name)