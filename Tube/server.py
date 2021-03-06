import media
import tubelist
import os
import json
import requests

# These are the youtube video ids that we will serve to the page
vid_ids = ["IeyPqo1t3jM", "6-x_21W1nX0", "-6-3pbRz4YM", "k9WSx7jZ-Rk",
		   "Qm-AtSz628k", "wYxSbJHshAo", "hkbVbJkBk_w", "BcOI7TqbxhA", "KeOWFI9uZkQ"]

# load in api key and get data needed for query
youtube = os.path.join(os.getcwd(), 'youtube.json')
query = json.loads(open(youtube).read())


def get_data_by_type(data, type):
	"""
	 Returns dictionary of specified type from data
	 returned from youtube api.
	 those types are:
		items
		kind
		eTag
		pageInfo
	"""
	for k in data:
		if k == type:
			return data[k]


def get_data_snippet(data):
	"""
	Most of the data we want exists under "snippet" in the data.
	We return the data from this part of the youtube dictionary.
	"""
	for k in data:
		if k == "items":
			for obj in data[k]:
				snippet = obj["snippet"]
				return snippet



def get_video_title(data):
	"""
	Given data returned from youtube api, returns the video title.
	"""
	dct = get_data_snippet(data)
	for k in dct:
		if k == "title":
			return dct[k]


def get_video_description(data):
	"""
	Given data returned from youtube api, returns the video title
	"""
	dct = get_data_snippet(data)
	for k in dct:
		if k == "description":
			descr = dct[k]
			return dct[k]


def get_video_img(data, type):
	"""
	 Given data returned from youtube api, returns the video image
	 Second parameter is the type of image desired.
	 Types available are:
		default = (120X90)
		high = (480X360)
		medium = (320X180)
		maxres = (1280X720)
		standard = (640X480)
	"""
	dct = get_data_snippet(data)
	for k in dct:
		if k =="thumbnails":
			thumbs = dct[k]
			img = thumbs[type]
			return img["url"]



def create_video_objects(ids):
	"""
	 Queries youtube to get the data about each video id in array
	 Creates a video object for each video, puts into an array and
	 returns that array
	"""

	videos = []

	for id in ids:

		params = dict(
			key=query['key'],
			part=query['part'],
			id=id
		)

		resp = requests.get(query['url'], params=params)
		data = json.loads(resp.text)

		title = get_video_title(data)
		dscr = get_video_description(data)
		image = get_video_img(data, 'high')

		video = media.Video(id, title, dscr, image)

		video.set_link()
		videos.append(video)

	return videos


tubelist.open_movies_page(create_video_objects(vid_ids))
