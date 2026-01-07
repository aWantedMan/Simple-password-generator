import random_password_generation
import robustness_evaluator
#v0.3

choix = input("Bienvenue dans simple_password_generator v0.3. Quelle action souhaitez-vous effectuer ? \nCommandes: \n'generation' : génère un mot de passe de longueur de votre choix \n'estimation' : estime la robustesse de votre mot de passe \n'bye': ferme le programme\n")


def _estimation():
    mot_de_passe = input("saissisez le mot de passe que vous souhaitez estimer\n")
    print(f"le niveau de robustesse de votre de mot de passe est de {robustness_evaluator.evaluation_de_robustesse(mot_de_passe)}/3")
    
def _generation():
    longueur_mdp = int(input("Quelle longueur souhaitez vous pour votre mot de passe\n"))
    mot_de_passe = random_password_generation.random_generation(longueur_mdp)
    print(f"votre mot de passe est le suivant : {mot_de_passe}, sa robustesse est de {robustness_evaluator.evaluation_de_robustesse(mot_de_passe)}/3")
    
            
while choix != 'bye':
    match choix :
        case 'estimation':
            _estimation()
            choix = input("quelle action souhaitez vous effetuer?\n")
        case 'generation':
            _generation()
        case _ :
            choix = input("Mauvaise saisie. Veuillez réessayer.\n")
