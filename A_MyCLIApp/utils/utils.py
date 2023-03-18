def printl(list):
    for i, item in enumerate(list):
        print(i, item)

from string import Template

class DeltaTemplate(Template):
    delimiter = "%"

    @staticmethod
    def strfdelta(tdelta, fmt):
        d = {"D": tdelta.days}
        d["H"], rem = divmod(tdelta.seconds, 3600)
        d["M"], d["S"] = divmod(rem, 60)
        d["H"] = d["H"] + tdelta.days * 24
        t = DeltaTemplate(fmt)
        return t.substitute(**d)