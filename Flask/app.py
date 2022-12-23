from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from engineio.payload import Payload
from aruco_ar import ARUCO_DICT, augmentAruco, readb64
import base64
import cv2

Payload.max_decode_packets = 2048
app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins='*')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/ar', methods=['POST', 'GET'])
def ar():
    return render_template('ar.html')

@app.route("/get_gallery")
def get_gallery():
    return {
    "gallery": [
        {
            "image": "static/gallery_art/cafe_in_paris.jpg",
            "name": "Cafe In Paris",
            "author": "Gan Aik Tong"
        },
        {
            "image": "static/gallery_art/cozy_home.jpg",
            "name": "Cozy Home",
            "author": "Ahmad Zakii Anwar"
        },
        {
            "image": "static/gallery_art/house_in_white.jpg",
            "name": "House in White",
            "author": "Hassan Muthalib"
        },
        {
            "image": "static/gallery_art/national_palace_malaysia.jpg",
            "name": "National Palace Malaysia",
            "author": "Mohamed Zain Idris"
        },
        {
            "image": "static/gallery_art/time_portal.jpg",
            "name": "Time Portal",
            "author": "Syed Ahmad Jamal"
        }
    ]
}

aruco_type = "DICT_6X6_100"
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[aruco_type])
arucoParams = cv2.aruco.DetectorParameters_create()

"""
myList = os.listdir(path)
augDics = {}
for imgPath in myList:
    key = int(os.path.splitext(imgPath)[0])
    imgAug = cv2.imread(f'{path}/{imgPath}')
    augDics[key] = imgAug
"""
path = "Markers"
@socketio.on('image')
def image(data_image):
    frame = (readb64(data_image))
    imgAug = cv2.imread(f'{path}/1.jpg')
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejected = cv2.aruco.detectMarkers(imgGray, arucoDict, parameters=arucoParams)
    if len(corners) !=0:
            for bbox, id in zip(corners, ids):
                frame = augmentAruco(bbox, frame, imgAug)

    imgencode = cv2.imencode('.jpeg', frame,[cv2.IMWRITE_JPEG_QUALITY,40])[1]
    
    # base64 encode
    stringData = base64.b64encode(imgencode).decode('utf-8')
    b64_src = 'data:image/jpeg;base64,'
    stringData = b64_src + stringData

    # emit the frame back
    emit('response_back', stringData)
    
if __name__ == '__main__':
    socketio.run(
        app, 
        port=5000,
        debug=True) 