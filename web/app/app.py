from flask import Flask, jsonify
import socket
import psutil
app=Flask(__name__)
@app.route('/info')
def sys_check():
    return jsonify({
        'hostname': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname()),
        'cpu_system_usage': psutil.cpu_percent(interval=1),
        'memory_usage':psutil.virtual_memory().percent
        })
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
