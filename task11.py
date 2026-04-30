class Song:
	def__init__(self,title, artist, duration, genre,play_count):
		self.title = title
		self.artist = artist
		self.duration = duration
		self.genre= genre
		self.play_count = play_count
	def get_title(self):
		return self.title
	def get_artist(self):
		return self.artist
	def get_duration(self):
		return self.duration
	def get_genre(self):
		return self.genre
	def get_play_count(self):
		return self.play_count
	def set_title(self, title):
		self.title = title
	def set_artist(self, artist):
		self.artist = artist
	def set_duration(self, duration):
		self.duration = duration
	def set_genre(self, genre):
		self.genre = genre
	def set_play_count(self, play_count):
		self.play_count = play_count
	def get_duration_formatted(self):
		minutes = self.duration // 60
		seconds = self.duration % 60
		return f"{minutes:02d}:{seconds:02d}"
	def is_short(self):
		return self.duration < 180
	def play(self):
		for _ in range(n):
			self.play_count += 1
			print(f"Проиграно {self.title} от {self.artist}. Всего прослушиваний {self.play_count}")
	def get_content(self):
		return "Music"
	def str(self):
		return f"Песня: {self.title] от {self.artist}({self.get_duration_formatted()})"
	def it(self, other):
		if not isinstance(other, Song):
			return  self.play_count < other.play_count
	def iadd(self, other):
		if isinstance(other, int):
			self.play_count += other
			return self
		return Notimplemented
class Podcast(Song):
	def__init__(self, title, artist, duration, genre, episode_number, episodes = None, play_count = 0):
		super().__init__(title, artist, duration, genre, play_count)
		self.episode_number = episode_number
		self.episodes = episodes if episodes is not None else []
	def episode_number(self):
		return self.episode_number
	def is_short(self):
		return self.duration < 1200
	def get_content_type(self):
		return "Podcast"
	def play(self, n = 1):
		for _ in range(n):
			self.play_count += 1
			print(f" Эпизод {self.epsode_number} название {self.title}. Всего {self.play_count}")

	def str(self):
		return f"Podcast: {self.title}. Episode {self.episode_number}({self.get_duration_formatted()})"
	def getitem(self, index):
		return self.episodes[index]
song1 = Song("Apex", "David", 355, "Rock")
print(song1)
print(f"is short? {song1.is_short()}")
print(f"Genre: {song1.get_content_type()}")

podcast1 = Podcast("House", "Alex", 1500, "Technology", 5, ["Intro", "News", "Outro"]
print(podcast1)
print(f"is short?{podcast1.is_short()}"
print(f"Type{podcast1.get_content_type()}")
print(f"Current episode part: {podcast1[1]}") 

song2 = Song("Short Song", "Artist", 120, "Pop")
song2.play(10) 
print(f" is {song2.title} < {song1.title}? {song2 < song1}")
song2 += 5
print(f" New play count for {song2.title}: {song2.play_count}")
	