#!/usr/bin/python

from flask import Flask,request
import subprocess

app = Flask(__name__)
@app.route("/deny")
def run_command():
    command = request.args.get('ip')
    # ufw deny from <Remote-IP> to <Local-IP> proto <Protocol> port <Port Number>
    command= f"command : ufw deny from {command} to any"
    print(command)
    output = subprocess.check_output(command,shell=True)
    return output

if __name__ =="__main__":
    app.run(host="0.0.0.0",port=8000)