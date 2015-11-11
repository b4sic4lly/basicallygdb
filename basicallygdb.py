#!/home/mft/Projects/gdbmft/archer/gdb/gdb -P

from mainform import FrameMain
import wx
import wx.stc as stc
import wx.richtext as rt
import sys
import gdb
import re 

def run(command):
    try:
        return gdb.execute(command, to_string=True)
    except gdb.error as e:
        return str(e) + "\n"


class PageASM(wx.Panel):
   def __init__(self, parent):
       wx.Panel.__init__(self, parent)
       self.bSizer = wx.BoxSizer( wx.VERTICAL )
              
       self.textbox = rt.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
       self.textbox.SetFont( wx.Font( 10, 76, 90, 90, False, "Monospace" ) )
              
       self.bSizer.Add( self.textbox, 5, wx.EXPAND |wx.ALL, 5 )
       
       self.SetSizer( self.bSizer )


class MainFrame(FrameMain):

    ASSEMBLY_COLOR_ADDRESS = (100,100,100)
    ASSEMBLY_COLOR_INSTRUCTION = (0,0,255)
    ASSEMBLY_COLOR_REGISTER = (255,0,255)
    ASSEMBLY_COLOR_NUMBERS = (0,100,0)
    ASSEMBLY_COLOR_BREAKPOINT = (150,0,0)
    
    REGISTERS = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15", "rip", "eflags", "cs", "ss", "ds", "es", "fs", "gs"]
    
    def addstyledtext(self, styledtextobj, text, color):
        styledtextobj.BeginTextColour(color)
        styledtextobj.WriteText(text)
        styledtextobj.EndTextColour()
    
    def markAssemblyLine(self, richtext, line, textcolor, color):
        if line != None:
            allreturns = [m.start() for m in re.finditer('\n', richtext.GetValue())]
            
            # insert a \n position at the beginning such that line 1 can be marked
            allreturns.insert(0, 0)
            
            doublepointidx = richtext.GetValue().find(":", allreturns[line])
            print allreturns[line]
            print doublepointidx
             
            style = rt.TextAttrEx()
            style.SetBackgroundColour(color)
            style.SetTextColour(textcolor)
            richtext.SetStyle((allreturns[line],doublepointidx), style)
    
    
    def colorAllText(self, richtext, text, color):
        dacode = richtext.GetValue()
        
        curidx = 0
        
        while curidx != -1:
            curidx = dacode.find(text, curidx)
            
            if curidx == -1:
                break
            
            style = rt.TextAttrEx()
            style.SetTextColour(color)
            richtext.SetStyle((curidx, curidx+len(text)), style)
            
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
                richtext.SetStyle((curidx, curidx+len(foundstr)), style)
                
                curidx += len(foundstr)
            else:
                break
    
    def getFunctions(self):
        pass
    
    def getTextBoxLineByAddress(self, richtext, address):
        text = richtext.GetValue()
        textarr = text.split("\n")
        print "searching for address " + address
        for i in range(0, len(textarr)):
            line = textarr[i]
            pattern = re.compile("0x[0-9abcdef]*")
            m = pattern.search(line)
            if m:
                foundstr = m.group(0)
                if foundstr == address:
                    return i
            
    
    def getCurrentBreakpoints(self):
        breakpointlist = run("info breakpoints")
        
        breakpointlistarr = breakpointlist.split("\n")
        
        resultlist = []
        
        for line in breakpointlistarr:
        
            pattern = re.compile("0x[0-9abcdef]*")
            m = pattern.search(line)
            if m:
                foundstr = m.group(0)
                resultlist.append(foundstr)
                
        return resultlist
    
    def showdisassemble(self, coderichtext, functionname):
        coderichtext.Clear()
        style = coderichtext.GetDefaultStyle()
        coderichtext.SetStyle((0,len(coderichtext.GetValue())), style)
        disas = run("disas " + functionname.replace("@plt", ""))
        
        disaslines = disas.split("\n")

        for line in disaslines[1:-2]:
            
            # line looks like this 
            # 0x0000000000400603<+1>:        mov        rbp,rsp
     
            # line split at tab splits address and instruction 
            # ['   0x000000000040063a <+56>:', 'mov    rax,QWORD PTR [rax]']
            linetabsplit = line.split("\t")
            
            # write the address            
            self.addstyledtext(coderichtext, linetabsplit[0].replace(" ", ""), self.ASSEMBLY_COLOR_ADDRESS)
            
            # divide address and instruction with a tab, if the <+xx> number is too short add another tab
            if len(linetabsplit[0].replace(" ", "")) < 24:  
                self.addstyledtext(coderichtext, "\t", self.ASSEMBLY_COLOR_ADDRESS)
                
            self.addstyledtext(coderichtext, "\t", self.ASSEMBLY_COLOR_ADDRESS)
            
            # parse the command            
            asmfullcommand = linetabsplit[1].split(" ")
            # write the instruction
            self.addstyledtext(coderichtext, asmfullcommand[0], self.ASSEMBLY_COLOR_INSTRUCTION)
            
               
            self.addstyledtext(coderichtext, '\t\t', self.ASSEMBLY_COLOR_INSTRUCTION)
            
            # write the rest of the command
            self.addstyledtext(coderichtext, ''.join(asmfullcommand[1:]), (0,0,0))
                        
            self.addstyledtext(coderichtext, "\n", self.ASSEMBLY_COLOR_ADDRESS)
            
        
        
        # style registers
        for register in self.REGISTERS:
            self.colorAllText(coderichtext, register, self.ASSEMBLY_COLOR_REGISTER)
        
        # style numbers
        self.colorRegEx(coderichtext, '0x[0-9abcdef]*', self.ASSEMBLY_COLOR_NUMBERS)
        
        # correctly style the now green numbers of the address
        self.colorRegEx(coderichtext, '0x[0-9abcdef]*<\+[0-9]*>:', self.ASSEMBLY_COLOR_ADDRESS)
        
        # mark breakpoints
        for breakpoint in self.getCurrentBreakpoints(): 
            self.markAssemblyLine(coderichtext, self.getTextBoxLineByAddress(coderichtext, breakpoint), (255,255,255), self.ASSEMBLY_COLOR_BREAKPOINT)
            
        # mark current position of IP
        curip = self.getRegisterValueHex("rip")
        if curip != None:
            self.markAssemblyLine(coderichtext, self.getTextBoxLineByAddress(coderichtext, curip), (255,255,255), (0,0,100))
    
    def functionchoose(self, event):
        selectedfunction = self.listfunctions.GetStringSelection()
        #self.showdisassemble(selectedfunction)
        self.openPageASM(selectedfunction)
    
    def getRegisterValueHex(self, registerstring):
        result = run("info registers " + registerstring)
        pattern = re.compile("0x[0-9abcdef]*")
        m = pattern.search(result)
        if m:
            foundstr = m.group(0)
            # bring in 64 bit format
            foundstr = "0x" + "0"*(18-len(foundstr)) + foundstr[2:]
            print "REGISTER IS " + foundstr
            return foundstr
        else:
            return None
    
    def updateAllASMPages(self):
        for i in range(0, self.notebookasm.GetPageCount()):
            functionname = self.notebookasm.GetPageText(i)
            self.showdisassemble(self.notebookasm.GetPage(i).textbox, functionname)
        
    
    def issueGDBCommand(self, event):
        result = run(self.txtgdbinput.GetValue())
        self.txtgdboutput.AppendText("$ " + self.txtgdbinput.GetValue() + "\n")
        self.txtgdboutput.AppendText(result)
        self.txtgdbinput.SetValue("")
        self.updateAllASMPages()
        
       
    def txtgdbinput_OnKeyDown(self, event):
        if event.GetKeyCode() != wx.WXK_RETURN:
            event.Skip()
            return
        
        self.issueGDBCommand(event)
    
    def functionAlreadyOpened(self, functionname):
        for i in range(0, self.notebookasm.GetPageCount()):
            if functionname == self.notebookasm.GetPageText(i):
                return i
        
        return -1
    
    
    def openPageASM(self, functionname):
        pageid = self.functionAlreadyOpened(functionname)
        
        if pageid >= 0:
            # already opened this just show it
            self.notebookasm.SetSelection(pageid)
        else:
            # we have to create the page
            newpage = PageASM(self.notebookasm)
            self.notebookasm.AddPage(newpage, functionname)
            self.showdisassemble(newpage.textbox, functionname)
    
    def __init__(self,parent):
        FrameMain.__init__(self,parent)
        
                        
        # event bindings
        self.listfunctions.Bind(wx.EVT_LISTBOX, self.functionchoose)   
        self.cmdsendgdbcommand.Bind(wx.EVT_BUTTON, self.issueGDBCommand)
        self.txtgdbinput.Bind(wx.EVT_KEY_DOWN, self.txtgdbinput_OnKeyDown)
        
        gdb.execute("file " + sys.argv[0])
        gdb.execute("set disassembly-flavor intel")
        
        gdb.execute("b *0x00000000004004b6")
        gdb.execute("b *0x0000000000400617")
        gdb.execute("b *0x0000000000400630")
        
        print "loaded file " + sys.argv[0]
        
        functionsstr = run("info functions")
        functionslist = functionsstr.split("\n")
        print functionslist
        for functionname in functionslist[3:]:
            namesplit = functionname.split(" ")
            if len(namesplit) >=2:
                self.listfunctions.Append(namesplit[2])
           



app = wx.App(False)

frame = MainFrame(None)
frame.Show(True)
app.MainLoop()