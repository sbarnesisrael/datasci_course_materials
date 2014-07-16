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
     select * from frequency     
     where docid = '10398_txt_earn'     
     and count = 1     
     UNION
     select * from frequency     
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
select count(*)
from (
     select * from (
            select a.docid, sum(a.count) as docsum from frequency as a, frequency as b     
            where a.docid = b.docid
            group by a.docid     
            order by sum(a.count)
     )
) x


