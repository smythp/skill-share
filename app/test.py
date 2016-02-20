import sqlite3

conn = sqlite3.connect("../skill.db")

c = conn.cursor()

out = c.execute("SELECT * FROM skill;")

# for row in out.fetchall():
#     print(row)

print('')


# for key in out.description:
#     print(key[0])




def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



def make_dict(cursor):
    list_of_dicts = []
    keys_list = []
    for key in cursor.description:
        keys_list.append(key[0])

    for (number,row) in enumerate(cursor.fetchall()):
        dict_out = {}
        for number2,key in enumerate(keys_list):
            dict_out[key] = row[number2]
        list_of_dicts.append(dict_out)

    return list_of_dicts


foo = make_dict(out)
