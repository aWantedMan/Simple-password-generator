import random
import string



def random_generation(longueur_mdp):




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
  return(mot_de_passe)