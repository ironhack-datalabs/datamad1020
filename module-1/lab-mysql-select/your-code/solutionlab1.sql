USE solutions;

/*SELECT a.au_id  AS ID,au_lname AS APELLIDO,au_fname AS NOMBRE,
t.title AS TITULO,
p.pub_name AS PUBLICACION
       
FROM authors AS a
JOIN titleauthor AS tl
ON a.au_id = tl.au_id
JOIN titles AS t
ON t.title_id = tl.title_id
JOIN publishers AS p
ON  p.pub_id = t.pub_id
;
*/
/*SELECT a.au_id AS ID,au_lname AS APELLIDO,au_fname AS NOMBRE,
p.pub_name AS PUBLICACION,
count(t.title)
FROM authors AS a
JOIN titleauthor AS tl
ON a.au_id = tl.au_id
JOIN titles AS t
ON t.title_id = tl.title_id
JOIN publishers AS p
ON  p.pub_id = t.pub_id
GROUP BY t.title 
;
*/
/*SELECT a.au_id AS 'AUTOR ID',au_lname AS 'APELLIDO',au_fname AS 'NOMBRE',
       SUM(s.qty)
FROM authors AS a
JOIN titleauthor AS tl
ON a.au_id = tl.au_id
JOIN sales AS s
ON s.title_id = tl.title_id
JOIN titles AS t
ON s.title_id = t.title_id
GROUP BY s.qty
ORDER BY s.qty DESC
LIMIT 3;
*/

































;








		