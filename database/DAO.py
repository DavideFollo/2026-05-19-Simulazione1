from database.DB_connect import DBConnect
from model.artist import Artist
from model.genre import Genre


class DAO():


    def getAllGenre(self):
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM genre"
        cursor.execute(query)

        for row in cursor:
            result[row["GenreId"]]= Genre(row["GenreId"], row["Name"])

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllNodes(genere):

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select ar.ArtistId , ar.Name 
                from track t ,genre g, album a, artist ar
                where g.GenreId =t.GenreId and a.AlbumId = t.AlbumId and
                a.ArtistId  = ar.ArtistId and t.GenreId = %s
                group by ar.ArtistId , ar.Name """
        cursor.execute(query, (genere,))

        for row in cursor:
            result.append(Artist(**row))

        cursor.close()
        conn.close()
        return result



