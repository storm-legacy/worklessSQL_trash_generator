import func

##----- EDIT ZONE -----###
def ref_values():
    global values
    values = ["NULL", func.rand_name(), func.rand_surname(
    ), func.rand_email(), str(func.rand_number(9)), func.rand_string(11)]
    return
columns = ["id", "name", "surname", "email", "phone_number", "random_code"]
database_name = "example_database"
table_name = "example_table"
number_of_rows = 10

##----- EDIT ZONE -----###


####------------ DANGER ZONE -----------####
RED = "\033[1;31m"
RESET = "\033[0;0m"
ref_values()
if len(columns) != len(values):
    print(RED + "[ERROR] COLUMNS.length != VALUES.length" + RESET)
    exit()

sql = "INSERT INTO %s.%s(" % (database_name, table_name)
for i in range(0, len(columns)):
    sql += columns[i]
    if i == len(columns)-1:
        break
    else:
        sql += ", "

sql += ") VALUES("

for i in range(0, number_of_rows):
    ref_values()
    for j in range(0, len(values)):
        if values[j] == "NULL":
            sql += "NULL"
        elif isinstance(values[j], int):
            sql += str(values[j])
        else:
            sql += "\'" + str(values[j]) + "\'"
        if j == len(values)-1:
            sql += ")"
        else:
            sql += ", "
    if i == number_of_rows-1:
        sql += ";"
    else:
        sql += ", ("
print(sql)
####------------ DANGER ZONE -----------####
