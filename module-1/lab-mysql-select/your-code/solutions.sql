-- CHALLENGE 1
select au.au_id as 'AUTHOR ID', au.au_lname as 'LAST NAME', au.au_fname as 'FIRST NAME', ti.title as 'TITLE', pu.pub_name as 'PUBLISHER'
from authors as au
	join titleauthor as ta
		on ta.au_id = au.au_id
	join titles as ti
		on ti.title_id = ta.title_id
	join publishers as pu
		on pu.pub_id = ti.pub_id;

-- CHALLENGE 2
select au.au_id as AUTHOR_ID, au.au_lname as 'LAST NAME', au.au_fname as 'FIRST NAME', pu.pub_name as PUBLISHER, COUNT(ti.title) AS 'TITLE COUNT'
from authors as au
	join titleauthor as ta
		on ta.au_id = au.au_id
	join titles as ti
		on ti.title_id = ta.title_id
	join publishers as pu
		on pu.pub_id = ti.pub_id
group by AUTHOR_ID, PUBLISHER; 

-- CHALLENGE 3

select au.au_id as AUTHOR_ID, au.au_lname as 'LAST NAME', au.au_fname as 'FIRST NAME', SUM(sa.qty) AS 'TOTAL'
from authors as au
	join titleauthor as ta
		on ta.au_id = au.au_id
	join titles as ti
		on ti.title_id = ta.title_id
	join sales as sa
		on sa.title_id = ti.title_id
group by AUTHOR_ID 
Order by TOTAL desc
limit 3;

-- CHALLENGE 4

select au.au_id as AUTHOR_ID, au.au_lname as 'LAST NAME', au.au_fname as 'FIRST NAME', coalesce(SUM(sa.qty), 0) AS 'TOTAL'
from authors as au
	left join titleauthor as ta
		on ta.au_id = au.au_id
	left join titles as ti
		on ti.title_id = ta.title_id
	left join sales as sa
		on sa.title_id = ti.title_id
group by AUTHOR_ID 
Order by TOTAL desc;

-- BONUS CHALLENGE

select au.au_id as AUTHOR_ID, au.au_lname as 'LAST NAME', au.au_fname as 'FIRST NAME', sum((ti.advance + (ti.price * sa.qty * ti.royalty/100))*ta.royaltyper/100) as 'PROFIT'
from authors as au
	join titleauthor as ta
		on ta.au_id = au.au_id
	join titles as ti
		on ti.title_id = ta.title_id
	join sales as sa
		on sa.title_id = ti.title_id
group by AUTHOR_ID 
Order by PROFIT desc
limit 3;
