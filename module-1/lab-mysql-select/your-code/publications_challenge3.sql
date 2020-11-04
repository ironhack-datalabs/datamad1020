-- CHALLENGE 3 --

-- Firstly I join first and last name in one same column, in order to later on display the unique values
SELECT DISTINCT au.au_id AS AuthorID, CONCAT (au_lname,' ', au_fname) AS Full_name, t.title_id AS Title_ID, qty AS Quantity 
FROM authors AS au
	JOIN titleauthor AS tau
		ON au.au_id = tau.au_id
-- Up to here there are only unique values for authors and their ID,
-- But we need to add columns and join tables in order to see the quantity sold by each author ID
	JOIN titles AS t
		ON t.title_id = tau.title_id
	JOIN sales AS s
		ON s.title_id = tau.title_id
-- Here we display the info in the column quantity from biggest to smallest
-- ORDER BY Quantity DESC   
-- In order to only display the top three we do the following
ORDER BY Quantity DESC LIMIT 3; 
