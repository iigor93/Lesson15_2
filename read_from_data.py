import sqlite3
"""Чтение данных по id"""


def main_read(animal_id):
    with sqlite3.connect('animal.db') as connection:
        cur = connection.cursor()

        query_read_main_data = """SELECT 
            animal_v2.id AS main_animal_id,
            animal_v2.name AS main_animal_name,
            animal_v2.age_upon_outcome AS age,
            animal_v2.animal_id AS animal_id_,
            animal_v2.date_of_birth AS date_of_birth,
            animal_v2.outcome_year AS outcome_year,
            animal_v2.outcome_month AS outcome_month,
                        
            outcome_types.outcome_type AS animal_outcome_type,
            outcome_subtypes.outcome_subtype AS animal_outcome_subtype,
            animal_types.animal_type AS animal_type
    
            FROM animal_v2
            
            JOIN outcome_types ON outcome_types.id = animal_v2.outcome_type
            JOIN outcome_subtypes ON outcome_subtypes.id = animal_v2.outcome_subtype
            JOIN animal_types ON animal_types.id = animal_v2.animal_type_id
            
            WHERE main_animal_id = (?)"""

        query_read_add_color_data = """
            SELECT 
            animal_v2.id AS main_animal_id,
            colors.color_type AS color_color_name
            
            FROM animal_v2
            
            JOIN animal_color ON  animal_color.animal_id = main_animal_id
            JOIN colors ON colors.id = animal_color.color_id
            
            WHERE main_animal_id = (?)
            """

        query_read_add_breed_data = """
            SELECT 
            animal_v2.id AS main_animal_id,
            breeds.breed_type AS breed_name

            FROM animal_v2

            JOIN animal_breed ON animal_breed.animal_id = main_animal_id
            JOIN breeds ON breeds.id = animal_breed.breed_id

            WHERE main_animal_id = (?)
            """

        param = []
        param.append(animal_id)
        param = tuple(param)

        read_data_main = cur.execute(query_read_main_data, param).fetchall()[0]
        read_data_add_color = cur.execute(query_read_add_color_data, param).fetchall()
        read_data_add_breed = cur.execute(query_read_add_breed_data, param).fetchall()

        color_list = []
        breed_list = []

        for item in read_data_add_color:
            color_list.append(item[1])
        for item in read_data_add_breed:
            breed_list.append(item[1])

        data_return = {}
        data_return['name'] = read_data_main[1]
        data_return['age'] = read_data_main[2]
        data_return['animal_id'] = read_data_main[3]
        data_return['date_of_birth'] = read_data_main[4]
        data_return['outcome_year'] = read_data_main[5]
        data_return['outcome_month'] = read_data_main[6]

        data_return['outcome_type'] = read_data_main[7]
        data_return['outcome_subtype'] = read_data_main[8]
        data_return['outcome_animal_type'] = read_data_main[9]

        data_return['colors'] = color_list
        data_return['breed'] = breed_list

    return data_return
