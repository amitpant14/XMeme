from api import db

class Meme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    caption = db.Column(db.String(1000))
    url = db.Column(db.String(1000))

    # method to convert a meme data to json and return it when asked for
    def memeToJson(self):
        data = {
            'id': self.id,
            'name': self.name,
            'caption': self.caption,
            'url': self.url
        }
        return data