-- Challenge 1

SELECT authors.au_id AS 'AUTHOR ID', au_lname AS 'LAST NAME', au_fname AS 'FIRST_NAME', title AS 'TITLE', pub_name AS 'PUBLISHER'
FROM authors 
	JOIN titleauthor 
		ON authors.au_id=titleauthor.au_id
	JOIN titles 
		ON titleauthor.title_id=titles.title_id
	JOIN publishers 
		ON titles.pub_id=publishers.pub_id;

-- Challenge 2

SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', publishers.pub_name AS 'PUBLISHER', COUNT(titles.title_id) AS 'TITLE COUNT'
FROM authors 
	JOIN titleauthor 
		ON authors.au_id=titleauthor.au_id
	JOIN titles 
		ON titleauthor.title_id=titles.title_id
	JOIN publishers 
		ON titles.pub_id=publishers.pub_id
GROUP BY authors.au_id, publishers.pub_id;

-- Challenge 3

SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname 'LAST NAME', authors.au_fname AS 'FIRST NAME', publishers.pub_name AS 'PUBLISHER', SUM(titles.ytd_sales) AS 'TOTAL'
FROM authors
	JOIN titleauthor 
		ON authors.au_id=titleauthor.au_id
	JOIN titles 
		ON titleauthor.title_id=titles.title_id
	JOIN sales
		ON titles.title_id=sales.title_id
	JOIN publishers 
		ON titles.pub_id=publishers.pub_id
GROUP BY authors.au_id, publishers.pub_name
ORDER BY SUM(titles.ytd_sales) DESC
LIMIT 3;

-- Challenge 4
SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname 'LAST NAME', authors.au_fname AS 'FIRST NAME', publishers.pub_name AS 'PUBLISHER', SUM(titles.ytd_sales) AS 'TOTAL'
FROM authors
	JOIN titleauthor 
		ON authors.au_id=titleauthor.au_id
	JOIN titles 
		ON titleauthor.title_id=titles.title_id
	JOIN sales
		ON titles.title_id=sales.title_id
	JOIN publishers 
		ON titles.pub_id=publishers.pub_id
GROUP BY authors.au_id, publishers.pub_name
ORDER BY SUM(titles.ytd_sales) DESC;