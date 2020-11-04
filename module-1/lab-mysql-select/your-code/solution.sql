-- Challenge 1:
SELECT
	authors.au_id as 'AUTHOR ID',
    authors.au_lname as 'LAST NAME',
    authors.au_fname as 'FIRST NAME',
    titles.title as 'TITLE',
    publishers.pub_name as 'PUBLISHER'
FROM my_lab.authors
LEFT JOIN my_lab.titleauthor
ON authors.au_id = titleauthor.au_id
LEFT JOIN my_lab.titles
ON titleauthor.title_id = titles.title_id
LEFT JOIN my_lab.publishers
ON titles.pub_id = publishers.pub_id;



-- Challenge 2:
SELECT 
	authors.au_id as 'AUTHOR_ID',
    authors.au_lname as 'LAST NAME',
    authors.au_fname as 'FIRST NAME',
	COUNT(titles.title) as 'TITLE COUNT',
    publishers.pub_name as 'PUBLISHER'

FROM authors
LEFT JOIN titleauthor
	ON authors.au_id = titleauthor.au_id
LEFT JOIN titles
	ON titleauthor.title_id = titles.title_id 
LEFT JOIN publishers
	ON titles.pub_id = publishers.pub_id
GROUP BY AUTHOR_ID, PUBLISHER
ORDER BY AUTHOR_ID

-- Challenge 3:
SELECT 
	authors.au_id AS 'AUTHOR_ID',
    authors.au_lname AS 'LAST NAME',
    authors.au_fname AS 'FIRST NAME',
    SUM(sales.qty) AS 'TOTAL'
FROM my_lab.authors
LEFT JOIN titleauthor
	ON authors.au_id = titleauthor.au_id
LEFT JOIN titles
	ON titleauthor.title_id = titles.title_id 
LEFT JOIN sales
	ON titles.title_id = sales.title_id
GROUP BY AUTHOR_ID
ORDER BY TOTAL DESC
LIMIT 3;

-- Challenge 4:
SELECT 
	authors.au_id AS 'AUTHOR_ID',
    authors.au_lname AS 'LAST NAME',
    authors.au_fname AS 'FIRST NAME',
    COALESCE(SUM(sales.qty),0) AS 'TOTAL'
FROM my_lab.authors
LEFT JOIN titleauthor
	ON authors.au_id = titleauthor.au_id
LEFT JOIN titles
	ON titleauthor.title_id = titles.title_id 
LEFT JOIN sales
	ON titles.title_id = sales.title_id
GROUP BY AUTHOR_ID
ORDER BY TOTAL DESC
LIMIT 23;