-- A script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT DISTINCT title
  FROM tv_shows AS s
		LEFT JOIN tv_show_genres AS sg
       ON sg.show_id = s.id
       LEFT JOIN tv_genres AS g
       ON g.id = sg.genre_id
       WHERE s.title NOT IN
             (SELECT title
				FROM tv_shows AS s
				     INNER JOIN tv_show_genres AS sg
					 ON sg.show_id = s.id
					 INNER JOIN tv_genres AS g
					 ON g.id = sg.genre_id
					 WHERE g.name = "Comedy")
ORDER BY title;