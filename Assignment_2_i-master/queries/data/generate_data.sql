insert into daily_impressions
select dateadd(day, seq2(1), ('{date_param}'::timestamp)) as day,
abs(round(normal(35000, 7000, random(4)))) as impression_count
from table(generator(rowcount=>{days_param}));