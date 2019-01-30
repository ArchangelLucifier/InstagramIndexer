import os
from progressbar import ProgressBar
minFollowers = 10
maxFollowers = 1000

minFollowings = 10
maxFollowings = 700

files = os.listdir("./c/")
ca = 0
fids = open("fi.txt", "a")
fusername = open("fu.txt", "a")
pbar = ProgressBar(maxval=len(files))
pbar.start()
for file in files:
	data = open("./c/"+file, "r").read().split("\n")
	id = data[0]
	username = data[1]
	followers = int(data[2])
	followings = int(data[3])

	if followers > minFollowers and followers < maxFollowers:
		if followings > minFollowings and followings < maxFollowings:
			fids.write(id + "\n")
			fusername.write(username + "\n")
	ca += 1
	#print ca
	pbar.update(ca)
pbar.finish()
