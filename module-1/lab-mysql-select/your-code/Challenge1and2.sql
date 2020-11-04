-- CHALLENGE 1 --
SELECT au.au_id AS AuthorID, au_lname AS Last_Name, au_fname AS First_Name, pub_name AS Publisher
FROM authors AS au
	JOIN titleauthor AS tau
		ON au.au_id = tau.au_id
	JOIN titles AS t
		ON t.title_id = tau.title_id
	JOIN publishers AS p
		ON p.pub_id = t.pub_id;
        
-- CHALLENGE 2 --
SELECT au.au_id AS AuthorID, au_lname AS Last_Name, au_fname AS First_Name, pub_name AS Publisher, au_ord AS Title_Count
FROM authors AS au
	JOIN titleauthor AS tau
		ON au.au_id = tau.au_id
	JOIN titles AS t
		ON t.title_id = tau.title_id
	JOIN publishers AS p
		ON p.pub_id = t.pub_id;

-- 1. To check if it has been done correctly we sum the column Title-Count

-- Nose porque la sum solo me funciona la primera vez que le doy al rayo... si quiero que me repita la suma le tengo que cambiar el nombre, en esta caso 'in_order'
-- por cualquier otro y me lo haria... Nose porque solo funciona la primera vez

-- Además, al darme error continuo con el Challenge 3 en otro sql porque sino no me deja correrlo

CREATE TEMPORARY TABLE in_order

SELECT au.au_id AS AuthorID, au_lname AS Last_Name, au_fname AS First_Name, pub_name AS Publisher, au_ord AS Title_Count
FROM authors AS au
	JOIN titleauthor AS tau
		ON au.au_id = tau.au_id
	JOIN titles AS t
		ON t.title_id = tau.title_id
	JOIN publishers AS p
		ON p.pub_id = t.pub_id;
        
SELECT SUM(Title_count) AS Total FROM in_order;
-- Con la suma el resultado seria 34





