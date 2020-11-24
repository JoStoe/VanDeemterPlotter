# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame_preset
###########################################################################

class MainFrame_preset ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"VanDeemter-Plotter", pos = wx.DefaultPosition, size = wx.Size( 1400,950 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_close = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_close )

		self.m_menubar1.Append( self.m_menu1, u"Files" )

		self.m_menu2 = wx.Menu()
		self.m_FlowCalc = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Flow Calculator", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_FlowCalc )

		self.m_about = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_about )

		self.m_menubar1.Append( self.m_menu2, u"Help" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.panel_graphic = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_graphic.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer4.Add( self.panel_graphic, 1, wx.ALL|wx.EXPAND, 0 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.b_plotGraph = wx.Button( self, wx.ID_ANY, u"Simulate Curves", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.b_plotGraph.SetToolTip( u"Connect you detector and start measuring data." )

		bSizer3.Add( self.b_plotGraph, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Particle size dp [µm]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Column radius dr [µm]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.slider_dp = wx.Slider( self, wx.ID_ANY, 200, 30, 400, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer3.Add( self.slider_dp, 0, wx.ALL|wx.EXPAND, 5 )

		choice_particleQualityChoices = [ u"High", u"Low", u"disable A-Term" ]
		self.choice_particleQuality = wx.RadioBox( self, wx.ID_ANY, u"Quality of particle-shape", wx.DefaultPosition, wx.DefaultSize, choice_particleQualityChoices, 1, wx.RA_SPECIFY_COLS )
		self.choice_particleQuality.SetSelection( 0 )
		bSizer3.Add( self.choice_particleQuality, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Liquid film thickness df [µm]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.slider_df = wx.Slider( self, wx.ID_ANY, 8, 1, 20, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS|wx.SL_VALUE_LABEL )
		bSizer3.Add( self.slider_df, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Temperature [°C]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.slider_T = wx.Slider( self, wx.ID_ANY, 200, 20, 300, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS|wx.SL_VALUE_LABEL )
		bSizer3.Add( self.slider_T, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Avg. column preassure [mBar]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.slider_pressure = wx.Slider( self, wx.ID_ANY, 1200, 500, 2000, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS|wx.SL_VALUE_LABEL )
		bSizer3.Add( self.slider_pressure, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.t_mobilePhase = wx.StaticText( self, wx.ID_ANY, u"Select mobile phase", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.t_mobilePhase.Wrap( -1 )

		bSizer3.Add( self.t_mobilePhase, 0, wx.ALL, 5 )

		self.m_check_H2 = wx.CheckBox( self, wx.ID_ANY, u"H2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_check_H2.SetValue(True)
		bSizer3.Add( self.m_check_H2, 0, wx.ALL, 5 )

		self.m_check_N2 = wx.CheckBox( self, wx.ID_ANY, u"N2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_check_N2.SetValue(True)
		bSizer3.Add( self.m_check_N2, 0, wx.ALL, 5 )

		self.m_check_He = wx.CheckBox( self, wx.ID_ANY, u"He", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_check_He.SetValue(True)
		bSizer3.Add( self.m_check_He, 0, wx.ALL, 5 )

		self.m_check_Air = wx.CheckBox( self, wx.ID_ANY, u"Air", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_check_Air, 0, wx.ALL, 5 )

		self.m_check_Methane = wx.CheckBox( self, wx.ID_ANY, u"Methane", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_check_Methane, 0, wx.ALL, 5 )

		self.m_check_CO2 = wx.CheckBox( self, wx.ID_ANY, u"CO2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_check_CO2, 0, wx.ALL, 5 )

		self.m_check_N2O = wx.CheckBox( self, wx.ID_ANY, u"N2O", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_check_N2O, 0, wx.ALL, 5 )

		self.m_check_Butane = wx.CheckBox( self, wx.ID_ANY, u"Butane", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_check_Butane, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer3, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.MainWindow_OnClose )
		self.Bind( wx.EVT_SHOW, self.MainWindow_OnStartup )
		self.Bind( wx.EVT_MENU, self.m_close_click, id = self.m_close.GetId() )
		self.Bind( wx.EVT_MENU, self.m_FlowCalc_click, id = self.m_FlowCalc.GetId() )
		self.Bind( wx.EVT_MENU, self.m_about_click, id = self.m_about.GetId() )
		self.b_plotGraph.Bind( wx.EVT_BUTTON, self.b_plotGraph_click )
		self.slider_dp.Bind( wx.EVT_SCROLL, self.slider_dp_changed )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def MainWindow_OnClose( self, event ):
		event.Skip()

	def MainWindow_OnStartup( self, event ):
		event.Skip()

	def m_close_click( self, event ):
		event.Skip()

	def m_FlowCalc_click( self, event ):
		event.Skip()

	def m_about_click( self, event ):
		event.Skip()

	def b_plotGraph_click( self, event ):
		event.Skip()

	def slider_dp_changed( self, event ):
		event.Skip()


###########################################################################
## Class FlowCalcFrame_preset
###########################################################################

class FlowCalcFrame_preset ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 416,487 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 7, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.VERTICAL )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.input_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_NO_VSCROLL )
		self.input_input.SetMaxLength( 10 )
		fgSizer2.Add( self.input_input, 0, wx.ALL|wx.EXPAND, 5 )

		rb_UnitChoices = [ u"Linear velocity [cm/sec]", u"Flow-rate [ml/sec]", u"Flow-rate [ml/min]" ]
		self.rb_Unit = wx.RadioBox( self, wx.ID_ANY, u"Choose Unit", wx.DefaultPosition, wx.DefaultSize, rb_UnitChoices, 1, wx.RA_SPECIFY_COLS )
		self.rb_Unit.SetSelection( 0 )
		fgSizer2.Add( self.rb_Unit, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"Column Diameter [mm]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		fgSizer2.Add( self.m_staticText101, 0, wx.ALL, 5 )

		self.input_diameter = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0.01, 15, 4, 0.01 )
		self.input_diameter.SetDigits( 2 )
		fgSizer2.Add( self.input_diameter, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Linear velocity [cm/sec]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.EXPAND, 5 )

		self.output_LinVel = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer2.Add( self.output_LinVel, 5, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Flow-rate [ml/sec]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer2.Add( self.m_staticText9, 0, wx.ALL|wx.EXPAND, 5 )

		self.output_FlowRateSec = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer2.Add( self.output_FlowRateSec, 5, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Flow-rate [ml/min]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer2.Add( self.m_staticText11, 5, wx.ALL|wx.EXPAND, 5 )

		self.output_FlowRateMin = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer2.Add( self.output_FlowRateMin, 5, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"estim. bubbles per sec.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer2.Add( self.m_staticText12, 0, wx.ALL|wx.EXPAND, 5 )

		self.output_Bubbles = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer2.Add( self.output_Bubbles, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer8.Add( fgSizer2, 1, wx.ALL|wx.EXPAND, 5 )

		self.b_calculate = wx.Button( self, wx.ID_ANY, u"Calculate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.b_calculate, 0, wx.ALL|wx.EXPAND, 10 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer8.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.b_exitFlowCalc = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.b_exitFlowCalc, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FlowCalcFrame_OnClose )
		self.b_calculate.Bind( wx.EVT_BUTTON, self.b_calculate_click )
		self.b_exitFlowCalc.Bind( wx.EVT_BUTTON, self.b_exitFlowCalc_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def FlowCalcFrame_OnClose( self, event ):
		event.Skip()

	def b_calculate_click( self, event ):
		event.Skip()

	def b_exitFlowCalc_click( self, event ):
		event.Skip()


###########################################################################
## Class AboutFrame_preset
###########################################################################

class AboutFrame_preset ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About Van-Deemter Plotter", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"img/about_banner.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap1, 0, wx.ALL|wx.EXPAND, 0 )

		self.t_licenseInfo = wx.TextCtrl( self, wx.ID_ANY, u"Van-Deemter Plotter Version 1.0\n2020 Johannes Stöckelmaier\n\n\nFor this project, open-source software was used:\nPython (PSF license)\nNumPy (NumPy license)\nMatplotlib (BSD compatible licenses)\nWxWidgets (wxWindows Library Licence 3.1)\nWxPython (wxWindows Library Licence 3.1)\n\n\nParts of the source-code were auto-generated by wxFormBuilder", wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer2.Add( self.t_licenseInfo, 5, wx.ALL|wx.EXPAND, 5 )

		self.b_close = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.b_close, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		bSizer2.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.AboutFrame_OnClose )
		self.b_close.Bind( wx.EVT_BUTTON, self.b_close_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def AboutFrame_OnClose( self, event ):
		event.Skip()

	def b_close_click( self, event ):
		event.Skip()


