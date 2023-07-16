def create_youtube_video(title,desc):
	vid = {'title': title, "description": desc, "likes": 0, "dislikes" : 0, "comments": {}}
	return vid
#as you asked


##i decided to do something else (DRY)
# def like(video):
# 	if "likes" in video.keys():
# 		video["likes"]+=1
# 	return video

# def dislike(video):
# 	if "dislikes" in video.keys():
# 		video["dislikes"]+=1
# 	return video

##the something else
def react(video, en):# en stands for enable, like on a flip flop
	if en == 1:
		if "likes" in video.keys():
			video["likes"]+=1
	elif en == 0:
		if "dislikes" in video.keys():
			video["dislikes"]+=1
	return video

def comment(youtubevideo, username, comment):
	youtubevideo["comments"][username] = comment
	return youtubevideo
##what you asked

fivemins = create_youtube_video("took me five minutes", "to bake a cake")##what you asked

react(fivemins, 1)

react(fivemins, 0)

for _ in range(494):
	react(fivemins, 1)
	#add 495 likes ( I added one before)


comment(fivemins, "sergey","I dont believe. fake news")
print(fivemins)