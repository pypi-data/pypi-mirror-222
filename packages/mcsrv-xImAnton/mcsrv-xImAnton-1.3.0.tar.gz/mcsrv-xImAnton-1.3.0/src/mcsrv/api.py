from flask import Flask, jsonify

from mcsrv import Server

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/servers")
def get_servers():
    return jsonify([s.id for s in Server.get_registered_servers()])


@app.route("/server/<server_id>/")
def get_server_info(server_id: str):
    server = Server.get_by_id(server_id)
    return jsonify(
        id=server.id,
        ram=server.ram,
        autostarts=server.autostarts,
        running=server.running,
        type=server.launch_method[0],
        port=server.properties.get_value("server-port")
    )
