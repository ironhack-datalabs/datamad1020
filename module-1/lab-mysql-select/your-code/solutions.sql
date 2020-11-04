SELECT authors.au_id AS AUTHOR_ID, au_lname AS 'LAST NAME', au_fname AS 'FIRST NAME', titles.title AS TITLE, publishers.pub_name AS PUBLISHER
FROM authors
    JOIN titleauthor
		ON authors.au_id = titleauthor.au_id
    JOIN titles
		ON titleauthor.title_id = titles.title_id
	JOIN publishers
		ON titles.pub_id = publishers.pub_id;
        
---------------------

SELECT authors.au_id AS AUTHOR_ID, au_lname AS 'LAST NAME', au_fname AS 'FIRST NAME', COUNT(titles.title) AS 'TITLE COUNT', publishers.pub_name AS PUBLISHER
FROM authors
    JOIN titleauthor
		ON authors.au_id = titleauthor.au_id
    JOIN titles
		ON titleauthor.title_id = titles.title_id
	JOIN publishers
		ON titles.pub_id = publishers.pub_id
	GROUP BY title WITH ROLLUP;

        
