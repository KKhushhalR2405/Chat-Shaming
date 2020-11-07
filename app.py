from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('main.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    try:
    	if len(json['message'])>5:
	    	print('received my event: ' + str(json))
	    	socketio.emit('my response', json, callback=messageReceived)
	    
    except:
    	print("retrying")
if __name__ == '__main__':
    socketio.run(app, debug=True)