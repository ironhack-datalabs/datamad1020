

-- CHALLENGE  1
SELECT  p.au_id AS "AUTHOR ID",
        p.au_fname AS "FIRST NAME",
        p.au_lname AS "LAST NAME",
	titles.title AS "TITLE",
	publishers.pub_name AS "PUBLISHER"

FROM publications.authors AS p
JOIN titleauthor
ON p.au_id = titleauthor.au_id
JOIN titles
ON titleauthor.title_id = titles.title_id
JOIN publishers
ON titles.pub_id = publishers.pub_id;

--CHALLENGE  2
SELECT  p.au_id AS "AUTHOR ID",
        p.au_fname AS "FIRST NAME",
        p.au_lname AS "LAST NAME",
        publishers.pub_name AS "PUBLISHER" ,
COUNT(DISTINCT titles.title) AS "TITLE COUNT"
FROM publications.authors AS p
JOIN titleauthor
ON p.au_id = titleauthor.au_id
JOIN titles
ON titleauthor.title_id = titles.title_id
JOIN publishers
ON titles.pub_id = publishers.pub_id
GROUP BY "AUTHOR ID", PUBLISHER;

--CHALLENGE  3
SELECT  p.au_id AS "AUTHOR ID",
	p.au_fname AS "FIRST NAME",
     	p.au_lname AS "LAST NAME",
        SUM(DISTINCT s.qty) AS `TOTAL`

FROM publications.authors AS p
JOIN titleauthor AS t
ON p.au_id = t.au_id
JOIN sales AS s
ON t.title_id = s.title_id
GROUP BY "AUTHOR ID"
ORDER BY `TOTAL` DESC
LIMIT 3;

-- CHALLENGE  4
SELECT  p.au_id AS "AUTHOR ID",
        p.au_fname AS "FIRST NAME",
        p.au_lname AS "LAST NAME",
        SUM(DISTINCT s.qty) AS `TOTAL`

FROM publications.authors AS p
JOIN titleauthor AS t
ON p.au_id = t.au_id
JOIN sales AS s
ON t.title_id = s.title_id
GROUP BY "AUTHOR ID"
ORDER BY `TOTAL` DESC;