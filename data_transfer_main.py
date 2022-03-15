import sqlite3

"""#3 main read write"""
"""#копирование данных животного"""


query_read = """ SELECT 
            age_upon_outcome, 
            animal_id, 
            name,  
            date_of_birth, 
            outcome_month, 
            outcome_year,
            animal_type,
            outcome_subtype,
            outcome_type,
            "index"
            
            FROM animals 
            """

query_read_animal_type = """SELECT * FROM animal_types"""
query_read_outcome_subtype = """SELECT * FROM outcome_subtypes"""
query_read_outcome_type = """SELECT * FROM outcome_types"""


query_write = """ INSERT INTO animal_v2 
        (age_upon_outcome, 
        animal_id, 
        name, 
        date_of_birth,
        outcome_month,
        outcome_year,
        animal_type_id,
        outcome_subtype,
        outcome_type,
        old_index
        ) 
        
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """

with sqlite3.connect('animal.db') as connection:
    cur = connection.cursor()

    data_read = cur.execute(query_read).fetchall()
    data_read_animal_type = cur.execute(query_read_animal_type).fetchall()
    data_read_outcome_subtype = cur.execute(query_read_outcome_subtype).fetchall()
    data_read_outcome_type = cur.execute(query_read_outcome_type).fetchall()

    new_list = []
    for item in data_read:
        temp_list = list(item[:6])
        new_temp_item = ''

        if item[6] is None:
            new_temp_item = 'NoType'
        else:
            new_temp_item = item[6]

        for temp_item_ in data_read_animal_type:
            if new_temp_item == temp_item_[1]:
                temp_list.append(temp_item_[0])
                break

        if item[7] is None:
            new_temp_item = 'NoType'
        else:
            new_temp_item = item[7]

        for temp_item_ in data_read_outcome_subtype:
            if new_temp_item == temp_item_[1]:
                temp_list.append(temp_item_[0])
                break

        if item[8] is None:
            new_temp_item = 'NoType'
        else:
            new_temp_item = item[8]

        for temp_item_ in data_read_outcome_type:
            if new_temp_item == temp_item_[1]:
                temp_list.append(temp_item_[0])
                break

        temp_list.append(item[9])

        new_list.append(tuple(temp_list))

    cur.executemany(query_write, new_list)
