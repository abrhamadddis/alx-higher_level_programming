-- A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name
  FROM tv_genres
       INNER JOIN tv_show_genres AS sg
       ON tv_genres.id = sg.genre_id
       INNER JOIN tv_shows AS s
       ON s.id = sg.show_id
       WHERE s.title = "Dexter"
ORDER BY tv_genres.name;