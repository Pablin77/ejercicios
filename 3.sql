/*  
3 - A team needs a list of customers who have
a maximum number of failure events (status = "failure") in their campaigns.
For all customers with more than 3 events with status = 'failure', report the customer name and
their number of failures.
The result should be in the following format: customer, failures.
● customer is a candidate's full name, the first_name and last_name separated by a single
space.
● The order of the output is not important.
*/ 
SELECT
    CONCAT(C.first_name, ' ', C.last_name) AS customer,
    COUNT(E.status) AS failures
FROM
    customers C
JOIN
    campaigns Cam ON C.id = Cam.customer_id
JOIN
    events E ON Cam.id = E.campaign_id
WHERE
    E.status = 'failure'
GROUP BY
    C.id, C.first_name, C.last_name
HAVING
    COUNT(E.status) > 3
