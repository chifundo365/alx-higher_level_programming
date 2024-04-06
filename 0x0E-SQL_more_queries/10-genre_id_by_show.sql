-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_s.title, tv_s_g.genre_id
FROM tv_show_genres tv_s_g
INNER JOIN tv_shows tv_s
ON tv_s_g.show_id = tv_s.id
ORDER BY 
tv_s.title ASC, tv_s_g.genre_id ASC;
