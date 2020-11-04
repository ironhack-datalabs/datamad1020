
-- Challenge 1 - Who Have Published What At Where?--

SELECT authors.au_id, au_lname, au_fname, title, pub_name
FROM authors
	JOIN titleauthor
		ON authors.au_id = titleauthor.au_id
	JOIN titles
		ON titleauthor.title_id= titles.title_id
	JOIN publishers
		ON titles.pub_id = publishers.pub_id;
        
        
-- Challenge 2 --
SELECT authors.au_id, au_lname, au_fname, pub_name, COUNT(titles.title_id)
FROM authors
	JOIN titleauthor
		ON authors.au_id = titleauthor.au_id
	JOIN titles
		ON titleauthor.title_id= titles.title_id
	JOIN publishers
		ON titles.pub_id = publishers.pub_id
GROUP BY authors.au_id, publishers.pub_id;

-- Challenge 3 --
SELECT authors.au_id, au_lname, au_fname, 

    