import func

def ref_values():
    global values
    values = ["NULL", func.rand_name(), func.rand_surname(), func.rand_email(), str(func.rand_number(9)), func.rand_string(11)]
    return
    
columns = ["id", "name", "surname", "email", "phone_number" , "random_code"]
database_name = "example_database"
table_name = "example_table"
number_of_rows = 10