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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 951,584 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        listfunctionsChoices = []
        self.listfunctions = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listfunctionsChoices, 0 )
        bSizer2.Add( self.listfunctions, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.notebookasm = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        
        bSizer2.Add( self.notebookasm, 5, wx.EXPAND |wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer2, 4, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.txtgdboutput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.txtgdboutput.SetFont( wx.Font( 10, 76, 90, 90, False, "Monospace" ) )
        
        bSizer3.Add( self.txtgdboutput, 5, wx.ALL|wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txtgdbinput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtgdbinput.SetFont( wx.Font( 10, 76, 90, 90, False, "Monospace" ) )
        
        bSizer4.Add( self.txtgdbinput, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.cmdsendgdbcommand = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.cmdsendgdbcommand, 0, wx.ALL, 5 )
        
        
        bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        
        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
    
    def __del__( self ):
        pass
    

