1-

def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

limit = 5
generator = square_root_generator(limit)

print(sum(generator))

----------------------------------------------------------------------------------------------------------
2- 

def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

limit = 13
generator = square_root_generator(limit)

for sqrt_value in generator:
    print(sqrt_value)

----------------------------------------------------------------------------------------------------------
3-

import dlt
import duckdb

def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}


def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}


pipeline = dlt.pipeline(pipeline_name='hw_pipeline', destination='duckdb', dataset_name='hw_dataset')

info_1 = pipeline.run(people_1(), table_name='people', write_disposition='replace')

info_2 = pipeline.run(people_2(), table_name='people', write_disposition='append')

print(info_1)
print(info_2)

conn = duckdb.connect(f"{pipeline.pipeline_name}.duckdb")

conn.sql(f"SET search_path = '{pipeline.dataset_name}'")

display(conn.sql("show tables"))

people = conn.sql("SELECT * FROM people")
display(people)

req_1 = conn.sql("SELECT sum(age) FROM people")
display(req_1)

----------------------------------------------------------------------------------------------------------
4-

import dlt
import duckdb

def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}


def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}


pipeline = dlt.pipeline(pipeline_name='hw_pipeline', destination='duckdb', dataset_name='hw_dataset')

info_1 = pipeline.run(people_1(), table_name='people', write_disposition='replace', primary_key='ID')

info_2 = pipeline.run(people_2(), table_name='people', write_disposition='merge')

print(info_1)
print(info_2)

conn = duckdb.connect(f"{pipeline.pipeline_name}.duckdb")

conn.sql(f"SET search_path = '{pipeline.dataset_name}'")

display(conn.sql("show tables"))

people = conn.sql("SELECT * FROM people")
display(people)

req_2 = conn.sql("SELECT sum(age) FROM people")
display(req_2)