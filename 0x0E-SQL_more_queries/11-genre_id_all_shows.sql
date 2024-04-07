-- Lists all shows contained in database `hbtn_0d_tvshows` even if the show does not have a genre
SELECT 	tv_s.title, tv_s_g.genre_id
FROM tv_shows tv_s
LEFT JOIN tv_show_genres tv_s_g
ON tv_s.id = tv_s_g.show_id
ORDER BY tv_s.title, tv_s_g.genre_id;
