class Painting:
    museum = "the Louvre"

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year


artwork = Painting(input(), input(), int(input()))


print(f'"{artwork.title}" by {artwork.painter} ({artwork.year}) hangs in {Painting.museum}.')

