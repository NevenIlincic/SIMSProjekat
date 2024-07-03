
class GroupFormDTO():
    def __init__(self, name: str, image: str, participants: list) -> None:
        self.name = name
        self.image = image
        self.participants = participants

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self, value):
        self._participants = value