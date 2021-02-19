class User():
    def __init__(self, id):
        self.offset = 0
        self.id = id
        self.update_stats()
        self.answer = False

    def update_stats(self):
        with open("UserBase.txt", "r+") as f:
            lines = f.readlines()
            for i in range(0, len(lines)):
                if ("$"+self.id) in lines[i]:
                    self.offset = i
                    break
            self.name = lines[self.offset+1].split()[1]
            self.rotors = lines[self.offset+2].split()[1]
            self.wires = lines[self.offset+3].split()[1]
   
    def get_stat(self, stat):
        f = open("UserBase.txt", "r+")
        lines = f.readlines()
        f.close()
        line = self.offset+1
        while lines[line] != "\n":
            if lines[line].split()[0] == stat:
                return lines[line].split()[1]
            line+=1

    def change_stat(self, stat, value):
        f = open("UserBase.txt", "r+")
        lines = f.readlines()
        f.close()
        line = self.offset+1
        while lines[line] != "\n":
            if lines[line].split()[0] == stat:
                lines[line] = (stat + " " + value + "\n")
                break
            line+=1
            if lines[line] == "\n":
                return 1
        text = ""
        for i in lines:
            text+=i
        f = open("UserBase.txt", "w")
        f.write(text)
        f.close()
        self.update_stats()
        return 0
        

