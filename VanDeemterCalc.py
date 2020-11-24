# -*- coding: utf-8 -*
#    VanDeemter-Plotter, a program to calculate Van-Deemter-Curves
#              
#    Copyright (C) 2020 Johannes Stoeckelmaier <j.stoeckelmaier@gmx.at>
#
#    This file is part of VanDeemter-Plotter.
#
#    VanDeemter-Plotter is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    VanDeemter-Plotter is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with VanDeemter-Plotter.  If not, see <http://www.gnu.org/licenses/>.
#
#    The main structure is based on the tutorial provided by: https://wiki.wxpython.org/AnotherTutorial#First_Steps


import wx

from src.VanDeemter_Forms import MainFrame_preset
from src.VanDeemter_Forms import AboutFrame_preset
from src.VanDeemter_Forms import FlowCalcFrame_preset

import src.VanDeemterClass as core
import src.PlottingClass as plot

#----------------------------------------------------------------------
# Programming of the GUI
#----------------------------------------------------------------------
        
class AboutFrame(AboutFrame_preset):
    def b_close_click( self, event ):
        self.Close()
    
    def AboutFrame_OnClose(self, event):
        self.Destroy()
        
        

class FlowCalcFrame(FlowCalcFrame_preset):
    def b_exitFlowCalc_click( self, event ):
        self.Close()
        
    def FlowCalcFrame_OnClose(self, event):
        self.Destroy()
        
    def b_calculate_click(self, event):
        ERROR = False
        PI = 3.1415926535
        
        try:
            inputValue = float(self.input_input.GetValue())
            print(inputValue)
        except:
            print("ERROR reading input value FlowToVol_Calc")
            ERROR = True
        
        if (ERROR == False): #Only continue if good input
            columnRadius = float(self.input_diameter.GetValue()) / 2.0
            linVel = 0.0
            flowRateSec = 0.0
            flowrateMin = 0.0
            bubbles = 0.0
                
            inputUnit = self.rb_Unit.GetSelection()
            if (inputUnit == 0): #Linear Velocity
                linVel = inputValue
                flowRateSec = ((columnRadius/10.0)**2*PI)*linVel
                flowRateMin = flowRateSec * 60.0
                bubbles = flowRateSec*10.0
            
                
            if (inputUnit == 1): #FlowRate per Sec
                linVel = inputValue/((columnRadius/10.0)**2*PI)
                flowRateSec = inputValue
                flowRateMin = flowRateSec * 60.0
                bubbles = flowRateSec*10.0
                
                
            if (inputUnit == 2): #FlowRate per Min
                linVel = (inputValue/((columnRadius/10.0)**2*PI)) * (1./60)
                flowRateSec = ((columnRadius/10.0)**2*PI)*linVel
                flowRateMin = inputValue
                bubbles = flowRateSec*10.0
                
        
            self.output_LinVel.SetValue(str(round(linVel,2)))
            self.output_FlowRateSec.SetValue(str(round(flowRateSec,2)))
            self.output_FlowRateMin.SetValue(str(round(flowRateMin,2)))
            self.output_Bubbles.SetValue(str(round(bubbles,1)))
        
        
    
class MainFrame(MainFrame_preset):
        
    def MainWindow_OnStartup( self, event ):
        self.panel = plot.CanvasPanel(self.panel_graphic)
        self.panel.clearPlot()
        
    def MainWindow_OnClose(self, event):
        self.Destroy()

    def m_close_click( self, event ):
        self.Close()
        
    def m_FlowCalc_click(self, event):
        flowCalcFrame = FlowCalcFrame(None)
        flowCalcFrame.ShowModal()

    def m_about_click( self, event ):
        aboutFrame = AboutFrame(None)
        aboutFrame.ShowModal()
            
    def b_plotGraph_click( self, event ):
        
        print("")
        print("")
        print("##############################################")
        print("#")
        print("# Start calculation ...")
        print("#")
        print("##############################################")
        self.panel.clearPlot()
        
        #Check each checkbox if ticked; if ticked, do the calculations and plot the Van-Deemter-Curve
        if (self.m_check_H2.GetValue()==True): self.calcAndPlot(mobilePhase = "H2")
        if (self.m_check_N2.GetValue()==True): self.calcAndPlot(mobilePhase = "N2")    
        if (self.m_check_He.GetValue()==True): self.calcAndPlot(mobilePhase = "He")

        if (self.m_check_Air.GetValue()==True): self.calcAndPlot(mobilePhase = "Air")
        if (self.m_check_Methane.GetValue()==True): self.calcAndPlot(mobilePhase = "CH4")    
        if (self.m_check_CO2.GetValue()==True): self.calcAndPlot(mobilePhase = "CO2")
        if (self.m_check_N2O.GetValue()==True): self.calcAndPlot(mobilePhase = "N2O") 
        if (self.m_check_Butane.GetValue()==True): self.calcAndPlot(mobilePhase = "Butane") 
          

    def slider_dp_changed( self, event ):
        #Update un moved slider
        event.Skip()

    def calcAndPlot(self, mobilePhase):
        vanDeemterCurve = core.VanDeemterGraph(self, mobilePhase = mobilePhase)
        ux, H, uOpt, hMin = vanDeemterCurve.calcOptimumParam()
        
        farbe = "red"
        labelText = mobilePhase
        
        if (mobilePhase=="H2"): farbe = "b"; labelText = r'$H_{2}$'
        if (mobilePhase=="He"): farbe = "g"; labelText = r'$He$'
        if (mobilePhase=="N2"): farbe = "r"; labelText = r'$N_{2}$'
    
        if (mobilePhase=="Air"): farbe = "m"; labelText = r'$Air$'
        if (mobilePhase=="CH4"): farbe = "c"; labelText = r'$CH_{4}$'
        if (mobilePhase=="CO2"): farbe = "k"; labelText = r'$CO_{2}$'
        if (mobilePhase=="N2O"): farbe = "gold"; labelText = r'$N_{2}O$'
        if (mobilePhase=="Butane"): farbe = "darkorange" ; labelText = r'$n-Butane$'
        
        self.panel.plotVanDeemter(ux, H, labelText = labelText, plotColor=farbe)
        self.panel.plotOptParam(uOpt, hMin, plotColor=farbe)

#----------------------------------------------------------------------
# StartUp Application
#----------------------------------------------------------------------

class Application(wx.App):
    def OnInit(self):
        frame = MainFrame(None)
        self.SetTopWindow(frame)
       
        #Set minimum size of the window
        sizeOfFrame = frame.GetSize()
        frame.SetMinSize((sizeOfFrame[0], sizeOfFrame[1]))
        
        #Set Icon
        frame.SetIcon(wx.Icon("./img/icon.png"))

        frame.Show(True)
        return True
        
if __name__ == '__main__':    
    main = Application(redirect=False)
    main.MainLoop()
