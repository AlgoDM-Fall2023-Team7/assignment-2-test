 -- change data to give a slight upward trend and a day of week effect
update daily_impressions
set impression_count=((CASE WHEN dayname(day) IN ('Sat', 'Sun') THEN 0.7
                            WHEN dayname(day)='Fri' THEN 0.9
                            ELSE 1
                        END)*
                     (impression_count+(DATEDIFF(day, '{date_param}'::timestamp, 
                      day)*120)));