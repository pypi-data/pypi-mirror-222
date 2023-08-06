from flask import jsonify, render_template, request, render_template_string
from flask_cors import CORS
import json
import requests

class Server():
    def __init__(self, app, base, cssDict={}, jsDict={}) -> None:
        self.app = app
        CORS(self.app)
        self.cssDict = cssDict
        self.jsDict = jsDict
        self.base = base.get("template")
        self.base_title = base.get("title")
        self.base_args = base.get("args")
        self.base_reload = base.get("reloadRequired")
        self.app.jinja_env.filters['load'] = self.load
        self.app.add_url_rule('/', 'index', self.index, methods=['GET'])
        self.app.add_url_rule('/', 'response', self.response, methods=['POST'])
        self.base_template = requests.post("https://sparkleweb.vercel.app/index").text

    def run(self, debug=False, port=5300):
        self.app.run(debug=debug, port=port)

    def index(self):
        siteData = {
            "route": request.base_url,
            "cssDict": self.cssDict,
            "jsDict": self.jsDict
        }
        startData = {
            "template": self.base,
            "title": self.base_title,
            "args": self.base_args,
            "reload": self.base_reload
        }
        return render_template_string(self.base_template, json_data=json.dumps(siteData), start_data=json.dumps(startData))

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

        else:
            return 'loadPage({"request":"page", "template" : "error.html", "title" : "ERROR", "args":{"error": "Invalid Request Type :- request type must be page or section not ' + requestType + '"},"reloadRequired" : [] }, "mainServerBody", "https://sparkleweb.vercel.app/error")'
