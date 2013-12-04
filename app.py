# -*- coding: utf-8 -*-

#################################################
# app.py     		
# 30 November 2013
# Said ÖZCAN									
# MomentCard
#################################################

from flask import *
from Api import Api
import flask, json
import datetime

app = Flask(__name__)

response = {}

@app.route('/generate',methods=['GET'])
def generate():	

	params = []

	required = ['access_token','photo_url']	

	for e in required:
		
		param = request.args.getlist(e) 
		
		if len(param) <= 0:
			response.update({
				"err":"1",
				"msg":e + ' is required for this method'
			})

			return reply(response)

		else:

			params.append(param)


	api = Api(params[0][0],params[1][0])

	photo_data = json.loads(api.run())

	if photo_data:
		
		try:
			photo_data["data"]["created_time"] = datetime.datetime.fromtimestamp(int(photo_data["data"]["created_time"])).strftime('%d %b %Y')
		except:
			pass
		return render_template("generate.html",all_info=photo_data)
	else:
		response.update({
			"err":"1",
			"msg":"Photo could not been fetched."
		})
		return reply(response)

@app.errorhandler(404)
def not_found(e):
	response.update({
		"err":"1",
		"msg":"Specified url not found on the server."
	})

	return reply(response), 404


def reply(response):
	return flask.jsonify(response)

if __name__ == "__main__":
    app.run('127.0.0.1',1105,debug=True)