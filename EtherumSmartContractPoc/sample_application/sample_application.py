# coding=utf-8
from flask import Flask, render_template, request, send_file, jsonify

from flask_qrcode import QRcode

import snapDelivery

app = Flask(__name__)
qrcode = QRcode(app)


@app.route('/')
def index():
    return render_template('sample_application.html')


@app.route('/qrcode', methods=['GET'])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get('data', '')
    image = qrcode("http://localhost:80/confirm")
    
    return render_template("qr_application.html",qr_image= image) 

@app.route("/confirm", methods=['GET'])
def confirm():
    # Create the contract instance with the newly-deployed address
    data = snapDelivery.broadcast_an_delivery_received('Received successfully')
    return render_template("confirm_application.html",response_data= data)



if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80,debug=True)
