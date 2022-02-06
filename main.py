
import json

from Consultation import consultation
from Patient import Patient

'''class maladieCardiaque(object):
    nom = "" ;
    description = {
        'symp1': "Mal de tête",
        'symp2': "Vertiges",
        'symp3': "Essoufflement",
        'symp4': "Douleurs thoraciques"
    }

    def __int__(self, nomMaladie, description):
        self.nom = nomMaladie;
        self.description = description;

class Patient(maladieCardiaque):
    def __init__(self, nomPatient, prenom, sexe, age,maladie):
        self.nom = nomPatient;
        self.prenom = prenom;
        self.sexe = sexe;
        self.age = age
        self.maladie = maladie


class avc(maladieCardiaque):
    def __init__(self, nomMaladie, description):
        maladieCardiaque.__init__(nomMaladie, description)

class consultation(maladieCardiaque):
    def __init__(self, dateConsultation, resultat):
        self.dateCons = dateConsultation;
        self.resultat = resultat;'''

'''class AVC(maladieCardiaque):
    def __init__(self, nomMaladie):
        maladieCardiaque.__init__(nomMaladie)

test = AVC("AVC")

print(test.SyptomeGeneral)
'''


cons1 = consultation("Ablo", "Celine", "F", 45, {"0":"Essoufflement", "1": "Vertiges", "2": "Mal de tête", "3": "saignements de nez" })
cons2 = consultation("Saga", "Blaise", "M", 85, {"0":"Essoufflement", "1": "Vertiges", "2": "Mal de tête", "3": "Fatique", "4": "Vomissement"})
cons3 = consultation("Amah", "Jack", "M", 63 ,  {"0":"Mal de tête","1":"Toux avec expectoration rose clair", "2":"Dyspnée nocturne paroxystique"})

print(cons1.Analyse())
print(cons1.symptome.values())

print(cons2.Analyse())
print(cons2.symptome.values())

print(cons3.Analyse())
print(cons3.symptome.values())



list_cons = []

list_cons.append(cons1.resultat())
list_cons.append(cons2.resultat())
list_cons.append(cons3.resultat())


print((list_cons))


'''dic = {"Patient":list_cons}
print(dic)
'''

with open('Consultation.json', 'a', encoding='utf-8') as f:
    json.dump(list_cons, f)

#, indent=4, default=serialiseur_patient

