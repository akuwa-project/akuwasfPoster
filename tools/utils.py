# -*- coding: utf-8 -*-

import uuid


def generateID():
    # Génère un id unique
    return str(uuid.uuid4())


def format_dict(obj):
    # Formate l'objet pour réecrire les objets
    if isinstance(obj, dict):
        obj = {k: None if not v else v for k, v in obj.items()}
        obj = {k: float(v) if isinstance(v, int) else v for k, v in obj.items()}
        obj = {k: format_dict(v) if isinstance(v, dict) else v for k, v in obj.items()}
        obj = {k: [format_dict(elm) for elm in v] if isinstance(v, list) else v for k, v in obj.items()}
        obj = {k: v.strip() if isinstance(v, str) else v for k, v in obj.items()}
    elif isinstance(obj, list):
        obj = [format_dict(elm) for elm in obj]
    else:
        return obj
    return obj
