-- A script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- import the data_dump.sql
SELECT s.title, g.genre_id
  FROM tv_shows AS s
       INNER JOIN tv_show_genres AS g
       ON s.id = g.genre_id
ORDER BY s.title, g.genre_id;