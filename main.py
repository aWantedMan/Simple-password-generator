import random
import string
import random_password_generation
import robustness_evaluator


choix = (input("saissisez votre choix : génération de mot de passe(1)/estimation du niveau de sécurité de votre mot de passe(2): "))

while choix not in ('1','2'):
    choix = input("mauvaise saisie. 1 pour la génération de mot de passe, 2 pour l'estimation de la sécurité. Veuillez réessayer: ")


if choix == '1' :
    longueur_mdp = int(input("Quelle longueur souhaitez-vous pour votre mot de passe? "))
    mot_de_passe = random_password_generation.random_generation(longueur_mdp)

    print(f"voici votre mot de passe : {mot_de_passe}")
    print(f"son score de robustesse est de {robustness_evaluator.evaluation_de_robustesse(mot_de_passe)}/3")

elif choix == '2':
    mot_de_passe = input("saississez votre mot de passe actuel: ")
    print(f"son score de robustess est de {robustness_evaluator.evaluation_de_robustesse(mot_de_passe)}/3")



input("appuyez sur entrée pour fermer le programme")


