-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked

select * from tv_show_genres;

select * from tv_shows;

SELECT
    tv_shows.title,
    tv_show_genres.genre_id
from tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;