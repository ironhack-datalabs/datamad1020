
-- Challenge 1 - Who Have Published What At Where? --

SELECT authors.au_id AS "AUTHOR ID", au_lname AS "LAST NAME", au_fname AS "FIRST NAME", title AS "TITLE", pub_name AS "PUBLISHER"
FROM authors 
	JOIN titleauthor
		ON authors.au_id =  titleauthor.au_id
	JOIN titles
		ON titleauthor.title_id = titles.title_id
	JOIN publishers
		ON titles.pub_id = publishers.pub_id;
	
-- Challenge 2 - Who Have Published How Many At Where? --

SELECT authors.au_id AS "AUTHOR ID", au_lname AS "LAST NAME", au_fname AS "FIRST NAME", pub_name AS "PUBLISHER" COUNT (titles.title) AS "TITLE COUNT";
FROM authors 
	JOIN titleauthor
		ON authors.au_id =  titleauthor.au_id
	JOIN titles
		ON titleauthor.title_id = titles.title_id

