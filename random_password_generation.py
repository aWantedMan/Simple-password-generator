import random
import string
#v0.3


def random_generation(longueur_mdp: int)->str:
  """Public API: generates a random password according to the lenght in parameter"""



  alphabet_minuscule = "abcdefghijklmnopqrstuvwxyz"
  alphabet_majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  caracteres_speciaux = "&#-_@:!;,."

  mdp = []

  def _selection_majuscule():
      mdp.append(alphabet_majuscule[random.randint(0,25)])

  def _selection_minuscule():
      mdp.append(alphabet_minuscule[random.randint(0,25)])

  def _selection_caracteres_speciaux() :
      mdp.append(caracteres_speciaux[random.randint(0,len(caracteres_speciaux)-1)])


  for i in range(longueur_mdp):
      choix = random.randint(0,3)
      match choix:
          case 0:
             _selection_majuscule()
          case 1:
             _selection_minuscule()
          case 2:
             _selection_caracteres_speciaux()
          case 3:
             mdp.append(str(random.randint(0,10)))

  mot_de_passe = ''.join((mdp))
  return(mot_de_passe)