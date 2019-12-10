import socket 
from flask import Flask
app = Flask(__name__)

@app.route('/')
#def hello_world:
#    return 'Hey, we have Flask in a Docker container!'
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 

if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')
