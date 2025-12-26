import random
import string



longueur_mdp = int(input("Quelle longueur souhaitez-vous pour votre mot de passe?"))

alphabet_minuscule = "abcdefghijklmnopqrstuvwxyz"
alphabet_majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
caracteres_speciaux = "&#-_@:!;,."

mdp = []

def selection_majuscule():
    mdp.append(alphabet_majuscule[random.randint(0,25)])

def selection_minuscule():
    mdp.append(alphabet_minuscule[random.randint(0,25)])

def selection_caracteres_speciaux() :
    mdp.append(caracteres_speciaux[random.randint(0,len(caracteres_speciaux)-1)])


for i in range(longueur_mdp):
    choix = random.randint(0,3)
    match choix:
        case 0:
           selection_majuscule()
        case 1:
           selection_minuscule()
        case 2:
           selection_caracteres_speciaux()
        case 3:
           mdp.append(str(random.randint(0,10)))

mot_de_passe = ''.join((mdp))


def evaluation_de_robustesse(mot_de_passe): #calcul le score de robustesse sur la base de la diversité (True ou False) et si le mot de passe contient plus de 8 caractères.
    #calcul de la diversité sur le base des caracètres spéciaux
    presence_minuscule = False
    presence_majuscule = False
    presence_nombre = False
    presence_caracteres_speciaux = False
    longueur_securite = False
    score_robustesse = 0
    diversity = False

    for i in range(len(mot_de_passe)):
        if mot_de_passe[i] in alphabet_minuscule :
            presence_minuscule = True
        elif mot_de_passe[i] in alphabet_majuscule:
            presence_majuscule = True
        elif mot_de_passe[i].isdigit():
            presence_nombre = True
        elif mot_de_passe[i] in caracteres_speciaux:
            presence_caracteres_speciaux = True

    if False not in (presence_majuscule, presence_minuscule, presence_nombre, presence_caracteres_speciaux):
        diversity = True
 

    #vérification que le mot de passe contient au moins 8 caracteres pour le critèrère de longueur
    if len(mot_de_passe) >= 8:
        longueur_securite = True
        
    
    #calcul du score de robustesse :
    if diversity == True and longueur_securite == True :
        score_robustesse = 3
    elif diversity == False or longueur_securite == False :
        score_robustesse = 2
    elif diversity == False and longueur_securite == False:
        score_robustesse = 1
    
    return(score_robustesse)




print(f"voici votre mot de passe : {mot_de_passe}")
print(f"son score de robustesse est de {evaluation_de_robustesse(mot_de_passe)}/3")

input("appuyez sur entrée pour fermer le programme")


