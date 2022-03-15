import sqlite3

"""#1 Создание таблиц """


with sqlite3.connect('animal.db') as connection:
    cur = connection.cursor()

    query = """
        
        CREATE TABLE animal_types (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_type VARCHAR(50) );
        
        CREATE TABLE breeds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        breed_type VARCHAR(100) );
        
        CREATE TABLE colors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        color_type VARCHAR(100) );
        
        CREATE TABLE outcome_subtypes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        outcome_subtype VARCHAR(100) );
        
        CREATE TABLE outcome_types (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        outcome_type VARCHAR(100) );
    
    
        CREATE TABLE animal_v2 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        old_index INTEGER,
        age_upon_outcome TEXT, -- возраст животного на момент прибытия (в неделях)
        animal_id TEXT NOT NULL, -- идентификато животного
        name VARCHAR(50), -- кличка животного
        date_of_birth DATETIME,  -- дата рождения
        outcome_month INTEGER, -- месяц прибытия
        outcome_year INTEGER,  -- год прибытия
        
        animal_type_id INTEGER, -- тип животного FOREIGN KEY
        outcome_subtype INTEGER,  -- программа в которой учавствует животное  FOREIGN KEY
        outcome_type INTEGER,  -- что сейчас с животным  FOREIGN KEY
        
        FOREIGN KEY(animal_type_id) REFERENCES animal_types(id),
        FOREIGN KEY(outcome_subtype) REFERENCES outcome_subtypes(id),
        FOREIGN KEY(outcome_type) REFERENCES outcome_types(id) );
        
        CREATE TABLE animal_color (
        color_id INTEGER,
        animal_id INTEGER,
        FOREIGN KEY(color_id) REFERENCES colors(id),
        FOREIGN KEY(animal_id) REFERENCES animal_v2(id)
        CONSTRAINT new_pk PRIMARY KEY(animal_id, color_id)
         );
        
        CREATE TABLE animal_breed (
        breed_id INTEGER,
        animal_id INTEGER,
        FOREIGN KEY(breed_id) REFERENCES breeds(id),
        FOREIGN KEY(animal_id) REFERENCES animal_v2(id)
        CONSTRAINT new_pk PRIMARY KEY(animal_id, breed_id)
         );
        
        
        """

    cur.executescript(query)
