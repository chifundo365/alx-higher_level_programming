-- Lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv_s.title, tv_s_g.genre_id
FROM tv_shows tv_s
LEFT JOIN tv_show_genres tv_s_g
ON tv_s.id = tv_s_g.show_id
WHERE tv_s_g.show_id IS NULL
ORDER BY tv_s.title, tv_s_g.genre_id;
