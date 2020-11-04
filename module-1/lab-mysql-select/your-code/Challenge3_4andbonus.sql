-- CHALLENGE 3 --

-- Firstly I join first and last name in one same column, in order to later on display the unique values
SELECT DISTINCT au.au_id AS AuthorID, CONCAT (au_lname,' ', au_fname) AS Full_name, t.title_id AS Title_ID, qty AS Total 
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
ORDER BY Total DESC LIMIT 3; 


-- CHALLENGE 4 --

-- It would be the same as the previouse exercise but, instead of using DESC LIMIT 3, we would only write desc
-- When I display the info, none of the rows have the value 0 for total of published books... so I dont understand what the question meant when it specified to 
-- inlcude those values as welll 

SELECT DISTINCT au.au_id AS AuthorID, CONCAT (au_lname,' ', au_fname) AS Full_name, t.title_id AS Title_ID, qty AS Total 
FROM authors AS au
	JOIN titleauthor AS tau
		ON au.au_id = tau.au_id
	JOIN titles AS t
		ON t.title_id = tau.title_id
	JOIN sales AS s
		ON s.title_id = tau.title_id

ORDER BY Total DESC;


-- BONUS CHALLENGE --

-- Firstly, we know we need the columns; author ID, fullname and profit, hence why we recycle part of the code written for the previous exercise
SELECT DISTINCT au.au_id AS AuthorID, CONCAT (au_lname,' ', au_fname) AS Full_name, advance AS Advance, royalty AS Royalty, (Advance + Royalty) AS Profit
FROM authors AS au
	JOIN titleauthor AS tau
		ON au.au_id = tau.au_id
	JOIN titles AS t
		ON t.title_id = tau.title_id
	
ORDER BY Profit DESC LIMIT 3;
-- we add the code so we can create a new column named profit, by summing the columns Advance and Royalty
-- Once we have the column Profit we sort them in descending order so the biggest number is on top, therefor the author with the most profit
		-- ORDER BY Profit DESC; 
				-- We only need to show the top three thats why we use LIMIT

