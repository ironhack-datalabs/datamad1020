-- CHALLENGE - 1

USE lab_sql_select;
SELECT a.au_id AS `AUTHOR ID`, a.au_lname AS `LAST NAME`, a.au_fname AS `FIRST NAME`, t.title AS `TITLE`, p.pub_name AS `PUBLISHER`  
FROM lab_sql_select.titles as t
	 JOIN lab_sql_select.titleauthor AS ta
		ON ta.title_id = t.title_id
	 JOIN lab_sql_select.authors AS a
		ON ta.au_id = a.au_id
	 JOIN lab_sql_select.publishers AS p
		ON t.pub_id = p.pub_id;

-- CHALLENGE - 2
SELECT a.au_id AS `AUTHOR ID`, a.au_lname AS `LAST NAME`, a.au_fname AS `FIRST NAME`, p.pub_name AS `PUBLISHER`, COUNT(t.title) as `TITLE COUNT`  
FROM lab_sql_select.titles as t
	 JOIN lab_sql_select.titleauthor AS ta
		ON ta.title_id = t.title_id
	 JOIN lab_sql_select.authors AS a
		ON ta.au_id = a.au_id
	 JOIN lab_sql_select.publishers AS p
		ON t.pub_id = p.pub_id
GROUP BY `AUTHOR ID`, `PUBLISHER`;

-- CHALLENGE - 2, an alternative
CREATE TEMPORARY TABLE temp
SELECT a.au_id AS `AUTHOR ID`, a.au_lname AS `LAST NAME`, a.au_fname AS `FIRST NAME`, t.title AS `TITLE`, p.pub_name AS `PUBLISHER`  
FROM lab_sql_select.titles as t
	 JOIN lab_sql_select.titleauthor AS ta
		ON ta.title_id = t.title_id
	 JOIN lab_sql_select.authors AS a
		ON ta.au_id = a.au_id
	 JOIN lab_sql_select.publishers AS p
		ON t.pub_id = p.pub_id;

SELECT `temp`.`AUTHOR ID`, `temp`.`LAST NAME`, `temp`.`FIRST NAME`,`temp`.`PUBLISHER`, COUNT(`temp`.`TITLE`) as `TITLE COUNT`
from `temp`
 GROUP BY `temp`.`AUTHOR ID`, `temp`.`PUBLISHER`;

-- CHALLENGE 3
SELECT a.au_id AS `AUTHOR ID`, a.au_lname AS `LAST NAME`, a.au_fname AS `FIRST NAME`, SUM(t.ytd_sales) as `TOTAL`  
FROM lab_sql_select.titles as t
	 JOIN lab_sql_select.titleauthor AS ta
		ON ta.title_id = t.title_id
	 JOIN lab_sql_select.authors AS a
		ON ta.au_id = a.au_id
	 JOIN lab_sql_select.publishers AS p
		ON t.pub_id = p.pub_id
	 JOIN lab_sql_select.sales AS s
		ON t.title_id = s.title_id        
GROUP BY `AUTHOR ID`, p.pub_name
ORDER BY SUM(t.ytd_sales) DESC
LIMIT 3;

-- CHALLENGE 4
SELECT a.au_id AS `AUTHOR ID`, a.au_lname AS `LAST NAME`, a.au_fname AS `FIRST NAME`, SUM(t.ytd_sales) as `TOTAL`    
FROM lab_sql_select.titles as t
	 JOIN lab_sql_select.titleauthor AS ta
		ON ta.title_id = t.title_id
	 JOIN lab_sql_select.authors AS a
		ON ta.au_id = a.au_id
	 JOIN lab_sql_select.publishers AS p
		ON t.pub_id = p.pub_id      
GROUP BY `AUTHOR ID`, p.pub_name
ORDER BY SUM(t.ytd_sales) DESC;

-- BONUS
SELECT a.au_id AS `AUTHOR ID`, a.au_lname AS `LAST NAME`, a.au_fname AS `FIRST NAME`, (SUM(t.ytd_sales*t.royalty+t.advance)) as `PORFIT`    
FROM lab_sql_select.titles as t
	 JOIN lab_sql_select.titleauthor AS ta
		ON ta.title_id = t.title_id
	 JOIN lab_sql_select.authors AS a
		ON ta.au_id = a.au_id
	 JOIN lab_sql_select.publishers AS p
		ON t.pub_id = p.pub_id      
GROUP BY `AUTHOR ID`, p.pub_name  -- Might come back later, the selected 
ORDER BY `PORFIT` DESC
LIMIT 3;
