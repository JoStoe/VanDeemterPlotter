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


import numpy as np
        
class VanDeemterGraph():
    def __init__(self,parent,mobilePhase):
        ##########################################
        #
        # Init the calculation of the Van-Deemter Curve
        #
        
        self.parent = parent #Set used Window

        tr = 80
        tm = 20

        #Set Parameters
        self.dp = parent.slider_dp.GetValue()*1e-6 #50*10e-6   #Partikeldurchmesser µm
        
        self.T = parent.slider_T.GetValue()+273.15    #Temperatur Kelvin
        self.pressure = parent.slider_pressure.GetValue()    #pressure in mbar
        self.mobilePhase = mobilePhase
        
        #Set Values for DGas
        self.Dgas = 1.63*1e-5  ##1.63*10e-5   #Ethane in N2; standardValue
        if (self.mobilePhase=="H2"): self.Dgas = self.evaluateFullerEqu(self.T,self.pressure,7.07,2) 
        if (self.mobilePhase=="He"): self.Dgas = self.evaluateFullerEqu(self.T,self.pressure,2.88,4)
        if (self.mobilePhase=="N2"): self.Dgas = self.evaluateFullerEqu(self.T,self.pressure,17.9,28)
 
        if (self.mobilePhase=="Air"): self.Dgas = self.evaluateFullerEqu(self.T,self.pressure,20.1,28.8) 
        if (self.mobilePhase=="CH4"): self.Dgas = self.evaluateFullerEqu(self.T,self.pressure,24.42,16.04) 
        if (self.mobilePhase=="CO2"): self.Dgas = self.evaluateFullerEqu(self.T,self.pressure,26.9,44.01)  
        if (self.mobilePhase=="N2O"): self.Dgas = self.evaluateFullerEqu(self.T,self.pressure,35.9,44.013)         
        if (self.mobilePhase=="Butane"): self.Dgas = self.evaluateFullerEqu(self.T,self.pressure,85.8,58.12)  
        
        #Set Values for Dliq
        self.Dliq = 1.3*1e-10   #Standardwert von Van-Deempter Paper, Seite 282
        if (self.mobilePhase=="H2"): self.Dliq = self.evauateWilkeChang(14.3, self.T)
        if (self.mobilePhase=="He"): self.Dliq = self.evauateWilkeChang(16.0, self.T)
        if (self.mobilePhase=="N2"): self.Dliq = self.evauateWilkeChang(31.1, self.T)

        if (self.mobilePhase=="Air"): self.Dliq = self.evauateWilkeChang(29.9, self.T)
        if (self.mobilePhase=="CH4"): self.Dliq = self.evauateWilkeChang(29.6, self.T)
        if (self.mobilePhase=="CO2"): self.Dliq = self.evauateWilkeChang(34.0, self.T)
        if (self.mobilePhase=="N2O"): self.Dliq = self.evauateWilkeChang(36.4, self.T)
        if (self.mobilePhase=="Butane"): self.Dliq = self.evauateWilkeChang(96.2, self.T)       
        
        if (parent.choice_particleQuality.GetSelection()==0):
            print("High quality column")
            self.particleQuality = "high"
            self.lamda = self.lambda_HQ(self.dp*1e6)
            self.gamma = 0.6
        elif (parent.choice_particleQuality.GetSelection()==1):
            print("Low quality column")
            self.particleQuality = "low"
            self.lamda = self.lambda_LQ(self.dp*1e6)
            self.gamma = 0.6
        else:
            print("A-Term disabled")
            self.particleQuality = "NONE"
            self.lamda = 1e-6
            self.gamma = 1.0
        
        self.k = (tr-tm)/tm
        self.df = parent.slider_df.GetValue()*1e-6 # 10*10e-6   #10microns, #Wert von Van-Deempter Paper, Seite 286
    
    def lambda_HQ(self, dp):
        #dp input in µm
        print("Dp: ",dp)
        return 0.5
    
    def lambda_LQ(self, dp):
        #dp input in µm
        print("Dp: ",dp)
        return 2.0

    def silicone100k_Visc(self, temperature): #Return Viscosity for silicone-oil cst100000
        cst = (100000*np.exp(1683*((1./temperature)-(1./298.0))))
        density = 0.977
        return cst * density * 0.001 #Returns in Pa*s
    
    def evauateWilkeChang(self, nbpVolume, temperature):

        prefactor = 7.48849937e-16
        weight = 139000
        
        nbpVolume_Toluen=118.2
        diffusity_analyte = prefactor * (weight**0.5) * temperature * 1./((self.silicone100k_Visc(temperature)) * (nbpVolume_Toluen/1000)**2.24)
        print("Diffusity analyte (Dliq): [m2/sec]", diffusity_analyte)
        
        """
        #Code for Diffusity mixxing
        diffusity_carrier = prefactor * (weight**0.5) * temperature * 1./((self.silicone100k_Visc(temperature)) * (nbpVolume/1000)**2.24)
        print("Diffusity carrier-gas (Dliq): [m2/sec]", diffusity_carrier)

        mixxing = 98.5 #Value between 0 and 100
        diffusity = (mixxing * diffusity_analyte + (100-mixxing)*diffusity_carrier)/100
        print("Mixxed diffusity  (Dliq): [m2/sec]", diffusity)
        """
        
        diffusity = diffusity_analyte
        return diffusity
    
    
    def evaluateFullerEqu(self, temperature, pressure, diffVol1, mass1 ):

        #Toluol
        diffVol2 = 111.14
        mass2 = 92.14
        pressure = pressure * 9.869*(10**-4) #Convert mbar to atm
        print("Average Column Preassure: [atm]", pressure)

        #Fuller equation
        uppderFraction = (1e-3*(temperature**1.75)*(1./mass1 + 1./mass2)**0.5) 
        lowerFraction = pressure*((diffVol1)**(1./3.)+(diffVol2)**(1./3.))**2
        diffusity = uppderFraction / lowerFraction
        
        print("Dgas: [m2/sec]", (diffusity * 1e-4))
        return (diffusity * 1e-4) #return in m2/s 
    
        
    def calcOptimumParam(self):
        #!!Die Trennleistung wird besser wenn Dliq größer und Dgas kleiner wird.
    
        self.ux = np.linspace(0.1/1000.0,500.0/1000.0,500)
        A = 2.0 * self.lamda * self.dp
        B = 2.0 * self.gamma * self.Dgas
        #C = (8.0/(np.pi**2.0)) * (self.k/((1.0+self.k)**2.0)) * (self.df**2.0)/(self.Dliq)
        
        Cs = (2.0/3.0) * (self.k/((1.0+self.k)**2.0)) * (self.df**2.0)/(self.Dliq)

        pref = ((1.0 + 6.0*self.k + 11.0*(self.k**2))/(24.0*((1.0 + self.k)**2.0)))
        Cm =  pref*((self.dp**2)/self.Dgas)#*(1.0/96)
        C =  Cs + Cm
        Cavg = np.average(C)
          
        self.H = A + B/self.ux + Cavg*self.ux
    
        uOpt = np.sqrt(B/C)
        hMin = A + 2*np.sqrt(B*C)
            
        #Print calculated Values if DEBUG is enabled
        DEBUG = False
        if (DEBUG==True):
            print("u optimum = ", uOpt*1000, " mm/sec")
            print("h minimum = ", hMin*1000, " mm")
        
            print("A: ", A , " m")
            print("B: ", B , " m^2/sec")
            print("C: ", Cavg, " sec")
        
        #Wirte "VanDeemterParam.dat" File
        f = open("VanDeemterParam.dat", "w")
        f.write("This file contains the Van-Deemter-parameters for a specific separation condition.\n")
        f.write("carrier_gas=" + self.mobilePhase + "\n")
        f.write("dp=" + str(self.dp) + "\n")
        f.write("lambda=" + str(self.lamda) + "\n")
        f.write("df=" + str(self.df) + "\n")
        f.write("Dgas=" + str(self.Dgas) + "\n")
        f.write("Dliq=" + str(self.Dliq) + "\n")
        f.close()
        
        if (DEBUG==True):
            np.savetxt("curve.txt", np.column_stack((self.ux, self.H)), delimiter=',') #Save calculated curve to file
        
        return self.ux, self.H, uOpt, hMin
    
    
