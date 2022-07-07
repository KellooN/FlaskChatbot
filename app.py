from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot',methods=('POST','GET'))
def chatbot():
    req = request.get_json(force=True)
    print(req)
    # return jsonify(fulfillmentText = 'Chatbot 접속 성공')
    return jsonify(fulfillment_messages=[
        {
          "payload": {
            "richContent": [
              [
                {
                  "type": "image",
                  "rawUrl": "https://cdn-icons-png.flaticon.com/512/5632/5632307.png",
                  "accessibilityText": "Example logo"
                },
                  {
                      "type": "info",
                      "title": "피자메뉴",
                      "subtitle": "z",
                      "actionLink": "https://notion.so/kelloon"
                  }
              ],
                [
                    {
                        "type": "image",
                        "rawUrl": "https://cdn-icons-png.flaticon.com/512/5632/5632307.png",
                        "accessibilityText": "Example logo"
                    },
                    {
                        "type": "info",
                        "title": "피자메뉴",
                        "subtitle": "z",
                        "actionLink": "https://notion.so/kelloon"
                    }
                ]
            ]
          }
        }
      ]
    )
if __name__=='__main__':
    app.run('0.0.0.0',port=5008, debug=True)