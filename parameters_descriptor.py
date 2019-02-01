from flask_restplus import fields
from restful import api

context_post = api.model('Context post', {
    'userIp': fields.String(required=True, description='user ip'),
    'userName': fields.String(required=True, description='user name'),
    'userSurname': fields.String(required=True, description='user surname'),
    'userMail': fields.String(required=True, description='user mail'),
    'userGeoCoord': fields.String(required=True, description='user geo coord'),
    'date': fields.String(required=True, description='date'),
    'methode_uri': fields.String(required=True, description='methode uri'),
    'expeditorId': fields.String(required=True, description='expeditor Id'),
    'expeditorLayer': fields.String(required=True, description='expeditor layer'),
    'destinatorLayer': fields.String(required=True, description='destinator layer'),
    'methode_type': fields.String(required=True, description='methode type'),
})