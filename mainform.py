# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FrameMain
###########################################################################

class FrameMain ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"basicallygdb v.0.1", pos = wx.DefaultPosition, size = wx.Size( 1098,646 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        middleplusbottom = wx.BoxSizer( wx.VERTICAL )
        
        middleleft = wx.BoxSizer( wx.HORIZONTAL )
        
        listfunctionsChoices = []
        self.listfunctions = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listfunctionsChoices, 0 )
        middleleft.Add( self.listfunctions, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.notebookasm = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        
        middleleft.Add( self.notebookasm, 5, wx.EXPAND |wx.ALL, 5 )
        
        
        middleplusbottom.Add( middleleft, 5, wx.EXPAND, 5 )
        
        bottombar = wx.BoxSizer( wx.VERTICAL )
        
        self.txtgdboutput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.txtgdboutput.SetFont( wx.Font( 10, 76, 90, 90, False, "Monospace" ) )
        
        bottombar.Add( self.txtgdboutput, 5, wx.ALL|wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txtgdbinput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtgdbinput.SetFont( wx.Font( 10, 76, 90, 90, False, "Monospace" ) )
        
        bSizer4.Add( self.txtgdbinput, 8, wx.ALL|wx.EXPAND, 5 )
        
        self.cmdsendgdbcommand = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.cmdsendgdbcommand, 1, wx.ALL, 5 )
        
        
        bottombar.Add( bSizer4, 2, wx.EXPAND, 5 )
        
        
        middleplusbottom.Add( bottombar, 1, wx.EXPAND, 5 )
        
        
        bSizer5.Add( middleplusbottom, 4, wx.EXPAND, 5 )
        
        rightbar = wx.BoxSizer( wx.VERTICAL )
        
        sizerdebugbuttons = wx.BoxSizer( wx.HORIZONTAL )
        
        self.cmdrun = wx.Button( self, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.Size( 10,-1 ), 0 )
        sizerdebugbuttons.Add( self.cmdrun, 1, wx.ALL, 5 )
        
        self.cmdcontinue = wx.Button( self, wx.ID_ANY, u"Cont.", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        sizerdebugbuttons.Add( self.cmdcontinue, 1, wx.ALL, 5 )
        
        self.cmdstep = wx.Button( self, wx.ID_ANY, u"Step", wx.DefaultPosition, wx.Size( 10,-1 ), 0 )
        sizerdebugbuttons.Add( self.cmdstep, 1, wx.ALL, 5 )
        
        self.cmdnext = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.Size( 10,-1 ), 0 )
        sizerdebugbuttons.Add( self.cmdnext, 1, wx.ALL, 5 )
        
        
        rightbar.Add( sizerdebugbuttons, 0, wx.EXPAND, 5 )
        
        sizerarguments = wx.BoxSizer( wx.VERTICAL )
        
        self.txtpythonargs = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.txtpythonargs.SetFont( wx.Font( 10, 76, 90, 90, False, "Monospace" ) )
        
        sizerarguments.Add( self.txtpythonargs, 7, wx.ALL|wx.EXPAND, 5 )
        
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.radiocmdargs = wx.RadioButton( self, wx.ID_ANY, u"via CMD Args", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.radiocmdargs, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.radiopipefile = wx.RadioButton( self, wx.ID_ANY, u"via File Pipe", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.radiopipefile, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        sizerarguments.Add( bSizer13, 1, wx.EXPAND, 5 )
        
        self.cmdshowargs = wx.Button( self, wx.ID_ANY, u"Eval Arguments", wx.DefaultPosition, wx.DefaultSize, 0 )
        sizerarguments.Add( self.cmdshowargs, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        rightbar.Add( sizerarguments, 3, wx.EXPAND, 5 )
        
        self.sizerregisters = wx.BoxSizer( wx.VERTICAL )
        
        
        rightbar.Add( self.sizerregisters, 6, wx.EXPAND, 5 )
        
        
        bSizer5.Add( rightbar, 1, wx.EXPAND, 5 )
        
        
        bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
    
    def __del__( self ):
        pass
    

