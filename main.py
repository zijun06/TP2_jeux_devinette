"""
NOM: zijun zhou
Group:406
L’ordinateur choisi au hasard (librairie random à importer) un nombre aléatoire entre 0 et 1000.
L’ordinateur demande à l’usager d’entrer un nombre de 0 à 1000 de façon à trouver celui qu’il a choisi."""
import random


def essai_joueur():
    global joueur_essai
    global nb_essai

    joueur_essai = int(input("Entrez votre essai :_"))
    nb_essai += 1


def nb_hasard():
    nb_assard = random.randint(borne_minimale, borne_maximale)
    return nb_assard


t = True

while t:

    borne_minimale = int(input("entrer le borne_minimale que vous voulez:_"))
    borne_maximale = int(input("entrer le borne_maximale que vous voulez_"))
    nb_essai = 0
    nb_hasard()
    nb_hasard = nb_hasard()

    print("J’ai cree un nombre au hasard entre borne_minimale et borne_maximale. À vous de le deviner...")

    essai_joueur()

    if joueur_essai > nb_hasard:
        print("Mauvais choix, le nombre est plus petit que", joueur_essai)
        essai_joueur()

    if joueur_essai < nb_hasard:
        print("Mauvaise réponse, le nombre est plus grand que", joueur_essai)
        essai_joueur()

    if joueur_essai == nb_hasard:
        print("Bravo! Bonne réponse")
        print("Vous avez réussi en :", nb_essai, "essai(s).")

        nouvelle_partie = str(input("Voulez-vous faire une autre partie (o/n)? _"))
        if nouvelle_partie == "o":
            t = True
        if nouvelle_partie == "n":
            t = False
            print("Merci et au revoir…")
