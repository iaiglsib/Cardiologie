from Maladie import maladieCardiaque
from Patient import *
from datetime import datetime
import json


class consultation(Patient, maladieCardiaque):
    dico = dict()
    maladie = ""

    def __init__(self,nomPatient, prenom, sexe, age, symptome ={}):
        Patient.__init__(self, nomPatient, prenom, sexe, age)
        self.symptome = symptome;
        self.maladie = "";
        self.dico = self.resultat();
        self.symptome;


    def Analyse(self):
        for item in self.symptome.values():
            if ("saignements de nez" in self.symptome.values()) and (item in maladieCardiaque.SyptomeGeneral):
                    self.maladie = "Hypertension artérielle"
                    return "Hypertension artérielle";
            elif ("Fatigue", "Vomissement" in self.symptome.values()) and (item in maladieCardiaque.SyptomeGeneral):
                    self.maladie = "Affection coronarienne"
                    return "Affection coronarienne";
            elif ("Toux avec expectoration rose clair", "Dyspnée nocturne paroxystique" in self.symptome.values()) and (item in maladieCardiaque.SyptomeGeneral):
                    self.maladie = "Insuffissance cardiaque"
                    return "Insuffissance cardiaque";
            else:
                return "Patient besoin d'une autre analyse";

    def resultat(self):
            dic_res = dict()
            tab = [i for i in self.symptome.values()]
            dic_res["Nom"] = self.nomPatient;
            dic_res["Prenom"] = self.prenom;
            dic_res["Age"] = self.age;
            dic_res["DateConsultation"] = str(datetime.now());
            dic_res["Maladie"] = self.maladie;

            dic_res["Symptomes"] = {k:v for k,v in enumerate(tab)}
            return dic_res

    def enregistreFichierTx(self, data=[]):
        tab = [i for i in self.symptome.values()]
        data.append({
                "Nom": self.nomPatient,
                "Prenom": self.prenom,
                "Age": self.age,
                "Sexe": self.sexe,
                "DateConsultation": str(datetime.now()),
                "Maladie": self.maladie,
                 "Symptomes":{k:v for k,v in enumerate(tab)}
            },);
        with open('EnregistrePatient.txt', 'w') as wf:
            for patient in data:
                wf.write("{} \n ".format(patient));
            wf.close()

    '''def insert(self):
        data =  []
        if (len(data)!=0):
            data['patient'].append({
            "Nom": self.nomPatient,
            "Prenom": self.prenom,
            "Age": self.age,
            "Sexe": self.sexe,
            "DateConsultation":str(datetime.now()),
            "Maladie":self.maladie,
            #"Symptomes":self.symptome.values(),
        });

        with open('Cardio_data.json', 'w') as nf:
            json.dump(data, nf)
            nf.close()
     '''
    def reading(self):
        with open('Cardio_data.json') as nf:
            data = json.load(nf)
            # source = mon_fichier.read()
            # print(json.loads(source))
            print(data)




