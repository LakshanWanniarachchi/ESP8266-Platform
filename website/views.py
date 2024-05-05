from flask import  render_template, request , Blueprint ,jsonify 

import requests
from flask_socketio import SocketIO 




views = Blueprint('views' ,__name__)

socketio = SocketIO()

@views.route('/')
def index():
    return render_template('home.html')

@views.route('/send_command', methods=['POST'])
def send_command():
    
    
    nodemcu_address = "192.168.8.158"
    nodemcu_port = 80 # Default HTTP port
    
    
    if request.method == 'POST':
        
        
     button = request.form.get("btn")
     
     if button == "on" :
    
          url = f"http://{nodemcu_address}:{nodemcu_port}/command"  # URL of NodeMCU endpoint
          response = requests.post(url, data={'command':"on"})
          print(response.text)
          socketio.emit('message', response.text)

          if response.status_code == 200:
           return "Command sent successfully"
          else:
           return "Failed to send command"
    
     else:
        
          url = f"http://{nodemcu_address}:{nodemcu_port}/command"  # URL of NodeMCU endpoint
          response = requests.post(url, data={'command':"off"})
          
          socketio.emit('message', response.text)
    
          if response.status_code == 200:
           return "Command sent successfully"
          else:
           return "Failed to send command"
          


@views.route('/get_data', methods=['POST'])
def get_data():
    
    if request.method=="POST":
        
        data = request.get_json()
        
        socketio.emit('message', data["Data"])
        
        return jsonify({"status": "success", "message": "Data received successfully"}), 200
        
        

        
        
@socketio.on('connect')
def handle_connect():
    print("NodeMCU connected")

@socketio.on('message')
def handle_message(message):
    print("Received message from NodeMCU:", message)
    socketio.emit('message', message)
    
    
