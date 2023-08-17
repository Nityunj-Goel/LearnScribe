from flask import Flask, render_template, request, jsonify
from llm import load_and_vectorize, chatbot_response

# Don't forget about OpenAI api key
vid_index = None

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText, vid_index)


@app.route('/send-url', methods=['POST'])
def receive_url():
    try:
        data = request.json
        url = data['url']

        # Process the URL as needed
        global vid_index
        vid_index = load_and_vectorize(url)

        response = {'message': 'URL received successfully'}
        return jsonify(response), 200
    except Exception as e:
        response = {'error': 'An error occurred'}
        return jsonify(response), 500

if __name__ == "__main__":
    app.run()