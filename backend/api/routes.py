from flask import request, jsonify, Response
from api import app, db
from api.models import Meme

memes=[]
id=1

@app.route('/memes', methods=['POST'])
def postMeme():
    memeData = request.get_json() or {}
    newName = memeData['name']
    newCaption = memeData['caption']
    newUrl = memeData['url']
    status = Meme.query.filter_by(name=newName, caption=newCaption, url=newUrl).first()
    if status is not None:
        return Response(status=409)
    newMeme = Meme(name = memeData['name'], caption = memeData['caption'], url = memeData['url'])
    db.session.add(newMeme)
    db.session.commit()
    newMeme = Meme.query.filter_by(name = memeData['name'], caption = memeData['caption'], url = memeData['url']).first()
    d={'id':newMeme.id}
    return d

@app.route('/memes', methods=['GET'])
def getAllMemes():
    allMemesData=Meme.query.all()
    memes = []
    for meme in allMemesData:
        memes.append(meme.memeToJson())
    return jsonify(memes[-100:])

@app.route('/memes/<id>', methods=['GET'])
def getMemeWithId(id):
    reqMeme = Meme.query.get(id)
    if reqMeme is None:
        return Response(status=404)
    else: 
        return reqMeme.memeToJson()
        
@app.route('/memes/<id>', methods=['PATCH'])
def updateMemeWithId(id):
    reqMeme = Meme.query.get(id)
    newMemeData = request.get_json() or {}
    newUrl = newMemeData['url'] if 'url' in newMemeData else reqMeme.url
    newCaption = newMemeData['caption'] if 'caption' in newMemeData else reqMeme.caption
    result = db.session.query(Meme).filter(Meme.id==id).update({Meme.url: newUrl, Meme.caption: newCaption}, synchronize_session = False)
    if result == 0:
        return Response(status=404)
    db.session.commit()
    return Response(status=200)