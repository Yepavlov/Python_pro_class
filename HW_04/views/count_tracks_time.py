from flask import Blueprint, render_template

from HW_04.database_handler import execute_query

count_tracks_time_for_each_album_route = Blueprint(
    "count_tracks_time_for_each_album_route", __name__
)
count_tracks_time_for_all_albums_route = Blueprint(
    "count_tracks_time_for_all_albums_route", __name__
)


@count_tracks_time_for_each_album_route.route("/count_tracks_time")
def get_count_tracks_time_for_each_album():
    query = """SELECT
                    a.AlbumId,
                    a.Title AS AlbumTitle,
                    ROUND(SUM(t.Milliseconds / 3600000.0), 2) AS TotalHours
                FROM
                    tracks t
                LEFT JOIN
                    albums a ON t.AlbumId = a.AlbumId
                GROUP BY
                    a.AlbumId, a.Title
                ORDER BY
                    a.AlbumId;
            """
    result = execute_query(query=query)
    if result:
        return render_template("count_tracks_time.html", album_infos=result)
    else:
        return "There are no required information."


@count_tracks_time_for_all_albums_route.route("/count_all_albums")
def count_tracks_time_for_all_albums():
    query = """
    SELECT
        COUNT(DISTINCT a.AlbumId) AS AlbumCount,
        COUNT(t.TrackId) AS TrackCount,
        ROUND(SUM(t.Milliseconds / 3600000.0), 2) AS TotalHours
    FROM
        tracks t
    LEFT JOIN
        albums a ON t.AlbumId = a.AlbumId;
    """
    result = execute_query(query=query)
    if result:
        album_count = result[0][0]
        track_count = result[0][1]
        total_hours = result[0][2]
        return render_template(
            "count_all_albums.html",
            album_count=album_count,
            track_count=track_count,
            total_hours=total_hours,
        )
    else:
        return "There are no required information."
