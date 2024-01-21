from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)


class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    location_id = Column(Integer, ForeignKey("location.id"))


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    department_id = Column(Integer, ForeignKey("department.id"))


class SubCategory(Base):
    __tablename__ = "sub_category"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    category_id = Column(Integer, ForeignKey("category.id"))


# # Create the table in the database
# engine = create_engine(f"sqlite:///database.db")
# Base.metadata.create_all(engine)