import matplotlib.pyplot as plt

def analyseTemps(tab):
    couche = moyenne(tab, 'ELLE_OÙ_COUCHE.wav')
    main = moyenne(tab, 'ELLE_OÙ_MAIN.wav')
    voiture = moyenne(tab, 'ELLE_OÙ_VOITURE.wav')
    ballon = moyenne(tab, 'IL_OÙ_BALLON.wav')
    biberon = moyenne(tab, 'IL_OÙ_BIBERON.wav')
    livre = moyenne(tab, 'IL_OÙ_LIVRE.wav')
    nez = moyenne(tab, 'IL_OÙ_NEZ.wav')
    pied = moyenne(tab, 'IL_OÙ_PIED.wav')

    plt.bar([0, 1, 2, 3, 4, 5, 6, 7], [couche, main, voiture, ballon, biberon, livre, nez, pied], tick_label=["Couche", "Main", "Voiture", "Ballon", "Biberon", "Livre", "Nez", "Pied"])
    plt.show()

def moyenne(tab, chaine):
    a = 0
    b = 0
    long = 1

    for case in tab:
        if case[0] == chaine and a == 0:
            a = case[2]
        elif case[0] == chaine and a != 0:
            b = case[2]
            long = 2

    return (a+b)/long





tab = [['IL_OÙ_PIED.wav', '', 268], ['IL_OÙ_BIBERON.wav', 'Vrai', 896], ['ELLE_OÙ_MAIN.wav', 'Vrai', 877]]

analyseTemps(tab)