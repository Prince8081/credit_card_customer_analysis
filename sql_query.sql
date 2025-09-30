create database Credit_Card_Customer_db;
use Credit_Card_Customer_db;
select * from credit_card_customers;


-- Total Customers & Basic Overview --

create view customer_overview as
SELECT 
    COUNT(*) AS total_customers,
    ROUND(AVG(CLV), 2) AS avg_CLV,
    ROUND(AVG(credit_utilization_ratio), 2) AS avg_credit_utilization,
    ROUND(AVG(transaction_frequency)) AS avg_transaction_frequency
FROM
    credit_card_customers;
    
select * from customer_overview;


-- Customer Segmentation by CLV --

create view clv_category_summary as
SELECT 
    CLV_Category,
    COUNT(*) AS total_customers,
    ROUND(AVG(CLV), 2) AS avg_CLV,
    ROUND(AVG(credit_utilization_ratio), 2) AS avg_credit_utilization,
    ROUND(AVG(transaction_frequency)) AS avg_transaction_frequency
FROM
    credit_card_customers
GROUP BY 1
ORDER BY 3 DESC;

select * from clv_category_summary;


-- Transaction Frequency Category Distribution --

create view transaction_frequency_category as
SELECT 
    transaction_frequency_category,
    COUNT(*) AS total_customers,
    ROUND(AVG(CLV), 2) AS avg_CLV,
    ROUND(AVG(credit_utilization_ratio), 2) AS avg_credit_utilization,
    ROUND(AVG(transaction_frequency)) AS avg_transaction_frequency
FROM
    credit_card_customers
    group by 1 ;
    
select * from transaction_frequency_category;
    
    
  -- High Risk Customer Analysis
--    (High Utilization + Multiple Late Payments) --


create view  high_risk_customer as
SELECT 
    COUNT(*) AS high_risk_customers,
    ROUND(AVG(CLV), 2) AS avg_CLV,
    ROUND(AVG(credit_utilization_ratio), 2) AS avg_credit_utilization,
    ROUND(AVG(transaction_frequency)) AS avg_transaction_frequency,
    ROUND(AVG(number_of_late_payments)) AS avg_no_of_late_payment
FROM
    credit_card_customers
WHERE
    Credit_Utilization_Ratio > 0.8
        AND number_of_late_payments > 2;
        
select * from high_risk_customer;



 -- Premium Customers (High CLV + High Utilization) --
 
 create view Premium_customer as
 SELECT 
    customer_id,
    CLV,
    credit_utilization_ratio,
    Transaction_Frequency,
    spend_to_income_ratio
FROM
    credit_card_customers
WHERE
    CLV_Category = 'High CLV'
        AND Credit_Utilization_Ratio > 0.7
ORDER BY CLV DESC
LIMIT 10;

select * from Premium_customer;



-- High Spenders (Spend-to-Income Ratio > 50%) --

create view high_spenders as
SELECT 
    COUNT(*) AS Higher_spender_customer,
    ROUND(AVG(spend_to_income_ratio), 2) AS avg_spend_ratio,
    ROUND(AVG(CLV), 2) AS avg_CLV
FROM
    credit_card_customers
WHERE
    spend_to_income_ratio > 30;
    
select * from high_spenders;
    
    
    

    


