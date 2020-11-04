-- CHALLENGE - 1

USE lab_sql_select;
SELECT a.au_id AS 'AUTHOR ID', a.au_lname AS 'LAST NAME', a.au_fname AS 'FIRST NAME', t.title AS 'TITLE', p.pub_name AS 'PUBLISHER'  
FROM titleauthor as ta
	JOIN lab_sql_select.authors AS a
		ON ta.au_id = ta.au_id
	JOIN lab_sql_select.titles AS t
		ON ta.title_id = ta.title_id
	JOIN lab_sql_select.publishers AS p
		ON t.pub_id = p.pub_id;
        
        