from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)

# Creating api object using flask-restx
api = Api(app, version='1.0', title='GeneralStore API',
    description='GeneralStore Endpoints',
)

# Creating api models
location_api_model = api.model('Location', {
    'name': fields.String(required=True, description='Name of the location'),
    'description': fields.String(description='Location Description')
})

department_api_model = api.model('Department', {
    'name': fields.String(required=True, description='Name of the Department'),
    'location_id': fields.Integer(required=True, description='Location ID of the department'),
    'description': fields.String(description='Department Description')
})

category_api_model = api.model('Category', {
    'name': fields.String(required=True, description='Name of the location'),
    'department_id': fields.Integer(required=True, description='Deparment ID of the category'),
    'description': fields.String(description='Category Description')
})

sub_category_api_model = api.model('SubCategory', {
    'name': fields.String(required=True, description='Name of the location'),
    'category_id': fields.Integer(required=True, description='Category ID'),
    'description': fields.String(description='Sub Category Description')
})

