from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hallo saya Berthy</h1> <p>Ini adalah tampilan default flask.</p>'''


# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request

    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    direct = "/home/berthyanggowo/mysite"
    # cv2.imshow("frame", img)
    cv2.imwrite("/home/berthyanggowo/mysite/car_save.jpg", img)
    cv2.waitKey(0)

    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)



    return Response(response=response_pickled, status=200, mimetype="application/json")


