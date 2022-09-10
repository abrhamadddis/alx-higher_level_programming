-- A script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT name
  FROM tv_genres AS g
       INNER JOIN tv_show_genres AS sg
       ON g.id = sg.genre_id
       INNER JOIN tv_shows AS s
       ON sg.show_id = s.id
       WHERE g.name NOT IN
             (SELECT name
				FROM tv_genres AS g
				     INNER JOIN tv_show_genres AS sg
					 ON g.id = sg.genre_id
					 INNER JOIN tv_shows AS s
					 ON sg.show_id = s.id
					 WHERE s.title = "Dexter")
ORDER BY g.name;