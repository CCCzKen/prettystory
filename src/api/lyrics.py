# coding: utf-8
from flask import request, jsonify
from flask.ext.restful import Resource
from src.function import Lyrics


class Song(Resource):
	def get(self):
		song = request.args.get('song', '')
		singer = request.args.get('singer', '')
		text = Lyrics(song, singer).find()
		res = {
			'song': song,
			'singer': singer,
			'lyrics': text
		}
		print text
		return jsonify(res)
