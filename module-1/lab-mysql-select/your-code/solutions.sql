-- Challenge 1 - Who Have Published What At Where?
SELECT 
authors.au_id AS 'AUTHOR ID',
authors.au_lname 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
titles.title AS TITLE,
publishers.pub_name as PUBLISHER
FROM authors
	JOIN titleauthor
		ON authors.au_id = titleauthor.au_id
    JOIN titles
		ON titles.title_id = titleauthor.title_id
	JOIN publishers
		ON publishers.pub_id = titles.pub_id;
-- Chekcing
SELECT COUNT(*)
FROM 
(SELECT 
authors.au_id AS 'AUTHOR ID',
authors.au_lname 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
titles.title AS TITLE,
publishers.pub_name as PUBLISHER
FROM authors
	JOIN titleauthor
		ON authors.au_id = titleauthor.au_id
    JOIN titles
		ON titles.title_id = titleauthor.title_id
	JOIN publishers
		ON publishers.pub_id = titles.pub_id) AS challenge_1;


-- Challenge 2 - Who Have Published How Many At Where?
SELECT 
authors.au_id AS 'AUTHOR ID',
authors.au_lname 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
publishers.pub_name as PUBLISHER,
COUNT(titles.title) 
FROM authors
	JOIN titleauthor
		ON authors.au_id = titleauthor.au_id
    JOIN titles
		ON titles.title_id = titleauthor.title_id
	JOIN publishers
		ON publishers.pub_id = titles.pub_id
	GROUP BY authors.au_id, publishers.pub_id;

-- Challenge 3 - Best Selling Authors
SELECT
authors.au_id AS 'AUTHOR ID',
authors.au_lname 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
COUNT(sales.qty) AS 'SALES PER AUTHOR'
FROM sales
	JOIN titles
		ON sales.title_id = titles.title_id
	JOIN titleauthor
		ON titles.title_id = titleauthor.title_id
	JOIN authors
		ON titleauthor.au_id = authors.au_id
	GROUP BY authors.au_id
    ORDER BY COUNT(sales.qty) DESC
    LIMIT 3;

-- Challenge 4 - Best Selling Authors Ranking
SELECT
authors.au_id AS 'AUTHOR ID',
authors.au_lname 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
COUNT(sales.qty) AS 'SALES PER AUTHOR'
FROM sales
	JOIN titles
		ON sales.title_id = titles.title_id
	JOIN titleauthor
		ON titles.title_id = titleauthor.title_id
	RIGHT JOIN authors
		ON titleauthor.au_id = authors.au_id
	GROUP BY authors.au_id
    ORDER BY COUNT(sales.qty) DESC;
--Checking
SELECT COUNT(*)
FROM 
(SELECT
authors.au_id AS 'AUTHOR ID',
authors.au_lname 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
COUNT(sales.qty) AS 'SALES PER AUTHOR'
FROM sales
	JOIN titles
		ON sales.title_id = titles.title_id
	JOIN titleauthor
		ON titles.title_id = titleauthor.title_id
	RIGHT JOIN authors
		ON titleauthor.au_id = authors.au_id
	GROUP BY authors.au_id
    ORDER BY COUNT(sales.qty) DESC) as chellenge_4;

-- BONUS!!
SELECT 
authors.au_id AS 'AUTHOR ID',
authors.au_lname 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
SUM(titles.advance + titles.royalty) AS PROFIT
FROM titles
	JOIN titleauthor
		ON titleauthor.title_id = titles.title_id
	JOIN authors
		ON authors.au_id = titleauthor.au_id
	GROUP BY authors.au_id
    ORDER BY PROFIT DESC
    LIMIT 3;