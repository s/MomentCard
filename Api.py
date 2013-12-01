# -*- coding: utf-8 -*-

#################################################
# Api.py     		
# 30 November 2013
# Said ÖZCAN									
# MomentCard
#################################################

import httplib, urllib2, json, os, re

class Api:

	# Instagram Api Url
	api_host = 'api.instagram.com'


	# Instagram Api Method Type
	method = 'GET'


	#Instagram Api Path
	api_path = '/v1/media/{$media_id}?access_token={$access_token}'

	#Instagram Api Path
	oembed_api_path = '/oembed?url={$photo_url}'

	def __init__( self, access_token, photo_url ):

		self.access_token = access_token
		
		self.httpsObject = httplib.HTTPSConnection( self.api_host )		

		self.oembed_api_path = self.oembed_api_path.replace( '{$photo_url}' , photo_url  )

		self.media_id = self.get_media_id( self.oembed_api_path )
	
	def run(self):

		self.api_path = self.api_path.replace( '{$media_id}', self.media_id ).replace( '{$access_token}', self.access_token )
		
		self.httpsObject.request( self.method, self.api_path )

		response = self.httpsObject.getresponse()

		return response.read()

	def process(self):
		pass

	def get_media_id(self, photo_url):
		
		self.httpsObject.request( self.method, self.oembed_api_path )

		response = self.httpsObject.getresponse()

		if response.status == 200:
			
			responseJson = response.read()

			responseData = json.loads( responseJson )

			return responseData['media_id']

		else:
			return None
