-- Write your query below

with bonus_table as (
    select
        employee_id
        , case
            when (employee_id % 2 = 1) and (substring(name, 1, 1) <> 'M') 
            then salary  
            else 0
        end as bonus 
    from employees 
)

select 
    employee_id
    , bonus 
from bonus_table
order by employee_id
 
 -- Additional Notes/Logic 
/*

    We can create a CTE (Common Table Expression) to define a 'bonus' column. Naming 
    this table as 'bonus_table' helps us understand the purpose of the table being 
    to calculate the bonus per a given 'employee_id'.

    To calculate both scenarios regarding an employee's bonus quantity (i.e. either 
    100% of their salary or 0), we can write a 'CASE' expression. 
    
    If an 'employee_id' is odd (aka employee_id mod 2 leaves a remainder) AND  
    their first character of their name is NOT 'M' (can be calculated with the
    [start:length] feature of 'SUBSTRING' function or using 'name not like 'M%'),
    then their bonus is equivalent to salary. Otherwise, the bonus is zero.

    We can then alias the column name of those two distinct scenarios as 'bonus',
    which we can then select 'employee_id' and 'bonus' from the 'bonus_table'.

*/
