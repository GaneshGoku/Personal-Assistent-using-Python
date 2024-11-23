# def downloadYouTube():
#     speak("Please provide the URL of the YouTube video you want to download.")
#     youtube_url = takeCommand()
#     if youtube_url != "None":
#         try:
#             yt = YouTube(youtube_url)
#             video = yt.streams.filter(progressive=True, file_extension='mp4').first()
#             video.download()
#             speak("Video downloaded successfully")
#         except Exception as e:
#             print(e)
#             speak("Sorry, I couldn't download the video.")
#     else:
#         speak("No URL provided")