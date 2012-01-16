# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec  2 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class PySpendGUI
###########################################################################

class PySpendGUI ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PySpend", pos = wx.DefaultPosition, size = wx.Size( 600,475 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook2 = wx.Notebook( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.item_panel = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel9 = wx.Panel( self.item_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer12.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.date_picker = wx.DatePickerCtrl( self.m_panel9, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		bSizer12.Add( self.date_picker, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.date_spin = wx.SpinButton( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.Size( 20,21 ), 0 )
		bSizer12.Add( self.date_spin, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.m_panel9.SetSizer( bSizer12 )
		self.m_panel9.Layout()
		bSizer12.Fit( self.m_panel9 )
		bSizer7.Add( self.m_panel9, 0, wx.EXPAND |wx.ALL, 0 )
		
		fgSizer3 = wx.FlexGridSizer( 2, 4, 0, 0 )
		fgSizer3.AddGrowableCol( 0 )
		fgSizer3.AddGrowableCol( 1 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText6 = wx.StaticText( self.item_panel, wx.ID_ANY, u"Category", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer3.Add( self.m_staticText6, 0, wx.ALL, 3 )
		
		self.m_staticText7 = wx.StaticText( self.item_panel, wx.ID_ANY, u"Item", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer3.Add( self.m_staticText7, 0, wx.ALL, 3 )
		
		self.m_staticText8 = wx.StaticText( self.item_panel, wx.ID_ANY, u"Cost (p)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer3.Add( self.m_staticText8, 0, wx.ALL, 3 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 3 )
		
		categoryChoices = []
		self.category = wx.ComboBox( self.item_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, categoryChoices, wx.CB_READONLY )
		fgSizer3.Add( self.category, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 3 )
		
		self.name = wx.TextCtrl( self.item_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.name, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 3 )
		
		self.cost = wx.TextCtrl( self.item_panel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		fgSizer3.Add( self.cost, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.add_item = wx.Button( self.item_panel, wx.ID_ADD, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.add_item, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		bSizer7.Add( fgSizer3, 0, wx.EXPAND, 3 )
		
		self.item_list = wx.ListCtrl( self.item_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer7.Add( self.item_list, 1, wx.ALL|wx.EXPAND, 3 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText10 = wx.StaticText( self.item_panel, wx.ID_ANY, u"Total cost", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer11.Add( self.m_staticText10, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.total_cost = wx.StaticText( self.item_panel, wx.ID_ANY, u"£0", wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE )
		self.total_cost.Wrap( -1 )
		bSizer11.Add( self.total_cost, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer11.AddSpacer( ( 26, 0), 0, wx.EXPAND, 3 )
		
		bSizer7.Add( bSizer11, 0, wx.EXPAND, 3 )
		
		self.item_panel.SetSizer( bSizer7 )
		self.item_panel.Layout()
		bSizer7.Fit( self.item_panel )
		self.m_notebook2.AddPage( self.item_panel, u"Items", True )
		self.cat_panel = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel6 = wx.Panel( self.cat_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"New category", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer6.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.cat_text = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.cat_text, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.add_cat = wx.Button( self.m_panel6, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.add_cat, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_panel6.SetSizer( bSizer6 )
		self.m_panel6.Layout()
		bSizer6.Fit( self.m_panel6 )
		bSizer5.Add( self.m_panel6, 0, wx.EXPAND |wx.ALL, 3 )
		
		self.cat_list = wx.ListCtrl( self.cat_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer5.Add( self.cat_list, 1, wx.ALL|wx.EXPAND, 3 )
		
		self.cat_panel.SetSizer( bSizer5 )
		self.cat_panel.Layout()
		bSizer5.Fit( self.cat_panel )
		self.m_notebook2.AddPage( self.cat_panel, u"Categories", False )
		
		bSizer2.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 3 )
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.menu_delete = wx.Menu()
		self.menu_delete_item = wx.MenuItem( self.menu_delete, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_delete.AppendItem( self.menu_delete_item )
		
		self.Bind( wx.EVT_RIGHT_DOWN, self.PySpendGUIOnContextMenu ) 
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
	def PySpendGUIOnContextMenu( self, event ):
		self.PopupMenu( self.menu_delete, event.GetPosition() )
		

