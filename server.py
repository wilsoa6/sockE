from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')#, methods=['GET'])
def index():
    return render_template('index.html')

@socketio.on('front2back')
def received(data):
	print "(2) received data from front to back " + str(data)
	emit('back2front', data)

if __name__ == '__main__':
    socketio.run(app)