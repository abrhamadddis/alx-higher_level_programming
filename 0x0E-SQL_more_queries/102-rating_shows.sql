-- A script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- import dump_data2.sql
SELECT title, SUM(rate) AS rating
  FROM tv_shows AS s
       INNER JOIN tv_show_ratings AS sr
       ON s.id = sr.show_id
GROUP BY title
ORDER BY rating DESC;