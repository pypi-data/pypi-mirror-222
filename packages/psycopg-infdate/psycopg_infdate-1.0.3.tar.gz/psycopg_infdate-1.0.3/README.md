# psycopg Infinite dates

Postgresql has support for special dates, 'infinity' and '-infinity', which compare respectively above or below any other dates.
This module gives psycopg3 support for those dates.

## Background


Suppose you have a set of contracts with suppliers. The end date of the contract would be an SQL DATE, represented as a datetime.date in Python.  

| Supplier Name    | Start Date | End Date   |
|------------------|------------|------------|
| ConcreteWorks    | 2023-04-01 | 2024-03-31 |
| Bricks R Us      | 2022-03-25 | 2023-09-24 |
| Lawn Maintenance | 2023-06-03 | NULL       |

Some suppliers are on fixed contracts with a known termination date. 
It is temping to represent the open-ended lawn maintenance contract as having a NULL end date, after all, 
all contracts eventually reach an end, we just don't know when.

This results in awkward SQL queries, such as:
```sql
SELECT supplier_name FROM suppliers WHERE end_date >= CURRENT_DATE OR end_date IS NULL
```

NULL is not a value and is therefore not indexed. 
The fact that we had to explicitly include NULL, as if it were a normal value, is a giveaway that this 
data is not normalized. 

While we do know not know what the end date will be, we do know that it is after today; 
it isn't a completely unknown quantity.
 
We could use a sentinel value, such as 1999-12-31. That's obviously a bad choice because it is in the past.
How about 2099-12-31? That could also represent real data, if the data pertains to future events.
There isn't any choice of sentinel value that could never be confused real data in some context.

Postgres has two special values for dates and timestamps that can be used instead
https://www.postgresql.org/docs/current/datatype-datetime.html#DATATYPE-DATETIME-SPECIAL-VALUES

* 'infinity'::DATE compares later than all other dates.
* '-infinity'::DATE compares before than all other dates.

Now we can use this for our lawn maintenance contract:

| Supplier Name    | Start Date | End Date   |
|------------------|------------|------------|
| ConcreteWorks    | 2023-04-01 | 2024-03-31 |
| Bricks R Us      | 2022-03-25 | 2023-09-24 |
| Lawn Maintenance | 2023-06-03 | infinity   |

And our SQL query is simpler too:
```sql
SELECT supplier_name FROM suppliers WHERE end_date >= CURRENT_DATE
```

## The problem



So far, so good. Let's try that SQL query in Python:


```python
with dbh.cursor() as cur:
    cur.execute("SELECT supplier_name FROM suppliers WHERE end_date >= CURRENT_DATE")
    suppliers = cur.fetchall()
```

This yields the error:
_psycopg.DataError: date too large (after year 10K): 'infinity'_. Not what we wanted!

The problem is that the corresponding Python type, datetime.date, cannot represent this value. 
It feels like we're back to square one.

## The solution

psycopg3 has the ability to register new dumpers and loaders that get data from the database and
send data to the database. Their job is to convert between Postgresql representation and Python objects.  

This module adds support implements a Python type for each of these special values, and creates the corresponding dumpers and 
loaders to enable the special values to be handled.

The new types implement basic date arithmetic and comparisons in a similar way to Postgresql, such as:
* 'infinity' == 'infinity'
* 'infinity' > datetime.date > '-infinity'
* 'infinity' + datetime.timedelta == 'infinity'
* 'infinity' - 'infinity' raises a ValueError


## Using the module

### For all database connections

```python
import psycopg_infdate
import psycopg

psycopg_infdate.register_inf_date_handler(psycopg)
dbh = psycopg.connect('...')
with dbh.cursor() as cur:
    cur.execute("SELECT 'infinity'::DATE")
    answer = cur.fetchall()
```

### For one database connection

```python
import psycopg_infdate
import psycopg

dbh = psycopg.connect('...')
psycopg_infdate.register_inf_date_handler(dbh)
with dbh.cursor() as cur:
    cur.execute("SELECT 'infinity'::DATE")
    answer = cur.fetchall()
```

### For just this cursor

```python
import psycopg_infdate
import psycopg

dbh = psycopg.connect('...')
with dbh.cursor() as cur:
    psycopg_infdate.register_inf_date_handler(cur)
    cur.execute("SELECT 'infinity'::DATE")
    answer = cur.fetchall()
```

