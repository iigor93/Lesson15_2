import sqlite3

"""#4  копирование данных для таблиц many to many """

query_read_old = """ SELECT 
            "index",
            breed,
            color1,
            color2

            FROM animals 
            
             """

query_read_new = """ SELECT
            "id",
            old_index
            
            FROM animal_v2
            """

query_write = """ INSERT INTO animal_color 
        ( 
         color_id, 
         animal_id
       
        ) 
        VALUES (?, ?) """

query_write_breed = """ INSERT INTO animal_breed 
        ( 
         breed_id, 
         animal_id

        ) 
        VALUES (?, ?) """

query_read_breed = """SELECT * FROM breeds"""
query_read_color = """SELECT * FROM colors"""

with sqlite3.connect('animal.db') as connection:
    cur = connection.cursor()

    # все варианты пород
    data_read_bread_all = cur.execute(query_read_breed).fetchall()
    # все варианты цветов
    data_read_color_all = cur.execute(query_read_color).fetchall()

    # старые записи
    data_read_old = cur.execute(query_read_old).fetchall()

    # Новые записи
    data_read_new = cur.execute(query_read_new).fetchall()

    color_list = []
    breed_list = []

    for item in data_read_old:
        temp_list = []
        temp_list_color2 = []
        temp_breed_list = []

        # color1
        if item[2] is None:
            new_temp_item = 'NoType'
        else:
            new_temp_item = item[2]

        # поиск ID цвета в таблице color1
        for temp_item_ in data_read_color_all:
            if new_temp_item == temp_item_[1]:
                temp_list.append(temp_item_[0])
                break

        # color2
        if (item[3] is not None) and (item[3] != item[2]):
            for temp_item_ in data_read_color_all:
                if item[3] == temp_item_[1]:
                    temp_list_color2.append(temp_item_[0])
                    break

        new_animal_id = 0
        # поиск в новой таблице ID
        for temp_item_ in data_read_new:
            if item[0] == temp_item_[1]:
                new_animal_id = temp_item_[0]
                temp_list.append(temp_item_[0])
                if (item[3] is not None) and (item[3] != item[2]):
                    temp_list_color2.append(temp_item_[0])
                break
        color_list.append(tuple(temp_list))
        if (item[3] is not None) and (item[3] != item[2]):
            color_list.append(tuple(temp_list_color2))
            pass

        # поиск породы
        temp_bree_new_set = set(str(item[1]).split('/'))
        temp_bree_new_set = list(temp_bree_new_set)
        for breed_item in temp_bree_new_set:
            for all_breed_item in data_read_bread_all:
                if breed_item == all_breed_item[1]:
                    temp_breed_list = []
                    temp_breed_list.append(all_breed_item[0])
                    temp_breed_list.append(new_animal_id)
                    break
            breed_list.append(tuple(temp_breed_list))


    #print(breed_list)
    cur.executemany(query_write, color_list)
    cur.executemany(query_write_breed, breed_list)
