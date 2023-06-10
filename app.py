from flask import Flask, jsonify, request, Response
from repository import add_conversation, add_message, get_messages_from_db, get_conversations_from_db
from email_summarize import summarize_thread

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({
        'greeting': 'Hello World!'
    })


@app.route('/conversations/', methods=['POST'])
def create_conversation():
    data = request.get_json()
    try:
        user_id = data['user_id']
        if user_id:
            print(user_id)
            data = add_conversation(user_id)
            return jsonify(data), 201
    except Exception as e:
        print(e)
        return Response('''{"message": "Bad Request"}''', status=400, mimetype='application/json')


@app.route('/messages/', methods=['POST'])
def create_message():
    data = request.get_json()
    try:
        conversation_id = data['conversation_id']
        user_id = data['user_id']
        message_text = data['message_text']
        if conversation_id and user_id and message_text:
            data = add_message(conversation_id, user_id, message_text)
            return jsonify(data), 201
    except Exception as e:
        print(e)
        return Response('''{"message": "Bad Request"}''', status=400, mimetype='application/json')


# get all conversations for a user
@app.route('/conversations/<user_id>', methods=['GET'])
def get_conversations(user_id):
    try:
        data = get_conversations_from_db(user_id)
        return jsonify(data), 201
    except Exception as e:
        print(e)
        return Response('''{"message": "Bad Request"}''', status=400, mimetype='application/json')


# get all messages from a conversation
@app.route('/messages/<conversation_id>', methods=['GET'])
def get_messages(conversation_id):
    try:
        data = get_messages_from_db(conversation_id)
        return jsonify(data), 201
    except Exception as e:
        print(e)
        return Response('''{"message": "Bad Request"}''', status=400, mimetype='application/json')


@app.route('/emails/', methods=['POST'])
def create_summary():
    data = request.get_json()
    try:
        thread_id = data['thread_id']
        if thread_id:
            data = summarize_thread(thread_id)
            return jsonify(data), 201
    except Exception as e:
        print(e)
        return Response('''{"message": "Bad Request"}''', status=400, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
