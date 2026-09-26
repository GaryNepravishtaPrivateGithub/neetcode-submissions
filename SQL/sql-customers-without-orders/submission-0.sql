-- Write your query below

select
    name
from customers
left join orders
  on customers.id = orders.customer_id
where orders.customer_id is null 

-- Additional Notes/Logic:

/*
    We can identify that we are looking for customer names (found only 
    in the 'customers' table thus explaining 'select names from customers').

    We want to include order information linked to each customer. While 'id'
    is the primary key for 'orders' table, 'customer_id' is the correct 1-1
    foreign key that links a customer to their respective order.

    To find customers that never placed an order, we search for names in the 
    'customers' table (left join) that do not have an order to their name.  

*/
