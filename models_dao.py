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
    def get(self, location_id=None):
        locations = []
        session = get_db_session()
        try:
            if location_id:
                location_obj = session.query(Location).filter(Location.id.__eq__(location_id))
            else:
                location_obj = session.query(Location)
            locations = [object_as_dict(location) for location in location_obj]
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            return locations

    def create(self, data):
        session = get_db_session()
        try:
            location_obj = Location(name=data['name'], description=data['description'])
            session.add(location_obj)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update(self, location_id, data):
        session = get_db_session()
        try:
            location_obj = session.query(Location).filter(Location.id.__eq__(location_id))
            location_obj.update(data)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete(self, location_id):
        session = get_db_session()
        try:
            location_obj = session.query(Location).filter(Location.id.__eq__(location_id))
            location_obj.delete()
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

class DepartmentDao:
    def get(self, department_id=None):
        departments = []
        session = get_db_session()
        try:
            if department_id:
                department_obj = session.query(Department).filter(Department.id.__eq__(department_id))
            else:
                department_obj = session.query(Department)
            departments = [object_as_dict(department) for department in department_obj]
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            return departments

    def create(self, data):
        session = get_db_session()
        try:
            department_obj = Department(name=data['name'],
                                        location_id=data['location_id'],
                                        description=data['description'])
            session.add(department_obj)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update(self, department_id, data):
        session = get_db_session()
        try:
            department_obj = session.query(Department).filter(Department.id.__eq__(department_id))
            department_obj.update(data)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete(self, department_id):
        session = get_db_session()
        try:
            department_obj = session.query(Department).filter(Department.id.__eq__(department_id))
            department_obj.delete()
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

class CategoryDao:
    def get(self, category_id=None):
        categories = []
        session = get_db_session()
        try:
            if category_id:
                category_obj = session.query(Category).filter(Category.id.__eq__(category_id))
            else:
                category_obj = session.query(Category)
            categories = [object_as_dict(category) for category in category_obj]
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            return categories

    def create(self, data):
        session = get_db_session()
        try:
            category_obj = Category(name=data['name'],
                                    department_id=data['department_id'],
                                    description=data['description'])
            session.add(category_obj)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update(self, category_id, data):
        session = get_db_session()
        try:
            category_obj = session.query(Category).filter(Category.id.__eq__(category_id))
            category_obj.update(data)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete(self, category_id):
        session = get_db_session()
        try:
            category_obj = session.query(Category).filter(Category.id.__eq__(category_id))
            category_obj.delete()
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

class SubCategoryDao:
    def get(self, sub_category_id=None):
        sub_categories = []
        session = get_db_session()
        try:
            if sub_category_id:
                sub_obj = session.query(SubCategory).filter(SubCategory.id.__eq__(sub_category_id))
            else:
                sub_obj = session.query(SubCategory)
            sub_categories = [object_as_dict(sub) for sub in sub_obj]
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            return sub_categories

    def create(self, data):
        session = get_db_session()
        try:
            sub_category_obj = SubCategory(name=data['name'],
                                           category_id=data['category_id'],
                                           description=data['description'])
            session.add(sub_category_obj)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update(self, sub_category_id, data):
        session = get_db_session()
        try:
            sub_obj = session.query(SubCategory).filter(SubCategory.id.__eq__(sub_category_id))
            sub_obj.update(data)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete(self, sub_category_id):
        session = get_db_session()
        try:
            sub_obj = session.query(SubCategory).filter(SubCategory.id.__eq__(sub_category_id))
            sub_obj.delete()
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()