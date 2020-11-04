--  Calculate the royalties of each sales for each author
USE lab_advanced;
CREATE TEMPORARY TABLE roy
SELECT a.au_id, t.title_id, (t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) AS sales_royalty
FROM lab_advanced.titles as t
	 JOIN lab_advanced.titleauthor AS ta
		ON ta.title_id = t.title_id
	 JOIN lab_advanced.authors AS a
		ON ta.au_id = a.au_id
	 JOIN lab_advanced.publishers AS p
		ON t.pub_id = p.pub_id    
	 JOIN lab_advanced.sales AS s
		ON t.title_id = s.title_id;

-- Aggregate the total royalties for each title for each author        
CREATE TEMPORARY TABLE sum_roy
SELECT au_id as a_id, title_id, SUM(sales_royalty) AS royal FROM roy
GROUP BY a_id, title_id;

-- Calculate the advance profits of each author
CREATE TEMPORARY TABLE adv
SELECT a.au_id, SUM(t.advance) as adv_p    
FROM lab_advanced.titles as t
			JOIN lab_advanced.titleauthor AS ta
				ON ta.title_id = t.title_id
			JOIN lab_advanced.authors AS a
				ON ta.au_id = a.au_id
			JOIN lab_advanced.publishers AS p
				ON t.pub_id = p.pub_id 
GROUP BY a.au_id, p.pub_name;


-- Calculate the total (advance and royalties) profits of each author
SELECT au.au_id, au.au_lname, au.au_fname, a.adv_p +  r.royal AS porfit
FROM adv AS a
	JOIN sum_roy AS r
		ON a.au_id = r.a_id
	JOIN lab_advanced.authors AS au
		ON a.au_id = au.au_id
ORDER BY porfit DESC;

-- Create permanent table
CREATE TEMPORARY TABLE porfits
SELECT au.au_id, au.au_lname, au.au_fname, a.adv_p +  r.royal AS porfit
FROM adv AS a
	JOIN sum_roy AS r
		ON a.au_id = r.a_id
	JOIN lab_advanced.authors AS au
		ON a.au_id = au.au_id
ORDER BY porfit DESC;

CREATE TABLE author_porfits
  AS (SELECT * FROM porfits);
