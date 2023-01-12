from functools import wraps
from models import Meme, UserMeme, meme_schema, meme_schemas, db
from flask import jsonify, request, Blueprint

api = Blueprint('api', __name__, url_prefix='/api' )


@api.route('/add-meme-template', methods=['POST'])
def add_meme_template():
    id = request.json['id']
    meme_url = request.json['meme_url']
    meme = Meme(id, meme_url)
    db.session.add(meme)
    db.session.commit()
    return jsonify({'message': 'meme added'}) 

@api.route('/get-meme-templates', methods=['GET'])
def get_meme_templates():
    memes = Meme.query.all()
    output = meme_schemas.dump(memes)
    print(output)
    return jsonify(output)

""" @api.route('/change-id/<id>', methods=['POST'])
def update_id(id):
    meme = Meme.query.filter_by(id = id).first()
    meme.id = request.json['id']
    db.session.commit()
    return jsonify({"message": 'updated'}) """

@api.route('get-meme-template/<id>', methods=['GET'])
def get_meme_template(id):
    meme = Meme.query.filter_by(id = id).first()
    output = meme_schema.dump(meme)
    if meme:
        return jsonify(output)
    else:
        return jsonify({'message': 'no meme was found with this id'})


@api.route('/add-meme', methods=['POST'])
def add_meme():
    if 1 == 1:
        new_text = request.json['inputs']
        new_positioning = request.json['positioning']
       #print(new_positioning)
        current_text = []
        current_positioning = []

        for index in range(4):
            try:
                if new_text[index]:
                    current_text.append(new_text[index])
                    #print(current_text)
            except:
                current_text.append(None)
                #print(current_text)

        for index in range(4):
            try:
                if new_positioning[index]:
                    print(new_positioning[index])
                    current_positioning.append(new_positioning[index])
            except:
                current_positioning.append(None)
        print(current_text)
        meme_template = request.json['memeId']
        meme_url = request.json['memeURL']
        user_token = request.json['token']
        user_input1 = current_text[0]
        user_input2 = current_text[1]
        user_input3 = current_text[2]
        user_input4 = current_text[3]
        input1_positioning = current_positioning[0]
        input2_positioning = current_positioning[1]
        input3_positioning = current_positioning[2]
        input4_positioning = current_positioning[3]
        user_meme = UserMeme(meme_template, meme_url, user_token, user_input1, user_input2, user_input3, user_input4, input1_positioning, input2_positioning, input3_positioning, input4_positioning)
        db.session.add(user_meme)
        db.session.commit()
        print(input1_positioning)
        print(input1_positioning['percentageFromLeft'])
        print(input1_positioning['percentageFromTop'])
        output = meme_schema.dump(user_meme)
        return jsonify(output)
    else:
        print('failed')
        return jsonify({'message': 'failed'})
    

@api.route('/view-my-memes', methods=['GET', 'POST'])
def view_my_memes():
    token = request.json['token']
    memes = UserMeme.query.filter_by(user_token = token).all()
    if memes:
        output = meme_schemas.dump(memes)
        return jsonify(output)
    else:
        return jsonify({'message': 'No memes found'})

@api.route('/view-meme/<id>', methods=['POST'])
def view_meme(id):
    token = request.json['token']
    meme = UserMeme.query.filter_by(id = id, user_token = token).first()
    if meme:
        output = meme_schema.dump(meme)
        if meme.user_token == token:
            return jsonify(output)
        else:
            return jsonify({'isUserMeme': 'false'})
    else:
        return jsonify({'message': 'No meme was found'})

@api.route('/update-meme/<id>', methods=['PATCH'])
def update_meme(id):
    token = request.json['token']
    meme = UserMeme.query.filter_by(id = id).first()
    if meme:
        output = meme_schema.dump(meme)
        print(output)
        if meme.user_token == token:
            new_text = request.json['inputs']
            new_positioning = request.json['positioning']
            current_text = [meme.user_input1, meme.user_input2, meme.user_input3, meme.user_input4]
            current_positioning = [meme.input1_positioning, meme.input2_positioning, meme.input3_positioning, meme.input4_positioning]
            for index in range(4):
                try: 
                    if new_text[index]:
                        print(index)
                        current_text[index] = new_text[index]
                except:
                    print(index)
                    current_text[index] = None

            for index in range(4):
                try:
                    if new_positioning[index]:
                        current_positioning[index] = new_positioning[index]
                except:
                    current_positioning[index] = None
            meme.user_input1 = current_text[0]
            meme.user_input2 = current_text[1]
            meme.user_input3 = current_text[2]
            meme.user_input4 = current_text[3]
            meme.input1_positioning = current_positioning[0]
            meme.input2_positioning = current_positioning[1]
            meme.input3_positioning = current_positioning[2]
            meme.input4_positioning = current_positioning[3]
            db.session.commit()
            return jsonify(output, {'message': 'Update successful'})
        else:
            return jsonify({'message': 'You do not have permission to change this meme'})
    else:
        return jsonify({'message': 'No meme found'})

@api.route('/delete-meme/<id>', methods=['POST', 'DELETE'])
def delete_meme(id):
    token = request.json['token']
    meme = UserMeme.query.filter_by(id = id).first()
    if meme:
        if meme.user_token == token:
            db.session.delete(meme)
            db.session.commit()
            return jsonify({'message': 'Meme deleted'})
        else:
            return jsonify({'message': 'You do not have permission to delete this meme'})
    else:
        return jsonify({'message': 'No meme found'})