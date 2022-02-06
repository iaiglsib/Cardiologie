'''import copy
from main import Patient
from main import consultation

def serialiseur_patient(obj):
    if isinstance(obj, consultation):
        obj_cpy = copy.copy(obj)
        obj_cpy.__class__ = Patient
        return {
            "__class__": "main",
            "Diagnostic": obj.dico,
            "__parent__": obj_cpy}

    if isinstance(obj, Patient):
        return {"__class__": "Patient",
                "Nom": obj.nomPatient,
                "Prenom": obj.prenom,
                "Age": obj.age,
                "Sexe": obj.sexe
                }'''