
-- Challange 1 --
USE `lab-mysql-select`;
SELECT a.au_id AS 'AUTHOR ID', a.au_lname AS 'LAST NAME', a.au_fname AS 'FIRST NAME', t.title AS TITLE, p.pub_name AS PUBLISHER
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
JOIN titleauthor AS ta
ON a.au_id=ta.au_id
JOIN titles AS t
ON ta.title_id=t.title_id
JOIN sales AS s
ON s.title_id=t.title_id
GROUP BY a.au_id
ORDER BY TOTAL DESC
LIMIT 3;

-- Challange 4 --

SELECT a.au_id AS 'AUTHOR ID', a.au_lname AS 'LAST NAME', a.au_fname AS 'FIRST NAME',
 SUM(s.qty) AS 'TOTAL'
FROM authors AS a
JOIN titleauthor AS ta
ON a.au_id=ta.au_id
JOIN titles AS t
ON ta.title_id=t.title_id
JOIN sales AS s
ON s.title_id=t.title_id
GROUP BY a.au_id
ORDER BY TOTAL DESC
LIMIT 23;
