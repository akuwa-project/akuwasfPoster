from flask import Flask,request
from flask_restplus import Resource, Api
from parameters_descriptor import e_user_fileds
import logging
import akwadb.e_user as e_user

app = Flask(__name__)                  #  Create a Flask WSGI application
api = Api(app)                         #  Create a Flask-RESTPlus API
log = logging.getLogger(__name__)
ns = api.namespace('akuwa/e_user', description='Operations related to save e_user')


@ns.route('/')
class Posts(Resource):

    @api.expect(e_user_fileds)
    @api.response(201, 'E_User successfully created.')
    def post(self):
        """
        Create a E_User.
        """
        b = e_user.E_user()
        return b.addNoed_User(request.json['name'],request.json['prenom'],request.json['mail'],
        request.json['tel'],request.json['user_name'],request.json['categorie']),201


    @api.response(201, 'E_User successfully.')
    def get(self):
        """
        get all E_user
        """
        b = e_user.E_user()
        return b.getAllEUser(),201