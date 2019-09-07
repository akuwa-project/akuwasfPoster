from flask import Flask,request
from flask_restplus import Resource, Api
from parameters_descriptor import poster_fileds
import logging
import akwadb.poster as poster
import uuid as uuid

app = Flask(__name__)                  #  Create a Flask WSGI application
api = Api(app)                         #  Create a Flask-RESTPlus API
log = logging.getLogger(__name__)

ns = api.namespace('akuwa/poster', description='Operations related to save , delete, update poster and created relationship')
@ns.route('/')
class Posts(Resource):

    @api.expect(poster_fileds)
    @api.response(201, 'Post successfully created.')
    def post(self):
        """
        Create a post.
        """
        b = poster.Poster()
        node_id = str(uuid.uuid4())
        b.addNoed_Poste(node_id,request.json['titre'],request.json['photo'],request.json['montant'],
                        request.json['date'],request.json['adresse'],request.json['commentaire'],
                        request.json['etatPoste'],request.json['information'],request.json['typeAnnonce'])
        b.add_relation_poste_user(request.json['user_name'], node_id)
        return node_id,201


    @ns.route('/<string:user_name>')
    @api.response(404, 'Category not found.')
    class getPosts(Resource):
        def get(self,user_name):
            """
            get all Post of E_user
            """
            b = poster.Poster()
            return b.getAllPostOfEuser(user_name),201

    @ns.route('/<string:annonce_id>/<string:etatPoste>')
    @api.response(404, 'Category not found.')
    class updatePosts(Resource):
        def put(self,annonce_id,etatPoste):
            """
            Update a post by user_name
            """
            b = poster.Poster()
            return b.updatePoste(annonce_id,etatPoste),201

    @ns.route('/<string:annonce_id>')
    @api.response(404, 'Category not found.')
    class deletePosts(Resource):
        def delete(self,annonce_id):
            """
            Update a post by user_name
            """
            b = poster.Poster()
            return b.deletePoste(annonce_id),201