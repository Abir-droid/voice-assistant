# voice-assistant
A voice assistant for windows made with python:

This is a command line voice assistant code made with python. It can run some usual task on your computer through voice. It can also help you to search in the
in the intrnet and do other tasks.

Thing's that this voice assistant can do:

1. Opening apps.
2. listing installed apps.
3. telling weather information.
4. telling time.
5. telling date.
6. telling 5 international news topics.
7. opening the news on browser by topic number.
8. Increasing or decreasing volume.
9. Turn on or off wifi.
10. list video files.
11. play video.
12. list music files.
13. play music.

Description of the functions:

1. listing installed apps:
	Just say "list apps". And it will show the list of installed apps on your pc.
2. Opening apps:
        Say "open (the app name)". And it will open the app for you. Remember that the app name has to be the exact name which is listed on the installed app from
		the previous command. Otherwise it won't work. [Example: open notepad]
3. telling weather information:
	Say "weather in (the city name)". And it will show the weather information of that city. [Eample: tell me the weather in Dhaka./what is the weather in Dhaka]
4. telling time:
	Say any sentence including the word "time" and it will tell you the local time. [Example: What is the time now? /Tell me the time/time]
5. telling date:
	Say any sentence including the word "date" and it will tell you today's date. [Example: What is the date today? /Tell me today's date /date]
6. telling 5 international news topics:
	By saying "news" it'll tell and show you 5 internaltional topic.
7. opening the news topic on browser by topic number:
	To know more about a news topic from 6 number step, you have to say "tell me about topic" and then it will ask you to enter the topic number.
	After typing the topic number it will redirect you to news article in your browser. 
8. Increasing or decreasing volume:
	To increase the volume of your pc say "volume up to (the percentage of volume). [Eample: volume up to 80 percent]
	To decrease the volume of your pc say "volume down to (the percentage of volume). [Eample: volume down to 20 percent]
9. Turn on or off wifi(Needed to run the pyhton file with Adminstrator previlages):
	to turn on wifi Say "turn on wireless fidelity"
	to turn of wifi Say "turn of wireless fidelity"
10. list video files:
	To list the video files on your video folder, say "videos". (Give the video file's folder path on the code)
11. play video:
	To play the video, you have two option:
		1. Play the video by the video's title:
			say "play video (video's title)"
		2. Play the video by it's position:
			say "play the (first/second/third etc) video"
12. list music files:
	To list the music files on your music folder, say "musics". (Give the music file's folder path on the code)
13. play music:
	To play the music, you have two option:
		1. Play the music by the music's title:
			say "play music (music's title)"
		2. Play the video by it's position:
			say "play (first/second/third etc) music"

To be noted:

# To run this code, you have to install the necessary python modules.
# The voice command's writen in the tutorials are absolute for executing commands. Means whatever sentence you say for executing a task it must
  have the corresponding words/phrases written in above.
# You have to modify the code according to your requirements. Like: for playing the video or music you must have to give your own folder paths in the code.
  And you can modify the 
# To turn on/off wifi you need to run this python file in the terminal with adminstritive previlages.
# The speech to text module used in this code doesn't support numbers. (It will recognize 1 as one).
