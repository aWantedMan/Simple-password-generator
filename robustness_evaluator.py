import random
import string
#v0.3



def evaluation_de_robustesse(mot_de_passe: str)->int:
    """Public API: return the estimated robustness score"""
    presence_minuscule = False
    presence_majuscule = False
    presence_nombre = False
    presence_caracteres_speciaux = False
    longueur_securite = False
    score_robustesse = 0
    diversity = False
    alphabet_minuscule = "abcdefghijklmnopqrstuvwxyz"
    alphabet_majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caracteres_speciaux = "&#-_@:!;,."

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
    elif diversity == False and longueur_securite == False :
        score_robustesse = 1
    elif diversity == False or longueur_securite == False:
        score_robustesse = 2
    
    return(score_robustesse)