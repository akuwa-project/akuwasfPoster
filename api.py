from parameters_descriptor import context_post
import logging
import fonction
from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)                  #  Create a Flask WSGI application
api = Api(app)                         #  Create a Flask-RESTPlus API
log = logging.getLogger(__name__)
ns = api.namespace('audit/', description='Operations related to context mangement')


@ns.route('/audits')
class PostsCollection(Resource):

    @api.expect(context_post)
    @api.response(201, 'Post successfully created.')
    def post(self):
        """
        Create a audit post.
        """
        return fonction.create_context(),201