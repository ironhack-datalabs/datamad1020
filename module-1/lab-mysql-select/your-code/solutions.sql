
-- Challange 1 --
USE `lab-mysql-select`;
SELECT a.au_id AS 'AUTHOR ID', a.au_lname AS 'LAST NAME', 
a.au_fname AS 'FIRST NAME', t.title AS TITLE, p.pub_name AS PUBLISHER
FROM authors AS a
JOIN titleauthor AS ta
ON a.au_id=ta.au_id
JOIN titles AS t
ON ta.title_id=t.title_id
JOIN publishers AS p
ON t.pub_id=p.pub_id;

-- Challange 2 --


SELECT a.au_id AS 'AUTHOR ID', a.au_lname AS 'LAST NAME', a.au_fname AS 'FIRST NAME',
p.pub_name AS PUBLISHER, COUNT(t.title) AS 'TITLE COUNT'
FROM authors AS a
JOIN titleauthor AS ta
ON a.au_id=ta.au_id
JOIN titles AS t
ON ta.title_id=t.title_id
JOIN publishers AS p
ON t.pub_id=p.pub_id
GROUP BY a.au_id, PUBLISHER;

-- Challange 3 --

SELECT a.au_id AS 'AUTHOR ID', a.au_lname AS 'LAST NAME', a.au_fname AS 'FIRST NAME',
 SUM(s.qty) AS 'TOTAL'
FROM authors AS a
LEFT JOIN titleauthor AS ta
ON a.au_id=ta.au_id
LEFT JOIN titles AS t
ON ta.title_id=t.title_id
LEFT JOIN sales AS s
ON s.title_id=t.title_id
GROUP BY a.au_id
ORDER BY TOTAL DESC
LIMIT 3;

-- Challange 4 --

SELECT a.au_id AS 'AUTHOR ID', a.au_lname AS 'LAST NAME', a.au_fname AS 'FIRST NAME', COALESCE(SUM(s.qty),0) AS 'TOTAL'
FROM authors AS a
LEFT JOIN titleauthor AS ta
ON a.au_id=ta.au_id
LEFT JOIN titles AS t
ON ta.title_id=t.title_id
LEFT JOIN sales AS s
ON s.title_id=t.title_id
GROUP BY a.au_id
ORDER BY TOTAL DESC
LIMIT 23;

-- BONUS --

SELECT a.au_id AS 'AUTHOR ID', a.au_lname AS 'LAST NAME', a.au_fname AS 'FIRST NAME',
t.advance + t.price*ytd_sales*t.royalty/100*ta.royaltyper/100 AS PROFIT
FROM authors AS a
JOIN titleauthor AS ta
ON a.au_id=ta.au_id
JOIN titles AS t
ON ta.title_id=t.title_id
JOIN sales AS s
ON s.title_id=t.title_id
GROUP BY t.title_id
ORDER BY PROFIT DESC
LIMIT 3;

-- If I run the code without "GROUP BY a.au_id" it works but the PROFIT coulumn is not the total amounts 
-- as it is divided by the different titles. Which means that this table is ordered by the top 3 tittles profit.

-- If I add "GROUP BY a.au_id" I got the error:"Error Code: 1055. (...)nonaggregated column 
-- 'lab-mysql-select.t.advance'(...) So I tried to creat a temporary table to work on it, 
-- But I get the same error:

CREATE TEMPORARY TABLE BONUS
SELECT a.au_id AS 'AUTHOR ID', a.au_lname AS 'LAST NAME', a.au_fname AS 'FIRST NAME',
t.advance + t.price*ytd_sales*t.royalty/100*ta.royaltyper/100 AS PROFIT
FROM authors AS a
JOIN titleauthor AS ta
ON a.au_id=ta.au_id
JOIN titles AS t
ON ta.title_id=t.title_id
JOIN sales AS s
ON s.title_id=t.title_id
ORDER BY PROFIT DESC;

SELECT 'AUTHOR ID', CONCAT("LAST NAME", ' ', "FIRST NAME") AS COMPLET_NAME,PROFIT
FROM `lab-mysql-select`.BONUS
GROUP BY COMPLET_NAME
ORDER BY PROFIT DESC
LIMIT 30;


