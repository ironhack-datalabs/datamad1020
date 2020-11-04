

-- CHALLENGE 1


CREATE TABLE mitabla(
SELECT au_id, au_lname, au_fname  FROM authors AS a
JOIN titleauthor AS t USING(au_id));


CREATE TABLE challenge(
SELECT * FROM bookstore.titles
JOIN mitabla USING (title_id));

CREATE TABLE challenge1(
SELECT * FROM bookstore.publishers
JOIN challenge USING (pub_id));

SELECT * FROM bookstore.challenge1;
ALTER TABLE challenge1
 DROP pub_id,
 DROP city,
 DROP state,
 DROP country,
 DROP title_id,
 DROP type,
 DROP price,
 DROP advance,
 DROP royalty,
 DROP ytd_sales,
 DROP  notes,
 DROP pubdate,
 DROP au_ord,
 DROP royaltyper;

-- APARECEN ALGUNOS LIBROS DUPLICADOS (NO SÉ EL MOTIVO) ASÍ QUE HE UTILIZADO :

SELECT DISTINCT* FROM bookstore.challenge1;



--CHALLENGE 2
SELECT AUTHOR_ID, LAST_NAME, FIRST_NAME, PUBLISHER ,
COUNT(DISTINCT title) AS `TITLE COUNT`
FROM challenge1
GROUP BY AUTHOR_ID, PUBLISHER ;



--CHALLENGE3

SELECT au_id AS AUTHOR_ID, au_fname AS FIRST_NAME, au_lname AS LAST_NAME, SUM(ytd_sales) AS TOTAL
FROM bookstore.challenge
GROUP BY (au_id)
ORDER BY TOTAL DESC
LIMIT 3 ;


-- CHALLENGE4

SELECT au_id AS AUTHOR_ID, au_fname AS FIRST_NAME, au_lname AS LAST_NAME, SUM(IFNULL(ytd_sales,0)) AS TOTAL
FROM bookstore.challenge
GROUP BY (au_id)
ORDER BY TOTAL DESC;