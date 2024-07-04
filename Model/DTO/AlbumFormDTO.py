
class AlbumFormDTO():
    def __init__(self, album_name: str, image: str, musical_pices: list) -> None:
        self.album_name = album_name
        self.image = image
        self.musical_pieces = musical_pices
        
    @property
    def album_name(self):
        return self._album_name

    @album_name.setter
    def album_name(self, value):
        self._album_name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def musical_pieces(self):
        return self._musical_pieces

    @musical_pieces.setter
    def musical_pieces(self, value):
        self._musical_pieces = value