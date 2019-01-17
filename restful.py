import logging

from flask_restplus import Api

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Audit manger',
          description='A audit manger of a Flask RestPlus powered API',contact_email="contact@rintio.com")


