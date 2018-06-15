# singes = ['pierre', 'marie']
#
# for singe in singes:
#     if singe == 'pierre':
#         print('banane jaune')
#     else:
#         print('banane verte')


class singe:
    def __init__(self,prenom):
        self.prenom = prenom

    def returnBanane(self):
        if self.prenom == 'pierre':
            banane = 'banane jaune'
        else:
            banane = 'banane verte'
        return banane

singes = ['pierre', 'marie']

for unSinge in singes:
    leSinge = singe(unSinge)
    print(leSinge.returnBanane())
