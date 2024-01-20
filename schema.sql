DROP table if exists location;
DROP table if exists department;
DROP table if exists category;
DROP table if exists sub_category;

CREATE TABLE location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE department (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location_id INTEGER REFERENCES location(id) NOT NULL,
    description TEXT
);

CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department_id INTEGER REFERENCES department(id) NOT NULL,
    description TEXT
);

CREATE TABLE sub_category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category_id INTEGER REFERENCES category(id) NOT NULL,
    description TEXT
);