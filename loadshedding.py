# import requests
import os.path
import httplib2 as http

class loadsheddingData:
    def __init__(self):
        self.dicti = self.perform_first_use()

    def getat(self, group):
        url = "https://acpmasquerade-nepal-loadshedding-schedule-by-sparrow-sms.p.mashape.com/schedule.php?format=format=json&group=" + str(
            group)
        h = http.Http()
        method="GET"
        headers={
            "X-Mashape-Key": "S5tT684lzzmsh7b9IggZVkjDllGsp1mWOaajsnh5mvzw7fk8uU",
            "Accept": "text/plain"
        }
        response, content = h.request(url,method,'',headers)
        return content

    # These code snippets use an open-source library.
    def update_dicti(self, dicti):
        with open(os.path.expanduser(r"~/.loadshedding/group"), "w") as text_file:
            text_file.write(dicti["group"])
        with open(os.path.expanduser(r"~/.loadshedding/latest"), "w") as text_file:
            text_file.write(dicti["latest"])
        with open(os.path.expanduser(r"~/.loadshedding/data"), "w") as text_file:
            text_file.write(dicti["data"])

    def refresh_data(self, dicti):
        if dicti is None:
            dicti = {"group": 1, "latest": "Never", "data": "Update before use"}
        group = dicti['group']
        datas = self.getat(group)
        liness = datas.split('\n')
        if not (dicti["latest"][:10] == liness[1]):
            dicti["group"] = 1
            dicti["latest"] = liness[1]
            dicti["data"] = datas
            self.update_dicti(dicti)
            for i in range(1, 8):
                dts = self.getat(i)
                fln = os.path.expanduser(r"~/.loadshedding")
                fln = fln + r"/dat" + str(i)
                with open(fln, "w") as text_file:
                    text_file.write(dts)
        self.dicti = dicti
        return dicti

    def retrieve(self):
        group = open(os.path.expanduser(r"~/.loadshedding/group")).read()
        latest = open(os.path.expanduser(r"~/.loadshedding/latest")).read()
        data = open(os.path.expanduser(r"~/.loadshedding/data")).read()
        dicti = {"group": int(group), "latest": latest, "data": data}
        return dicti

    def perform_first_use(self):
        if os.path.exists(os.path.expanduser(r"~/.loadshedding/")):
            return self.retrieve()
        else:
            os.makedirs(os.path.expanduser(r'~/.loadshedding'))
            self.update_dicti({"group": 7, "latest": "never", "data": "Not updated"})
            return self.refresh_data(None)

    def getDatFile(self, group):
        fln = os.path.expanduser(r"~/.loadshedding")
        fln = fln + r"/dat" + str(group)
        return open(fln).read()
