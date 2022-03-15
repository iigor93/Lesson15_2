import sqlite3

"""#2 копирование данных новых таблиц (порода, тип, цвет и т.д.)"""


def read_write(query_read, query_write, query_read_2=''):
    with sqlite3.connect('animal.db') as connection:
        cur = connection.cursor()

        data_read = cur.execute(query_read)

        new_list = [('NoType',)]
        for item in data_read:
            item_list = str(item[0]).split('/')
            for new_item in item_list:
                temp_list = []
                temp_list.append(new_item)
                new_list.append(tuple(temp_list))

        if query_read_2:
            data_read_2 = cur.execute(query_read_2)

            for item in data_read_2:
                new_list.append(item)

        new_list = set(new_list)

        cur.executemany(query_write, new_list)
    return 0


# outcome_type
query_read = """ SELECT DISTINCT outcome_type FROM animals  """
query_write = """ INSERT INTO outcome_types (outcome_type) VALUES (?) """
read_write(query_read, query_write)


# outcome_subtype
query_read = """  SELECT DISTINCT outcome_subtype FROM animals   """
query_write = """ INSERT INTO outcome_subtypes (outcome_subtype) VALUES (?) """
read_write(query_read, query_write)


# breeds
query_read = """  SELECT DISTINCT breed FROM animals  """
query_write = """ INSERT INTO breeds (breed_type) VALUES (?) """
read_write(query_read, query_write)


# animal_type
query_read = """ SELECT DISTINCT animal_type FROM animals   """
query_write = """ INSERT INTO animal_types (animal_type) VALUES (?) """
read_write(query_read, query_write)


# colors
query_read_1 = """  SELECT DISTINCT color1 FROM animals  """
query_read_2 = """ SELECT DISTINCT color2 FROM animals """
query_write = """ INSERT INTO colors (color_type) VALUES (?) """
read_write(query_read_1, query_write, query_read_2)


