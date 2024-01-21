from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Location, Department, Category, SubCategory


def get_db_session():
    engine = create_engine(f"sqlite:///database.db")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

class LocationDao:
    def get(self):
        locations = []
        session = get_db_session()
        try:
            location_obj = session.query(Location)
            locations = [object_as_dict(location) for location in location_obj]
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            return locations

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class DepartmentDao:
    def get(self):
        departments = []
        session = get_db_session()
        try:
            department_obj = session.query(Department)
            departments = [object_as_dict(department) for department in department_obj]
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            return departments

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class CategoryDao:
    def get(self):
        categories = []
        session = get_db_session()
        try:
            category_obj = session.query(Category)
            categories = [object_as_dict(category) for category in category_obj]
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            return categories

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class SubCategoryDao:
    def get(self):
        sub_categories = []
        session = get_db_session()
        try:
            sub_obj = session.query(SubCategory)
            sub_categories = [object_as_dict(sub) for sub in sub_obj]
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            return sub_categories

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass