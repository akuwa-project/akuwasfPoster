import logging

from flask_restplus import Api

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Akuwa Immobilier manger',
          description='Akuwa manger of a Flask RestPlus powered API',contact_email="contact@akuwa.com")


