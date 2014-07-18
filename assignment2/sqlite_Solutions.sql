-- Assignment 2, Problem 1, Part a
select count(*)
from (
     select * from frequency     
     where docid = '10398_txt_earn'     
) x

-- Assignment 2, Problem 1, Part b
select count(*)
from (
     select * from frequency     
     where docid = '10398_txt_earn'     
     and count = 1
) x

-- Assignment 2, Problem 1, Part c
select count(*)
from (
     select term from frequency     
     where docid = '10398_txt_earn'     
     and count = 1     
     UNION
     select term from frequency     
     where docid = '925_txt_trade'     
     and count = 1
) x

-- Assignment 2, Problem 1, Part d
select count(*)
from (
     select * from frequency     
     where term = 'parliament'
) x

-- Assignment 2, Problem 1, Part e
select count(*) from (
	select a.docid, a.count from frequency as a, frequency as b
	where a.docid = b.docid
	group by a.term
	having sum(a.count) >= 300)
select count(*) from docs_total where docsum >= 300 order by docsum desc;

-- Assignment 2, Problem 1, Part f
select count(*) from
	(select * from frequency
	where frequency.term = 'transactions'
	union
	select * from frequency
	where frequency.term = 'world')


-- Assignment 2, Problem 2, Part g
-- matrix.db
select a.row_num, b.col_num, sum(a.value * b.value)
from a
join b on b.row_num = a.col_num
where a.row_num = 2
and b.col_num = 3


-- Assignment 2, Problem 3, Part h
-- reuters.db
select a.docid, b.term, sum(a.count * b.count)
from frequency as a
join frequency as b on b.term = a.term
where a.docid = '10080_txt_crude'
and b.docid = '17035_txt_earn'

-- Assignment 2, Problem 3, Part i
-- reuters.db
select * from frequency
union
select 'q' as docid, 'washington' as term, 1 as count
union
select 'q' as docid, 'taxes' as term, 1 as count
union
select 'q' as docid, 'treasury' as term, 1 as count