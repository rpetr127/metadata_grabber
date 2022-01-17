from sqlite_utils import Database

db = Database('metadata_grabber/assets/metadata.db', check_same_thread=False)
table = db['radiometadata']
# class Stream(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(30), unique=True)
#     logo = db.Column(db.String(100), unique=False)
#     url = db.Column(db.String(100), unique=True)
#
#     def __init__(self):
#         self.title = title
#         self.logo = logo
#         self.url = url
