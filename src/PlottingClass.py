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


import wx

import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
matplotlib.use('WXAgg')

#Set the fontsize of graphics globally
matplotlib.rcParams.update({'font.size': 16})


#----------------------------------------------------------------------
#plot an 2D-Array
#----------------------------------------------------------------------
class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent = parent)
        
        #Create the graphical panel
        width,height = parent.GetSize()
        self.figure = Figure(figsize=(width/90,height/90),dpi=90)
        self.canvas = FigureCanvas(parent, -1, self.figure)
        self.axes = self.figure.add_subplot(1, 1, 1)
 
        #Size the Graphical output
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND, 5)
        parent.SetSizer( self.sizer )
        self.Fit()

    def plot(self,data,labelText):
        
        #self.axes.clear()
        x = data[:,0]
        y = data[:,1]
        self.axes.plot(x,y,label=labelText)
        
        #Do the labeling
        self.axes.set_xlabel("ux [mm/sec]")
        self.axes.set_ylabel("H [mm]")
        self.axes.legend()
        
        self.canvas.draw()
        
    def clearPlot(self):
        self.axes.clear()
        #Do the labeling
        self.axes.set_xlabel("ux [mm/sec]")
        self.axes.set_ylabel("H [mm]")
        self.canvas.draw()
        
    def plotVanDeemter(self, ux, H, labelText, plotColor):
        self.axes.plot(ux*100,H*1000,label=labelText, color=plotColor, linewidth=2.5)
        
        #Do the labeling
        self.axes.set_xlabel("ux [cm/sec]")
        self.axes.set_ylabel("H [mm]")
        self.axes.set_xlim(0,50)
        self.axes.set_ylim(0,6.0)
        
        #self.axes.legend(prop={'weight':'bold'})
        self.axes.legend()
        
        self.canvas.draw()
    
    
    def plotOptParam(self, uOpt, hMin, plotColor):
        #plot horizontal line (hMin)
        self.axes.hlines(y=hMin*1000, xmin = 0.0, xmax = uOpt*100, linestyle='--', color=plotColor, linewidth=0.75)
        #Do the labeling
        self.axes.set_yticks(list(self.axes.get_yticks()) + [hMin*1000])
        labels = self.axes.get_yticklabels()
        labels[-1].set_text(str("{0:.1f}".format(round(hMin*1000,1))))
        labels[-1].set_position([-0.04,0.0])
        labels[-1].set_color(plotColor)
        self.axes.set_yticklabels(labels, rotation=0, ha='center')    
        
        
        #plot vertical line (uOpt)
        self.axes.vlines(x=uOpt*100, ymin = 0.0, ymax = hMin*1000, linestyle='--', color=plotColor, linewidth=0.75)
        #Do the labeling
        self.axes.set_xticks(list(self.axes.get_xticks()) + [uOpt*100])
        labels = self.axes.get_xticklabels()
        labels[-1].set_text(str("{0:.1f}".format(round(uOpt*100,1))))
        labels[-1].set_position([0.0,-0.02])
        labels[-1].set_color(plotColor)
        self.axes.set_xticklabels(labels, rotation=45, ha='center')
        
        self.canvas.draw()
