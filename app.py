import sqlite3
from flask import request
from flask_restx import Resource
from flask_basicauth import BasicAuth
from api import app, api, location_api_model, department_api_model, category_api_model, sub_category_api_model
from models import Location, Department, Category, SubCategory
from models_dao import get_db_session, object_as_dict
from models_dao import LocationDao, DepartmentDao, CategoryDao, SubCategoryDao


# Configuring auth porams, username and password
app.config['BASIC_AUTH_USERNAME'] = 'chaitujaya720@gmail.com'
app.config['BASIC_AUTH_PASSWORD'] = 'test@123'

basic_auth = BasicAuth(app)  # Initiating Basic Auth


# Initiating DAO Objects
location_dao = LocationDao()
department_dao = DepartmentDao()
category_dao = CategoryDao()
sub_category_dao = SubCategoryDao()


# Method to establish connection for executing raw sql queries
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@api.route('/api/v1/location')
class LocationAPI(Resource):
    @basic_auth.required
    def get(self):
        locations = []
        status_code = 200
        try:
            locations = location_dao.get()
            if not locations:
                status_code = 204
        except Exception as e:
            raise e
        finally:
            return locations, status_code

    @basic_auth.required
    @api.expect(location_api_model)
    def post(self):
        try:
            data = api.payload
            location_dao.create(data)
            return "Location Created", 201
        except Exception as e:
            raise e

@api.route('/api/v1/location/<int:location_id>')
class LocationApiById(Resource):
    @basic_auth.required
    def get(self, location_id):
        try:
            location = location_dao.get(location_id)
            if location:
                return location, 200
            return "Invalid Location ID", 400
        except Exception as e:
            raise e

    @basic_auth.required
    def put(self, location_id):
        try:
            data = request.json
            location = location_dao.get(location_id)
            if location:
                location_dao.update(location_id, data)
                return "Location Updated Successfully", 200
            return "Invalid Location ID", 400
        except Exception as e:
            raise e

    @basic_auth.required
    def delete(self, location_id):
        try:
            location = location_dao.get(location_id)
            if location:
                location_dao.delete(location_id)
                return "Location Deleted Successfully", 200
            return "Invalid Location ID", 400
        except Exception as e:
            raise e


@api.route('/api/v1/department')
class DepartmentAPI(Resource):
    @basic_auth.required
    def get(self):
        departments = []
        status_code = 200
        try:
            departments = department_dao.get()
            if not departments:
                status_code = 204
        except Exception as e:
            raise e
        finally:
            return departments, status_code

    @basic_auth.required
    @api.expect(department_api_model)
    def post(self):
        data = api.payload
        locations = location_dao.get()
        locations = {location['id'] for location in locations}
        if data['location_id'] in locations:
            department_dao.create(data)
            return "Department Created", 201
        return "Invalid Location", 400


@api.route('/api/v1/location/<int:department_id>')
class DepartmentApiById(Resource):
    @basic_auth.required
    def get(self, department_id):
        try:
            department = department_dao.get(department_id)
            if department:
                return department, 200
            return "Invalid Department ID", 400
        except Exception as e:
            raise e

    @basic_auth.required
    def put(self, department_id):
        try:
            data = request.json
            department = department_dao.get(department_id)
            if department:
                department_dao.update(department_id, data)
                return "Department Updated Successfully", 200
            return "Invalid Department ID", 400
        except Exception as e:
            raise e

    @basic_auth.required
    def delete(self, department_id):
        try:
            department = department_dao.get(department_id)
            if department:
                department_dao.delete(department_id)
                return "Department Deleted Successfully", 200
            return "Invalid Department ID", 400
        except Exception as e:
            raise e


@api.route('/api/v1/category')
class CategoryAPI(Resource):
    @basic_auth.required
    def get(self):
        categories = []
        status_code = 200
        try:
            categories = category_dao.get()
            if not categories:
                status_code = 204
        except Exception as e:
            raise e
        finally:
            return categories, status_code

    @basic_auth.required
    @api.expect(category_api_model)
    def post(self):
        data = api.payload
        departments = department_dao.get()
        departments = {department['id'] for department in departments}
        if data['department_id'] in departments:
            category_dao.create(data)
            return "Category Created", 201
        return "Invalid Department", 400


@api.route('/api/v1/location/<int:category_id>')
class CategoryApiById(Resource):
    @basic_auth.required
    def get(self, category_id):
        try:
            category = category_dao.get(category_id)
            if category:
                return category, 200
            return "Invalid Category ID", 400
        except Exception as e:
            raise e

    @basic_auth.required
    def put(self, category_id):
        try:
            data = request.json
            category = category_dao.get(category_id)
            if category:
                category_dao.update(category_id, data)
                return "Category Updated Successfully", 200
            return "Invalid Category ID", 400
        except Exception as e:
            raise e

    @basic_auth.required
    def delete(self, category_id):
        try:
            category = category_dao.get(category_id)
            if category:
                category_dao.delete(category_id)
                return "Category Deleted Successfully", 200
            return "Invalid Category ID", 400
        except Exception as e:
            raise e


@api.route('/api/v1/sub_category')
class SubCategoryAPI(Resource):
    @basic_auth.required
    def get(self):
        sub_categories = []
        status_code = 200
        try:
            sub_categories = sub_category_dao.get()
            if not sub_categories:
                status_code = 204
        except Exception as e:
            raise e
        finally:
            return sub_categories, status_code

    @basic_auth.required
    @api.expect(sub_category_api_model)
    def post(self):
        data = api.payload
        categories = category_dao.get()
        categories = {category['id'] for category in categories}
        if data['category_id'] in categories:
            category_dao.create(data)
            return "Sub Category Created", 201
        return "Invalid Category", 400

@api.route('/api/v1/location/<int:sub_category_id>')
class SubCategoryApiById(Resource):
    @basic_auth.required
    def get(self, sub_category_id):
        try:
            sub_category = sub_category_dao.get(sub_category_id)
            if sub_category:
                return sub_category, 200
            return "Invalid Sub Category ID", 400
        except Exception as e:
            raise e

    @basic_auth.required
    def put(self, sub_category_id):
        try:
            data = request.json
            sub_category = sub_category_dao.get(sub_category_id)
            if sub_category:
                sub_category_dao.update(sub_category_id, data)
                return "Sub Category Updated Successfully", 200
            return "Invalid Sub Category ID", 400
        except Exception as e:
            raise e

    @basic_auth.required
    def delete(self, sub_category_id):
        try:
            sub_category = sub_category_dao.get(sub_category_id)
            if sub_category:
                sub_category_dao.delete(sub_category_id)
                return "Sub Category Deleted Successfully", 200
            return "Invalid Sub Category ID", 400
        except Exception as e:
            raise e
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


if __name__ == '__main__':
    app.run(debug=True)
