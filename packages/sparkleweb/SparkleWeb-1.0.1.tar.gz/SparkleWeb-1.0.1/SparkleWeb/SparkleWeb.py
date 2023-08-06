from flask import jsonify, render_template, request, render_template_string, Flask, Blueprint
from flask_cors import CORS
import json
import requests
import os

class Server():
    def __init__(self) -> None:
        root_directory = os.getcwd()
        self.app = Flask(__name__, template_folder=os.path.join(root_directory, "templates"), static_folder=os.path.join(root_directory, "static"))
        CORS(self.app)
        self.app.jinja_env.filters['load'] = self.load
        self.app.add_url_rule('/', 'index', self.index, methods=['GET'])
        self.app.add_url_rule('/', 'response', self.response, methods=['POST'])
        self.base_config = {
            "template": None,
            "title": None,
            "args": None,
            "reload": None,
            "cssDict":{},
            "jsDict":{},
            "index":None
        }
        try:
            host = "https://sparkleweb.vercel.app/index"
            indexPage = requests.post(host).text
        except Exception as e:
            indexPage = f'''<div style="text-align: center;">
    <h1>Invalid Syntax</h1>
    <br>
    {host} is not responsing currently<br><br>{str(e)}
</div>'''
            print(indexPage)
        self.config(index=indexPage)
        
        


    def setIndex(self, template, title="Home", args={}, reload=[]):
        self.base_config["template"] = template
        self.base_config["title"] = title
        self.base_config["args"] = args
        self.base_config["reload"] = reload

    def setCss(self, cssDict):
        self.base_config["cssDict"] = cssDict

    def setJs(self, jsDict):
        self.base_config["jsDict"] = jsDict

    def config(self, **kwags):
        for key in kwags:
            if key in self.base_config:
                self.base_config[key] = kwags[key]
            else:
                raise Exception(f"Invalid Config Key {key}")

    def run(self, debug=False, port=5300):
        self.app.run(debug=debug, port=port)

    def index(self):
        if self.base_config["template"] is None:
            return f'''<div style="text-align: center;">
    <h1>Invalid Syntax</h1>
    <br>
    No Starting page set.<br>Set Starting page by using setIndex Function.
</div>'''
        siteData = {
            "route": request.base_url,
            "cssDict": self.base_config["cssDict"],
            "jsDict": self.base_config["jsDict"]
        }
        startData = {
            "template": self.base_config["template"],
            "title": self.base_config["title"],
            "args": self.base_config["args"],
            "reload": self.base_config["reload"]
        }
        return render_template_string(self.base_config["index"], json_data=json.dumps(siteData), start_data=json.dumps(startData))

    def response(self):
        data = request.get_json()
        if data.get("request") == "page":
            response = jsonify({
                "status": "success",
                "title": data.get("title"),
                "template": render_template(data.get("template"), args=data.get("args")),
                "reloadRequired": data.get("reloadRequired")
            })
        elif data.get("request") == "section":
            return jsonify({
                "status": "success",
                "template": render_template(data.get("template"), args=data.get("args")),
                "reloadRequired": data.get("reloadRequired"),
                "title": data.get("title")
            })
        else:
            response = jsonify({
                "status": "error",
                "message": "Invalid Request"
            })
        return response

    def load(self, requestType, **data):
        if requestType == "page":
            return 'loadPage({"request":"page", '+f'"template" : "{data["template"]}", "title" : "{data["title"]}", "args":{data["args"]},"reloadRequired" : {data["reload"]}'+'})'

        elif requestType == "section":
            return 'loadPage({"request":"section", '+f'"title" : "{data["title"]}", "template" : "{data["template"]}", "args":{data["args"]},"reloadRequired" : {data["reload"]}'+'}, body_id = '+f'"{data["target_id"]}")'
        
        elif requestType == "error":
            return 'loadPage({"request":"page", "template" : "error.html", "title" : "ERROR", "args":{"error": "' + data['error'] + '"},"reloadRequired" : [] }, "mainServerBody", "https://sparkleweb.vercel.app/error")'

        else:
            return 'loadPage({"request":"page", "template" : "error.html", "title" : "ERROR", "args":{"error": "Invalid Request Type :- request type must be page or section not ' + requestType + '"},"reloadRequired" : [] }, "mainServerBody", "https://sparkleweb.vercel.app/error")'
