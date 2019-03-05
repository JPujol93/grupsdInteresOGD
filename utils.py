
class node:

    def __init__(self, vals):
        self.name=vals[0]
        self.type=vals[1]
        self.extra= vals[2]
        self.source=vals[3]

class edge:


    def __init__(self, vals):


        self.origin=vals[0]
        self.end = vals[1]
        self.charge= vals[2]
        self.publicFound = vals[3]
        self.sector= vals[4]
        self.code = vals[5]
        self.amount= vals[6]
        self.parenthood = vals[7]
        self.title= vals[8]
        self.location = vals[9]
        self.extra = vals[10]
        self.source = vals[11]
        self.origin = vals[12]


