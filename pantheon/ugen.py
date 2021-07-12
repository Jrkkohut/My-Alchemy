import sys
inputfile = sys.argv[1]
outputfile = sys.argv[2] 

def withdraw(self):
    self.info = open (inputfile,"r") 
    self.out=[]
    for i in self.info:
         self.out.append(i)
    self.info.close


def export(self):
    self.output = open (outputfile,"w")
    for line in withdraw.out:
        self.output.write(line)
    self.output.close

withdraw()    
export()
