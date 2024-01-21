import sqlite3
from flask import Flask
from flask_restx import Api, Resource, fields
from flask_basicauth import BasicAuth
from models import Location, Department, Category, SubCategory
from models_dao import get_db_session, object_as_dict
from models_dao import LocationDao, DepartmentDao, CategoryDao, SubCategoryDao

# Initiating Flask Object
app = Flask(__name__)

# Configuring auth porams, username and password
app.config['BASIC_AUTH_USERNAME'] = 'chaitujaya720@gmail.com'
app.config['BASIC_AUTH_PASSWORD'] = 'test@123'

basic_auth = BasicAuth(app) #Initiating Basic Auth

# Creating api object using flask-restx
api = Api(app, version='1.0', title='GeneralStore API',
    description='GeneralStore Endpoints',
)

# Creating api models
location = api.model('Location', {
    'name': fields.String(required=True, description='Name of the location'),
    'description': fields.String(description='Location Description')
})

department = api.model('Department', {
    'name': fields.String(required=True, description='Name of the Department'),
    'location_id': fields.Integer(required=True, description='Location ID of the department'),
    'description': fields.String(description='Department Description')
})

category = api.model('Category', {
    'name': fields.String(required=True, description='Name of the location'),
    'department_id': fields.Integer(required=True, description='Deparment ID of the category'),
    'description': fields.String(description='Category Description')
})

sub_category = api.model('SubCategory', {
    'name': fields.String(required=True, description='Name of the location'),
    'category_id': fields.Integer(required=True, description='Category ID'),
    'description': fields.String(description='Sub Category Description')
})


# Initiating DAO Objects
location = LocationDao()
department = DepartmentDao()
category = CategoryDao()
sub_category = SubCategoryDao()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@api.route('/api/v1/summary')
class StoreSummary(Resource):
    @basic_auth.required
    def get(self):
        objects = []
        status_code = 200
        session = get_db_session()
        try:
            store_obj = session.query(Location.name.label('Location'),
                                      Department.name.label('Departmment'),
                                      Category.name.label('Category'),
                                      SubCategory.name.label('SubCategory')
                                     ).join(Category, SubCategory.category_id.__eq__(Category.id)\
                                           ).join(Department, Category.department_id.__eq__(Department.id)
                                                  ).join(Location, Department.location_id.__eq__(Location.id))

            objects = [entry._asdict() for entry in store_obj.all()]
            if not objects:
                status_code = 204
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            return objects, status_code


@api.route('/api/v1/location')
class LocationAPI(Resource):
    @basic_auth.required
    def get(self):
        locations = []
        status_code = 200
        try:
            locations = location.get()
            if not locations:
                status_code = 204
        except Exception as e:
            raise e
        finally:
            return locations, status_code

    @basic_auth.required
    @api.expect(location)
    def post(self):
        test = api.payload
        import ipdb
        ipdb.set_trace()

@api.route('/api/v1/department')
class DepartmentAPI(Resource):
    @basic_auth.required
    def get(self):
        departments = []
        status_code = 200
        try:
            departments = department.get()
            if not departments:
                status_code = 204
        except Exception as e:
            raise e
        finally:
            return departments, status_code


@api.route('/api/v1/category')
class CategoryAPI(Resource):
    @basic_auth.required
    def get(self):
        categories = []
        status_code = 200
        try:
            categories = category.get()
            if not categories:
                status_code = 204
        except Exception as e:
            raise e
        finally:
            return categories, status_code


@api.route('/api/v1/sub_category')
class SubCategoryAPI(Resource):
    @basic_auth.required
    def get(self):
        sub_categories = []
        status_code = 200
        try:
            sub_categories = sub_category.get()
            if not sub_categories:
                status_code = 204
        except Exception as e:
            raise e
        finally:
            return sub_categories, status_code


@api.route('/api/v1/location/<int:location_id>/department')
class DeparmentsByLocation(Resource):
    @basic_auth.required
    def get(self, location_id):
        departments = []
        status_code = 200
        session = get_db_session()
        try:
            department_obj = session.query(Department).filter(Department.location_id.__eq__(location_id))
            departments = [object_as_dict(department) for department in department_obj]
            if not departments:
                status_code = 204
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            return departments, status_code


@api.route('/api/v1/location/<int:location_id>/department/<int:department_id>/category')
class CategoriesByDepartmentPerLocation(Resource):
    @basic_auth.required
    def get(self, location_id, department_id):
        categories = []
        status_code = 200
        session = get_db_session()
        try:
            category_obj = session.query(Category
                                         ).filter(Category.department_id.__eq__(department_id),
                                                  Department.location_id.__eq__(location_id))

            categories = [object_as_dict(category) for category in category_obj]
            if not categories:
                status_code = 204
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            return categories, status_code


if __name__ == '__main__':
    app.run(debug=True)