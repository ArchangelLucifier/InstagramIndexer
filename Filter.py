import time
from InstagramAPI import InstagramAPI

class Filter():
    def __init__(self, currentNumber, login, password, proxy, user_agent, phone_id, guid, device_id, crftoken):
        self.currentNumber = currentNumber
        self.login = login
        self.password = password
        self.proxy = proxy
        self.user_agent = user_agent
        self.phone_id = phone_id
        self.guid = guid
        self.device_id = device_id
        self.crftoken = crftoken

    def auth(self):
        self.api = InstagramAPI(self.login, self.password)
        self.api.USER_AGENT = self.user_agent
        self.api.setProxy(self.proxy)
        status = self.api.login(self.phone_id,
                                self.guid,
                                self.device_id,
                                self.crftoken)

    def setIDS(self, ids):
        self.ids = ids
        print "Filter #" + str(self.currentNumber) + " set ids"

    def parse(self):
        for id in self.ids:
            self.api.getUsernameInfo(id)
            try:
                user = self.api.LastJson['user']
                username = user['username']
                followers = user['follower_count']
                followings = user['following_count']
                # print id, username, followers, followings
                print "c/" + id + ".txt"
                data = id + "\n" + username + "\n" + str(followers) + "\n" + str(followings)
                open("./c/" + id + ".txt", "w").write(data)
                time.sleep(5)
            except:
                print "Filter #" + str(self.currentNumber) + " parse error"

    def start(self):
        self.auth()
        self.parse()
