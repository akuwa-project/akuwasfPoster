from flask_restplus import fields
from restful import api



e_user_fileds = api.model('E_User', {
    "name": fields.String(required=True, description='nom'),
    "prenom": fields.String(required=True, description='prenom'),
    "mail": fields.String(required=True, description='mail'),
    "tel": fields.String(required=True, description='tel'),
    "user_name": fields.String(required=True, description='user_name'),
    "categorie": fields.String(required=True, description='categorie')

})


poster_fileds = api.model('Poster', {
"user_name": fields.String(required=True, description='nom'),
"titre": fields.String(required=True, description='titre'),
"photo": fields.List(fields.String(required=True,description='Information')),
"montant": fields.String(required=True, description='montant'),
"date": fields.String(required=True, description='date'),
"adresse": fields.String(required=True, description='adresse'),
"commentaire": fields.String(required=True, description='commentaire'),
"etatPoste": fields.String(required=True, description='etatPoste'),
"information": fields.List(fields.String(required=True,description='Information')),
"typeAnnonce": fields.String(required=True, description='typeAnnonce')
})
