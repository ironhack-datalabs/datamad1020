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