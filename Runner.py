from LOsztaly import LOsztaly

c=LOsztaly()


c.list_week("202510")
c.getNumber("123")
c.numberOfPlayers("202510")
print("kihuz")
c.lottaryDrawn("202510", [10,20,30,35,45])

c.number_of_winners("202510", 2)
c.number_of_winners("202510", 3)

c.winners("202510", 2)
c.winners("202510", 3)
