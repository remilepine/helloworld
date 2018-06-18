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

    def seReproduitAvec(self,singe2,nom_enfant):
        print('Le singe ' + self.prenom + ' se reproduit avec le singe ' + singe2.prenom + ' pour creer ' + nom_enfant)
        enfant = singe(nom_enfant)
        return enfant

singes = ['pierre', 'marie']

for unSinge in singes:
    leSinge = singe(unSinge)
    print(leSinge.returnBanane())

pierre = singe('Pierre')
marie = singe('Marie')
robert = pierre.seReproduitAvec(marie,'Robert')