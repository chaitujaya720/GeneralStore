import sqlite3
from flask import Flask
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Location, Department, Category, SubCategory


app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_db_session():
    engine = create_engine(f"sqlite:///database.db")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


@app.route('/')
def store_summary():
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


@app.route('/api/v1/location')
def locations():
    locations = []
    status_code = 200
    session = get_db_session()
    try:
        location_obj = session.query(Location)
        locations = [object_as_dict(location) for location in location_obj]
        if not locations:
            status_code = 204
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
        return locations, status_code


@app.route('/api/v1/department')
def departments():
    departments = []
    status_code = 200
    session = get_db_session()
    try:
        department_obj = session.query(Department)
        departments = [object_as_dict(department) for department in department_obj]
        if not departments:
            status_code = 204
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
        return departments, status_code


@app.route('/api/v1/category')
def categories():
    categories = []
    status_code = 200
    session = get_db_session()
    try:
        category_obj = session.query(Category)
        categories = [object_as_dict(category) for category in category_obj]
        if not categories:
            status_code = 204
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
        return categories, status_code

@app.route('/api/v1/sub_category')
def sub_categories():
    sub_categories = []
    status_code = 200
    session = get_db_session()
    try:
        sub_obj = session.query(SubCategory)
        sub_categories = [object_as_dict(sub) for sub in sub_obj]
        if not sub_categories:
            status_code = 204
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
        return sub_categories, status_code


@app.route('/api/v1/location/<int:location_id>/department')
def departments_by_location(location_id):
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


@app.route('/api/v1/location/<int:location_id>/department/<int:department_id>/category')
def categories_by_department_per_location(location_id, department_id):
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