from pytube import YouTube
from pytube.cli import on_progress
from moviepy.editor import *
from redvid import Downloader
from colorama import Back, Style
import re
import os

def merge_clips(video_path:str, audio_path:str, output_path:str):
	video_clip = VideoFileClip(video_path)
	audio_clip = AudioFileClip(audio_path)
	new_audio_clip = CompositeAudioClip([audio_clip])
	video_clip.audio = new_audio_clip
	video_clip.write_videofile(output_path) 

def youtube(user_link:str):
	
	choices = {
		"1" : "1080p",
		"2" : "720p",
		"3" : "480p",
		"4" : "360p",
		"5" : "240p",
		"6" : "144p"
	}

		
	
	stream_itag = 0
	audio_stream_itag = 0	
	
	yt = YouTube(user_link, on_progress_callback=on_progress)
	for i in choices:
		print(f"{i} => {choices[i]}")


	user_i = input("Choose a resolution:")
		
	print(yt.title)
	video_title =re.sub("[+*.|()${}?#]", "", yt.title)
	for stream in yt.streams.filter(file_extension="mp4"):
		is_av01 =  stream.codecs[0].find('av01')
		is_avc1 = stream.codecs[0].find('avc1')
		if stream.resolution == choices[user_i]  and is_av01 == 0:
		       	stream_itag = stream.itag
			#print(f"{stream.resolution} | {stream.itag} ")
		elif stream.resolution == choices[user_i] and is_avc1 == 0:
			stream_itag = stream.itag
	for audio_strm in yt.streams.filter(only_audio=True, file_extension="mp4"):
		if audio_strm.abr == "128kbps":
			audio_stream_itag = audio_strm.itag
			print(audio_stream_itag)
		
	print(f"{Back.BLUE} !!!Downloading Video!!! {Style.RESET_ALL}")
	strm = yt.streams.get_by_itag(stream_itag)
	strm.download("video/", filename=f"{video_title}.mp4")	
	
	print(f"{Back.BLUE} !!!Downloading Audio!!! {Style.RESET_ALL}")
	a_strm = yt.streams.get_by_itag(audio_stream_itag)
	a_strm.download("audio/", filename=f"{video_title}.mp4")	
	
	os.makedirs("Youtube", exist_ok=True)

	merge_clips(f"video/{video_title}.mp4", f"audio/{video_title}.mp4", f"Youtube/{video_title}.mp4")
			
def reddit(user_link:str):
	reddit = Downloader(max_q=True)
	reddit.url = user_link
	os.makedirs("Reddit", exist_ok=True)
	reddit.path = "Reddit"
	reddit.download()
	
