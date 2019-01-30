from Filter import Filter
from threading import Thread

class FilterController():
    def __init__(self, accountsFilepath, idsFilepath):
        self.accountsFilepath = accountsFilepath
        self.idsFilepath = idsFilepath
        self.filters = []
        # self.ids = open(self.idsFilepath, "r").read().replace("\r", "").split("\n")
        self.ids = open(self.idsFilepath, "r").read().replace("\r", "").split("\n")

    def createWorkers(self):
        accs = open(self.accountsFilepath, "r").read().replace("\r", "").split("\n")
        ca = 0
        for acc in accs:
            u, d = acc.split("+-+")
            lp, py = u.split(";")
            l, p = lp.split(":")

            d = d.split("|")

            user_agent = d[0]
            phone_id = d[1]
            guid = d[2]
            device_id = d[3]
            crftoken = d[4]

            w = Filter(ca, l, p, py, user_agent, phone_id, guid, device_id, crftoken)

            self.filters.append(w)
            ca += 1

    def idsPrepair(self):
        self.ArrayOfIds = []
        module = len(self.ids) % len(self.filters)
        equalIDS = self.ids[0:len(self.ids) - module]
        colIDS = len(equalIDS)/ len(self.filters)

        lastIDS = self.ids[len(equalIDS):len(self.ids)]

        for i in range(len(self.filters)):
            self.ArrayOfIds.append(equalIDS[i*colIDS:(i+1)*colIDS])

        lID = 0
        for lastID in lastIDS:
            try:
                self.ArrayOfIds[lID].append(lastID)
            except:
                print lID
            lID += 1

    def run(self):
        cf = 0

        for filter in self.filters:
            filter.setIDS(self.ArrayOfIds[cf])
            Thread(target=filter.start).start()

            cf += 1

if __name__ == "__main__":
    fc = FilterController("Assets/Accounts.txt", "Assets/ids4.txt")
    fc.createWorkers()
    fc.idsPrepair()
    fc.run()
