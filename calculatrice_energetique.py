#!/usr/bin/python3

import time

# Determination metabolisme base par équation
#Calcul metabolisme basal homme kcal
# 66,5 + (13.75 x poids en kg) + (5 x taille en cm) - (6.77 x age)
def homme():
    poids = input("Veuillez saisir votre poids en kg: ")
    taille = input("Veuillez saisir votre taille en cm: ")
    age = input("Veuillez saisir votre age: ")
    metabolismebase = 66.5 + (13.75 * int(poids)) + (5 * int(taille)) - (6.77 * int(age))
    print(f"Votre métabolisme de base en kcal est de: {metabolismebase}")

# Détermination de dépense énergétique totale
    print(
        """
        Quel est votre niveau d'activité journalier:
        1 - Journée passée au repos
        2 - Travail sédentaire assis, pas de sport, moins de 30 min de marche
        3 - Travail sédentaire avec 30min de marche
        4 - Travail sédentaire et 1h à 1h15 de sport
        5 - Travail sédentaire et 1h30 à 2h de sport
        6 - Travail physique avec beaucoup de déplacements et 1h30 à 2h de sport
        7 - Travail physique et 3 à 4h de sport
        """
    )
    activite = input("Veuillez sélectionnez votre niveau d'activité: ")
# metabolisme de base x coefficent d'activité
    if activite == "1":
        coeffactivite = metabolismebase * 1
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    elif activite == "2":
        coeffactivite = metabolismebase * 1.2
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    elif activite == "3":
        coeffactivite = metabolismebase * 1.4
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    elif activite == "4":
        coeffactivite = metabolismebase * 1.6
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    elif activite == "5":
        coeffactivite = metabolismebase * 1.7
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    elif activite == "6":
        coeffactivite = metabolismebase * 1.8
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    elif activite == "7":
        coeffactivite = metabolismebase * 2
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    else:
        print("Demande incomprise fermeture du programme...")
        time.sleep(5)
        exit(0)

#calcul metabolisme basal femme en kcal
# 655,1 + (9.56 x poids en kg) + (1.85 x taille en cm) - (4.67 x age)
def femme():
    poids = input("Veuillez saisir votre poids en kg: ")
    taille = input("Veuillez saisir votre taille en cm: ")
    age = input("Veuillez saisir votre age: ")
    metabolismebase = 655.1 + (9.56 * int(poids)) + (1.85 * int(taille)) - (4.67 * int(age))
    print(f"Votre métabolisme de base en kcal est de: {metabolismebase}")
    print(
        """
        Quel est votre niveau d'activité journalier:
        1 - Journée passée au repos
        2 - Travail sédentaire assis, pas de sport, moins de 30 min de marche
        3 - Travail sédentaire avec 30min de marche
        4 - Travail sédentaire et 1h à 1h15 de sport
        5 - Travail sédentaire et 1h30 à 2h de sport
        6 - Travail physique avec beaucoup de déplacements et 1h30 à 2h de sport
        7 - Travail physique et 3 à 4h de sport
        """
    )
    activite = input("Veuillez sélectionnez votre niveau d'activité: ")
    if activite == "1":
        coeffactivite = metabolismebase * 1
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    elif activite == "2":
        coeffactivite = metabolismebase * 1.2
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    elif activite == "3":
        coeffactivite = metabolismebase * 1.4
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    elif activite == "4":
        coeffactivite = metabolismebase * 1.6
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    elif activite == "5":
        coeffactivite = metabolismebase * 1.7
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    elif activite == "6":
        coeffactivite = metabolismebase * 1.8
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    elif activite == "7":
        coeffactivite = metabolismebase * 2
        print(f"Votre dépense journalière est de: {coeffactivite}")
        time.sleep(5)
        remarque()
    else:
        print("Demande incomprise fermeture du programme...")
        time.sleep(5)
        exit(0)

def remarque():
    print(
        """
        Remarque:
        On pourra ajuster ce résultat de:
        + 10 % pour des personnes ayant un métabolisme qui brûle beaucoup naturellement (profil plutôt maigre et sec)
        - 10 % pour des personnes ayant un métabolisme plus qui ont tendance à prendre du poids facilement
        \n
        Bilan énergétique:
        - Si la dépense excède les apports, il y a perte de poids
        - Si les apports excédent la dépense, il y a prise de poids
        """
    )
    time.sleep(30)

def main():
    print(
        """
        Pour quel sexe voulez calculer la dépense énergétique ?
        > 1: Homme <
        > 2: Femme <
        > q: Quitter <
        """
    )
    choix = input("Veuillez sélectionnez une option: ")
    if choix == "1":
        homme()
    elif choix == "2":
        femme()
    elif choix == "q":
        print("fermeture programme")
        exit(0)
    else:
        print("veuillez sélectionner une option présente dans la liste")
        main()

main()