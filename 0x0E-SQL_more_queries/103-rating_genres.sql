-- A script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT name, SUM(rate) AS rating
  FROM tv_genres AS g
       INNER JOIN tv_show_genres AS sg
	   ON sg.genre_id = g.id
	   INNER JOIN tv_show_ratings AS sr
	   ON sr.show_id = sg.show_id
GROUP BY name
ORDER BY rating DESC;