-- CHALLENGE 1

CREATE TEMPORARY TABLE `authors_publisher`
SELECT authors.au_id AS author_id, 
	   authors.au_lname AS last_name, 
       authors.au_fname AS first_name, 
       titles.title AS title,
       publishers.pub_name AS publisher
FROM titleauthor 
	JOIN titles
		ON titles.title_id = titleauthor.title_id
    JOIN authors
		ON authors.au_id = titleauthor.au_id
	JOIN publishers
		ON publishers.pub_id = titles.pub_id;
        
SELECT * FROM authors_publisher;

-- CHALLENGE 2

CREATE TEMPORARY TABLE `title_by_pub`
SELECT author_id, last_name, first_name, publisher,
COUNT(*) AS title_count FROM authors_publisher
GROUP BY author_id, last_name, first_name, publisher;

SELECT SUM(title_count) FROM title_by_pub;

-- CHALLENGE 3 (AQUÍ CON LAS VENTAS ME HE LIADO UN POCO, PRIMERO HE COGIDO QTY DE SALES Y LUEGO HE VITO MÁS RAZONABLE EL YTD_SALES DE TITLES, ESPERO QUE SEA ESO)

CREATE TEMPORARY TABLE `sellers_ranking`
SELECT author_id, last_name, first_name, SUM(titles.ytd_sales) AS total
FROM authors_publisher
	JOIN titles
		ON authors_publisher.title = titles.title
GROUP BY author_id, last_name, first_name;

SELECT * FROM sellers_ranking ORDER BY total DESC LIMIT 3;

-- CHALLENGE 4

CREATE TEMPORARY TABLE `all_authors`
SELECT au_id, au_lname, au_fname FROM authors;

CREATE TEMPORARY TABLE `sellers_ranking_full`
SELECT au_id, au_lname, au_fname, CASE WHEN sellers_ranking.total IS NULL THEN 0 ELSE sellers_ranking.total END AS total
FROM all_authors
LEFT OUTER JOIN sellers_ranking 
	ON sellers_ranking.author_id = all_authors.au_id
ORDER BY total DESC;

-- BONUS 

CREATE TEMPORARY TABLE `auth_publish_ids`
SELECT authors.au_id AS author_id, 
	   authors.au_lname AS last_name, 
       authors.au_fname AS first_name,
       (titles.royalty * titles.ytd_sales) * (titleauthor.royaltyper / 100) AS royalty_ps,
       titles.advance * (titleauthor.royaltyper / 100) AS advance
FROM titleauthor
	JOIN titles
		ON titles.title_id = titleauthor.title_id
    JOIN authors
		ON authors.au_id = titleauthor.au_id;
        
SELECT au_id, au_lname, au_fname, 
	   CASE WHEN SUM(auth_publish_ids.royalty_ps + auth_publish_ids.advance) IS NULL THEN 0 
       ELSE SUM(auth_publish_ids.royalty_ps + auth_publish_ids.advance) END AS profit 
FROM sellers_ranking_full
LEFT OUTER JOIN auth_publish_ids 
	ON auth_publish_ids.author_id = sellers_ranking_full.au_id
GROUP BY au_id, au_lname, au_fname
ORDER BY profit DESC LIMIT 3;




