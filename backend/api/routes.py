from flask import request, jsonify, Response
from api import app, db
from api.models import Meme
import json
import validators
import mimetypes

#function to validate name
def isValidName(name):
    if type(name) != type("") or name == '':
        return False
    return True

#function to validate caption
def isValidCaption(caption):
    if type(caption) != type("") or caption == '':
        return False
    return True

#function to validate a url
def isValidUrl(url):
    mimetype,encoding = mimetypes.guess_type(url)
    return (mimetype and mimetype.startswith('image'))

# endpoint to post a meme 
@app.route('/memes', methods=['POST'])
def postMeme():
    # getting the json data from the request
    memeData = request.get_json() or {}
    reqParams = ['name', 'caption', 'url']
    # if request contains invalid parameters or
    # all required parameters are not obtained, return bad request error
    if len(memeData) != 3:
        return Response(status=400)
    for key in memeData:
        if key not in reqParams:
            return Response(status=400)
    newName = memeData['name'].strip()
    newCaption = memeData['caption'].strip()
    newUrl = memeData['url'].strip()
    # check if name and caption are invalid
    if not (isValidName(newName) and isValidCaption(newCaption) and isValidUrl(newUrl)):
        return Response(status=400)
    # if url is invalid, return BAD REQUEST response
    # checking if the record already exists in the database
    status = Meme.query.filter_by(name=newName, caption=newCaption, url=newUrl).first()
    # if already present, returning 409 - CONFLICT response code
    if status is not None:
        return Response(status=409)
    # updating the database with the new meme
    newMeme = Meme(name = newName, caption = newCaption, url = newUrl)
    db.session.add(newMeme)
    db.session.commit()
    # getting the id of the new meme created 
    newMeme = Meme.query.filter_by(name = memeData['name'], caption = memeData['caption'], url = memeData['url']).first()
    d={'id':newMeme.id}
    # returning the id as the json response
    return d

# endpoint to get the latest 100 memes
@app.route('/memes', methods=['GET'])
def getAllMemes():
    # getting all the memes from db and selecting the last 100 from them
    # as they are in order of id, they should be in increasing order of creation time
    allMemesData=Meme.query.all()
    allMemesData = allMemesData[-100:]
    memes = []
    # for each meme, getting its attributes in json format
    # using the method defined in the Meme model
    for meme in allMemesData:
        memes.append(meme.memeToJson())
    return jsonify(memes)

# endpoint to get the json data for a meme with given id
@app.route('/memes/<id>', methods=['GET'])
def getMemeWithId(id):
    # getting the meme with given id
    reqMeme = Meme.query.get(id)
    # if the meme does not exist, returning 404 response code
    if reqMeme is None:
        return Response(status=404)
    # else returning the requested meme data in json format
    return reqMeme.memeToJson()
        
# endpoint to update the url or caption of a particular meme with given id
@app.route('/memes/<id>', methods=['PATCH'])
def updateMemeWithId(id):
    # getting the required meme, if does not exist, returning 404 code
    reqMeme = Meme.query.get(id)
    if reqMeme is None:
        return Response(status=404)
    # getting the json data from PATCH request or setting it to empty dict if no json was found
    newMemeData = request.get_json() or {}
    # getting list of keys present in json request
    allKeys = newMemeData.keys()
    totalKeys = len(allKeys)
    # if keys are 0 or more than two, it is an invalid request
    if totalKeys > 2 or totalKeys == 0:
        return Response(status=400)
    else:
        for key in allKeys:
            # if keys other than url and caption are present, it is an invalid request
            if key != 'url' and key != 'caption':
                return Response(status=400)
    # setting newUrl and newCaption to the new entries that are to be updated, or the previous one if not found
    newUrl = newMemeData['url'].strip() if 'url' in newMemeData else reqMeme.url
    newCaption = newMemeData['caption'].strip() if 'caption' in newMemeData else reqMeme.caption
    # if url is invalid, return BAD REQUEST response
    if not (isValidCaption(newCaption) and isValidUrl(newUrl)):
        return Response(status=400)
    # checking if similar entry is already present, returning conflict error code if True
    similarMeme = Meme.query.filter_by(name=reqMeme.name, caption=newCaption, url=newUrl).first()
    if similarMeme is not None:
        return Response(status=409)
    # updating the meme in the database
    result = db.session.query(Meme).filter(Meme.id==id).update({Meme.url: newUrl, Meme.caption: newCaption}, synchronize_session = False)
    # if the update fails for some reason, it returns 0, in which case a 500 server error code is returned by the application
    if result == 0:
        return Response(status=500)
    db.session.commit()
    # everything goes well, return OK status code
    return Response(status=200)