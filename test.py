#!/home/mft/Projects/gdbmft/archer/gdb/gdb -P

from mainform import MyFrame1
import wx
import wx.stc as stc
import wx.richtext as rt
import sys
import gdb
import re 

def run(command):
    return gdb.execute(command, to_string=True)

class MainFrame(MyFrame1):

    ASSEMBLY_COLOR_ADDRESS = (100,100,100)
    ASSEMBLY_COLOR_INSTRUCTION = (0,0,255)
    ASSEMBLY_COLOR_REGISTER = (255,0,255)
    ASSEMBLY_COLOR_NUMBERS = (0,100,0)
    
    REGISTERS = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15", "rip", "eflags", "cs", "ss", "ds", "es", "fs", "gs"]
    
    def addstyledtext(self, styledtextobj, text, color):
        styledtextobj.BeginTextColour(color)
        styledtextobj.WriteText(text)
        styledtextobj.EndTextColour()
    
    def colorAllText(self, richtext, text, color):
        dacode = richtext.GetValue()
        
        curidx = 0
        
        while curidx != -1:
            curidx = dacode.find(text, curidx)
            
            if curidx == -1:
                break
            
            style = rt.TextAttrEx()
            style.SetTextColour(self.ASSEMBLY_COLOR_REGISTER)
            self.code.SetStyle((curidx, curidx+len(text)), style)
            
            curidx += len(text)
        
    def colorRegEx(self, richtext, regex, color):
        dacode = richtext.GetValue()
        curidx = 0
        
        while True:
            
            pattern = re.compile(regex)
            m = pattern.search(dacode, curidx)
            if m:
                foundstr = m.group(0)
                curidx = m.start(0)

                    
                style = rt.TextAttrEx()
                style.SetTextColour(color)
                self.code.SetStyle((curidx, curidx+len(foundstr)), style)
                
                curidx += len(foundstr)
            else:
                break
    
    def getFunctions(self):
        pass
    
    def showdisassemble(self, functionname):
        self.code.Clear()
        disas = run("disas " + functionname.replace("@plt", ""))
        
        disaslines = disas.split("\n")
        print disaslines[1:-2]
        for line in disaslines[1:-2]:
            
            # line looks like this 
            # 0x0000000000400603<+1>:        mov        rbp,rsp
     
            # line split at tab splits address and instruction 
            # ['   0x000000000040063a <+56>:', 'mov    rax,QWORD PTR [rax]']
            linetabsplit = line.split("\t")
            
            # write the address            
            self.addstyledtext(self.code, linetabsplit[0].replace(" ", ""), self.ASSEMBLY_COLOR_ADDRESS)
            
            # divide address and instruction with a tab, if the <+xx> number is too short add another tab
            if len(linetabsplit[0].replace(" ", "")) < 24:  
                self.addstyledtext(self.code, "\t", self.ASSEMBLY_COLOR_ADDRESS)
                
            self.addstyledtext(self.code, "\t", self.ASSEMBLY_COLOR_ADDRESS)
            
            # parse the command            
            asmfullcommand = linetabsplit[1].split(" ")
            print asmfullcommand
            # write the instruction
            self.addstyledtext(self.code, asmfullcommand[0], self.ASSEMBLY_COLOR_INSTRUCTION)
            
               
            self.addstyledtext(self.code, '\t\t', self.ASSEMBLY_COLOR_INSTRUCTION)
            
            # write the rest of the command
            self.addstyledtext(self.code, ''.join(asmfullcommand[1:]), (0,0,0))
            
            test = ''.join(asmfullcommand[1:])
            print self.code.GetValue().encode("hex")
            
            self.addstyledtext(self.code, "\n", self.ASSEMBLY_COLOR_ADDRESS)
            
        
        # style registers
        for register in self.REGISTERS:
            self.colorAllText(self.code, register, self.ASSEMBLY_COLOR_REGISTER)
        
        # style numbers
        self.colorRegEx(self.code, '0x[0-9abcdef]*', self.ASSEMBLY_COLOR_NUMBERS)
        
        # correctly style the now green numbers of the address
        self.colorRegEx(self.code, '0x[0-9abcdef]*<\+[0-9]*>:', self.ASSEMBLY_COLOR_ADDRESS)
        
        print run("info functions")
    
    
    def functionchoose(self, event):
        selectedfunction = self.listfunctions.GetStringSelection()
        print "here it is " + selectedfunction
        self.showdisassemble(selectedfunction)
    
    
    def __init__(self,parent):
        MyFrame1.__init__(self,parent)
        
        self.listfunctions.Bind(wx.EVT_LISTBOX, self.functionchoose)   
        
        gdb.execute("file " + sys.argv[0])
        gdb.execute("set disassembly-flavor intel")
        
        print "loaded file " + sys.argv[0]
        
        functionsstr = run("info functions")
        functionslist = functionsstr.split("\n")
        print functionslist
        for functionname in functionslist[3:]:
            namesplit = functionname.split(" ")
            if len(namesplit) >=2:
                self.listfunctions.Append(namesplit[2])
        
        #self.showdisassemble("main")






app = wx.App(False)

frame = MainFrame(None)
frame.Show(True)
app.MainLoop()