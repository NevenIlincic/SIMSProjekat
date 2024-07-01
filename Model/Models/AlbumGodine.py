from Model.Models.Album import Album

class AlbumGodine:
    def __init__(self, godina: int, glasovi_urednika: dict[Album, int], glasovi_korisnika: dict[Album, int], album_urednika: Album, album_korisnika: Album, korisnici: list, muzicki_urednici: list):
        self.godina = godina
        self.glasovi_urednika = glasovi_urednika
        self.glasovi_korisnika = glasovi_korisnika
        self.album_urednika = album_urednika
        self.album_korisnika = album_korisnika
        self.korisnici = korisnici
        self.muzicki_urednici = muzicki_urednici