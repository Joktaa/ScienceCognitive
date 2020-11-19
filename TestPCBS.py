""" 
 
The experiment is driven by the file `trials1.csv`  with one row per trial and two columns: `Sound` and `Image`.

"""
 
from os.path import join
import expyriment
from random import randint
import matplotlib.pyplot as plt

def analyse(tab):
    plt.bar([0, 1], [nombreVrai(tab), len(tab) - nombreVrai(tab)], tick_label=["Vrai", "Faux"])
    plt.show()

def nombreVrai(tab):
    res = 0
    for case in tab:
        if case[1] == "Vrai":
            res += 1
    return res

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

 
# TABLEAU STOCKANT LES CHEMINS DES IMAGES ET DES SONS
tableau = [['sounds\\ELLE_OÙ_COUCHE.wav', 'pictures\\couche.jpg', 'pictures\\main.jpg', 1], ['sounds\\ELLE_OÙ_COUCHE.wav', 'pictures\\couche.jpg', 'pictures\\main.jpg', 1], ['sounds\\ELLE_OÙ_VOITURE.wav', 'pictures\\voiture.jpg', 'pictures\\balle.jpg', 1], ['sounds\\ELLE_OÙ_VOITURE.wav', 'pictures\\voiture.jpg', 'pictures\\balle.jpg', 1], ['sounds\\IL_OÙ_BIBERON.wav', 'pictures\\biberon.jpg', 'pictures\\livre.jpg', 1], ['sounds\\IL_OÙ_BIBERON.wav', 'pictures\\biberon.jpg', 'pictures\\livre.jpg', 1], ['sounds\\IL_OÙ_NEZ.wav', 'pictures\\nez.jpg', 'pictures\\pied.jpg', 1], ['sounds\\IL_OÙ_NEZ.wav', 'pictures\\nez.jpg', 'pictures\\pied.jpg', 1], ['sounds\\ELLE_OÙ_MAIN.wav', 'pictures\\couche.jpg', 'pictures\\main.jpg', 2], ['sounds\\ELLE_OÙ_MAIN.wav', 'pictures\\couche.jpg', 'pictures\\main.jpg', 2], ['sounds\\IL_OÙ_BALLON.wav', 'pictures\\voiture.jpg', 'pictures\\balle.jpg', 2], ['sounds\\IL_OÙ_BALLON.wav', 'pictures\\voiture.jpg', 'pictures\\balle.jpg', 2], ['sounds\\IL_OÙ_LIVRE.wav', 'pictures\\biberon.jpg', 'pictures\\livre.jpg', 2], ['sounds\\IL_OÙ_LIVRE.wav', 'pictures\\biberon.jpg', 'pictures\\livre.jpg', 2], ['sounds\\IL_OÙ_PIED.wav', 'pictures\\nez.jpg', 'pictures\\pied.jpg', 2], ['sounds\\IL_OÙ_PIED.wav', 'pictures\\nez.jpg', 'pictures\\pied.jpg', 2]]

exp = expyriment.design.Experiment(name="sentence picture matching task")  # create an Experiment object
expyriment.control.set_develop_mode(on=True)  ## Set develop mode. Comment for real experiment
 
expyriment.control.initialize(exp)
 
mouse = expyriment.io.Mouse(show_cursor=True)
screen = exp.screen
window_size = screen.window_size
screen_size = window_size
center_x = exp.screen.center_x
center_y = exp.screen.center_y
 
 
fixcross = expyriment.stimuli.FixCross(size=(25, 25),
                                 line_width=3,
                                 colour=expyriment.misc.constants.C_WHITE)
 
exp.add_data_variable_names(['sound', 'picture1', 'picture2', 'result', 'rt'])
 
expyriment.control.start()
fixcross.present()  # clear screen, presenting fixation cross


vraiOuFaux = ""
tabData = [["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0], ["", "", 0]]
apparu = []
i = 0
while i < 16:
    ok = False
    while ok == False:
        nbr_aleatoire = randint(0, 15)
        for _, value in enumerate(apparu):
            if nbr_aleatoire == value :
                break
        else : 
            ok = True
 
    apparu.append(nbr_aleatoire)
    sound = expyriment.stimuli.Audio(tableau[nbr_aleatoire][0])
    image1 = expyriment.stimuli.Picture(tableau[nbr_aleatoire][1], position = (-200, 0))
    image2 = expyriment.stimuli.Picture(tableau[nbr_aleatoire][2], position = (200, 0))
    BB = expyriment.io.TouchScreenButtonBox([image1, image2])
    BB.create()
    BB.show()
 
    sound.present()
 
    response, rt = BB.wait(duration = 8000)


    courtSound = tableau[nbr_aleatoire][0][7:]
    courtImage1 = tableau[nbr_aleatoire][1][9:]
    courtImage2 = tableau[nbr_aleatoire][2][9:]

    if response == image1 and tableau[nbr_aleatoire][3] == 1:
        vraiOuFaux = "Vrai"
    elif response == image2 and tableau[nbr_aleatoire][3] == 2:
        vraiOuFaux = "Vrai"
    else :
        vraiOuFaux = "Faux"
    print(vraiOuFaux)

    exp.data.add([courtSound,
                courtImage1,
                courtImage2,
                vraiOuFaux,
				 rt])
 
    tabData[i][0] = courtSound
    tabData[i][1] = vraiOuFaux
    tabData[i][2] = rt
 
    fixcross.present()
    exp.clock.wait(1000)
    i += 1

 
expyriment.control.end(goodbye_text= 'Thanks for taking part to this experiment, see you soon')

analyse(tabData)
analyseTemps(tabData)