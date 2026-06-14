-- Write your query below

select 
    customer_id
from customers
where revenue > 0
    and year = 2020

-- Additional Notes/Logic
/*
    We understand that return order does not matter, so we can just select
    customer_id without any constraints (no order by clause is required).

    (customer_id, year) is the primary key, so each customer can have
    at most one row per year. Therefore, no aggregation or distinct is needed.

    year is an integer column, so the comparison should be to 2020, not '2020'.
    Quotes are typically for strings, dates, or timestamps.
*/

