#!/home/mft/Projects/basicallygdb/archer/gdb/gdb -P

from mainform import MyFrame1
import wx
import wx.stc as stc
import sys
import gdb 

def run(command):
    return gdb.execute(command, to_string=True)

class MainFrame(MyFrame1):

    ASSEMBLY_COLOR_ADDRESS = (100,100,100)
    ASSEMBLY_COLOR_INSTRUCTION = (0,0,255)
    
    def addstyledtext(self, styledtextobj, text, color):
        styledtextobj.BeginTextColour(color)
        styledtextobj.WriteText(text)
        styledtextobj.EndTextColour()
    
    def showdisassemble(self, functionname):
        disas = run("disas " + functionname)
        
        disaslines = disas.split("\n")
        
        for line in disaslines[1:-2]:
            print line
            linetabsplit = line.split("\t")
            self.addstyledtext(self.code, linetabsplit[0].replace(" ", ""), self.ASSEMBLY_COLOR_ADDRESS)
            
            if len(linetabsplit[0].replace(" ", "")) < 24:  
                self.addstyledtext(self.code, "\t", self.ASSEMBLY_COLOR_ADDRESS)
                
            self.addstyledtext(self.code, "\t", self.ASSEMBLY_COLOR_ADDRESS)
            
            print linetabsplit[1].split(" ")
            
            asmfullcommand = linetabsplit[1].split(" ")
            
            
            self.addstyledtext(self.code, asmfullcommand[0] + '\t\t', self.ASSEMBLY_COLOR_INSTRUCTION)
                       
            self.addstyledtext(self.code, ''.join(asmfullcommand[1:]), (0,0,0))
            
            
            self.addstyledtext(self.code, "\n", self.ASSEMBLY_COLOR_ADDRESS)
            
        
    
    def __init__(self,parent):
        MyFrame1.__init__(self,parent)
                
        gdb.execute("file " + sys.argv[0])
        gdb.execute("set disassembly-flavor intel")
        
        print "loaded file " + sys.argv[0]
        
        self.showdisassemble("main")

print "hello from pytrhon"




app = wx.App(False)

frame = MainFrame(None)
frame.Show(True)
app.MainLoop()
