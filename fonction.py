import tools.log_exception as logger
import json
import uuid
import pymongo
from flask import Flask, abort, request
from enum import Enum
APP = Flask(__name__)

class LAYER(Enum):
    SF = 1
    UC = 2
    CLIENT = 3


class TYPE_METHODE(Enum):
    POST = 1
    PUT = 2
    GET = 3
    DELETE = 4


def connect_to_db(db):
    """
    mongodb database connection
    :param db:
    :return:
    """
    # noinspection PyBroadException
    try:
        """connection au serveur mongodb"""
        parameters_file = "tools/parametres.json"
        with open(parameters_file, 'r') as fich_p:
            parameters = json.loads(fich_p.read())
            mongo_url = parameters['mongodb']['url']
            mongo_client = pymongo.MongoClient(mongo_url)
    except Exception:
        logger.printLog(logger.LOG_ERROR, logger.DUNIYA_EXCEPTION_TYPE.MONGO_CONNECTION_EXCEPTION,
                        "ECHEC DE CONNECTION AU SERVEUR MONGODB")
        logger.printLog(logger.LOG_TYPE.ERROR, logger.DUNIYA_EXCEPTION_TYPE.PARSING_EXCEPTION)
        return None
    """utilisation de la base de donnee 'db' 
    si elle n'existe pas elle sera cree"""
    db = mongo_client[db]
    # retourne la connection a la base de donnee si la connexion au serveur mongodb a ete bien etabli
    #return db
    return mongo_client

def save_ong(audit):
    """
    save ong json object to mongodb server
    :param ong:
    :return:
    """
    parameters_file = "tools/parametres.json"
    with open(parameters_file, 'r') as fich_p:
        parameters = json.loads(fich_p.read())
        mongo_url = parameters['mongodb']['url']
        # mongo_client = pymongo.MongoClient(mongo_url)

    client = pymongo.MongoClient(mongo_url)
    data_base = client['duniya']
    return data_base.audit.save(audit)

    # db = connect_to_db('context')
    # col = db['context']
    # # return col.insert_one(context)
    # return col.save(context)


def create_context():
    if not request.get_json(force=True):
        abort(400)
    context_result = request.get_json(force=True)
    context_to_mongo = {
        "_id":str(uuid.uuid4()),
        "userIp":context_result['userIp'],
        "userName":context_result['userName'],
        "userSurname":context_result['userSurname'],
        "userMail":context_result['userMail'],
        "userGeoCoord": context_result['userGeoCoord'],
        "date":context_result['date'],
        "methode_uri":context_result['methode_uri'],
        "expeditorId":context_result['expeditorId'],
        "expeditorLayer":context_result['expeditorLayer'],
        "destinatorLayer": context_result['destinatorLayer'],
        'methode_type': context_result['methode_type']
    }
    save_ong(context_to_mongo)
    #return json.dumps(context_to_mongo)
    #save_ong(context_to_mongo)
    return context_to_mongo
    #return connect_to_db('context')


