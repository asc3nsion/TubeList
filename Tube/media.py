class Video():
	"""This is the class object used to store data returned from youtube
	-----------------------------------------------------------------------
	1. It must be passed a video id, title, image link.
	2. The video link is created by calling this objects' set_link method."""
	BASE_URL = "https://www.youtube.com/watch?v="

	def __init__(self, video_id, video_title, video_description, video_image,
				 video_link=None):
		self.id = video_id
		self.title = video_title
		self.description = video_description
		self.image = video_image
		self.link = video_link

	def set_link(self):
		self.link = Video.BASE_URL + self.id
