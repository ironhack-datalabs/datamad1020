
-- ----------- --
-- CHALLENGE 1 --
-- ----------- --

USE authors;
SELECT a.au_id AS author_id, a.au_lname AS `LAST NAME`, a.au_fname AS `FIRST NAME`, t.title AS TITLE, p.pub_name AS PUBLISHER
FROM titleauthor AS ta
	JOIN titles AS t
		ON ta.title_id = t.title_id
	JOIN publishers AS p
		ON p.pub_id=t.pub_id
	JOIN authors AS a
		ON a.au_id=ta.au_id;

-- FROM authors AS a
-- JOIN titleauthor AS ta
-- ON a.au_id = ta.au_idtitleauthor
-- JOIN titles AS t
-- ON ta.title_id=t.title_id
-- JOIN publishers AS p
-- ON t.pub_id = t.pub_id

-- SELECT COUNT(au_id)
-- FROM titleauthor;


-- ----------- --
-- CHALLENGE 2 --
-- ----------- --
 

SELECT a.au_id AS author_id, a.au_lname AS `LAST NAME`, a.au_fname`FIRST NAME`, p.pub_id AS PUBLISHER, COUNT(t.title) AS `TITLE COUNT`
FROM titleauthor AS ta

	JOIN authors AS a
	ON ta.au_id=a.au_id
    
	JOIN titles AS t 
	ON ta.title_id=t.title_id
    
	JOIN publishers AS p
	ON t.pub_id=p.pub_id
    
GROUP BY p.pub_id, a.au_id;


-- ----------- --
-- CHALLENGE 3 --
-- ----------- --


SELECT a.au_id AS `AUTHOR ID`, a.au_lname AS `LAST NAME`, a.au_fname AS `FIRST NAME`, SUM(t.ytd_sales) AS `TOTAL`
FROM authors AS a

	JOIN titleauthor AS ta
	ON ta.au_id=a.au_id
    
	JOIN titles AS t 
	ON ta.title_id=t.title_id

GROUP BY a.au_id
ORDER BY `TOTAL`
DESC LIMIT 3;


-- ----------- --
-- CHALLENGE 4 --
-- ----------- --


SELECT COALESCE (ytd_sales , 0 )
FROM titles;

SELECT a.au_id AS `AUTHOR ID`, a.au_lname AS `LAST NAME`, a.au_fname AS `FIRST NAME`, SUM(t.ytd_sales) AS `TOTAL`
FROM authors AS a

	JOIN titleauthor AS ta
	ON ta.au_id=a.au_id
    
	JOIN titles AS t 
	ON ta.title_id=t.title_id

GROUP BY a.au_id
ORDER BY `TOTAL`