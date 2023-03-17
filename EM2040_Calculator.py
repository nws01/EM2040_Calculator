# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 01:20:56 2020

@author: postmodernic

Build 1.1
Released: 27.12.2020
Added:
Updated settings and pulse lengths from KM Support

"""

from tkinter import*
import tkinter as tk
from tkinter.ttk import *
import math
import time
import tkinter.ttk as ttk
import decimal 
from tkinter.ttk import *
import math
from math import *
import time
import pathlib, os


WIDTH = 1600
HEIGHT = 800
windowed=True 
console=False


#=============================1.0 GENERAL USER intERFACE=============================================================================

root = tk.Tk()
root.title("EM2040 Calculator")
root.resizable(False, False)


        
#===================1.1 FRAMES=======================================================================================================
canvas =  tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

current_dir = pathlib.Path(__file__).parent.resolve() #set working directory
image_file_name = "bathy1.png"
background_image = tk.PhotoImage(file=os.path.join(current_dir, image_file_name))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
label_colour = '#484B51'
entry_colour = 'white'
result_colour = 'black'



#===================1.2 VARIABLES=======================================================================================================

swathwidth = tk.StringVar()
bathycoverage = tk.StringVar()
bathyoverlap = tk.StringVar()
effectiveangle = tk.StringVar()
slantrange = tk.StringVar()
gridping = tk.StringVar()
pingrate = tk.StringVar()
swathrate = tk.StringVar()
transmissionloss = tk.StringVar()
beamsperping = tk.StringVar()
pulselength = tk.StringVar()
pulsetype = tk.StringVar()

swathwidth.set(0) 
bathycoverage.set(0) 
bathyoverlap.set(0) 
effectiveangle.set(0)  
slantrange.set(0) 
gridping.set(0) 
pingrate.set(0)
swathrate.set(0)
transmissionloss.set(0)
beamsperping.set(0)
pulselength.set(0)
pulsetype.set(0)


#===================1.3 USER INPUT MBES============================================================================================
#Column1:
MBEStype_Label = tk.Label(bg=(label_colour), text="MBES:", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
MBEStype_Label.place(relx=0.03, rely=0.05, relwidth=0.15, relheight=0.05)

MBEStype = tk.Label(bg=("white"), text="KM EM2040", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
MBEStype.place(relx=0.18, rely=0.05, relwidth=0.1, relheight=0.05)

Swathtype_Label = tk.Label(bg=(label_colour), text="Swath Type:", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
Swathtype_Label.place(relx=0.03, rely=0.11, relwidth=0.15, relheight=0.05)

Swathtype_Combobox = ttk.Combobox(justify='center', values=["Single", "Dual"])
Swathtype_Combobox.place(relx=0.18, rely=0.11, relwidth=0.1, relheight=0.05)

Beamwidth_Label = tk.Label(bg=(label_colour), text="Beam Width:", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
Beamwidth_Label.place(relx=0.03, rely=0.17, relwidth=0.15, relheight=0.05)

Beamwidth_Combobox = ttk.Combobox(justify='center', values=["0.4° x 0.7°", "0.7° x 0.7°"])
Beamwidth_Combobox.place(relx=0.18, rely=0.17, relwidth=0.1, relheight=0.05)

Freq_Label = tk.Label(bg=(label_colour), text="Transmit Frequency (kHz):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
Freq_Label.place(relx=0.03, rely=0.23, relwidth=0.15, relheight=0.05)

Freq_Combobox = ttk.Combobox(justify='center', values=["200", "300", "400"])
Freq_Combobox.place(relx=0.18, rely=0.23, relwidth=0.1, relheight=0.05)

BeamSpacing_label = tk.Label(bg=(label_colour), text="Beam Spacing :", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
BeamSpacing_label.place(relx=0.03, rely=0.29, relwidth=0.15, relheight=0.05)

BeamSpacing_combobox = ttk.Combobox(justify='center', values=["Equidistance", "Equiangle", "High Density", "Ultra High Density"])
BeamSpacing_combobox.place(relx=0.18, rely=0.29, relwidth=0.1, relheight=0.05)

DepthMode_label = tk.Label(bg=(label_colour), text="Depth Mode :", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
DepthMode_label.place(relx=0.03, rely=0.35, relwidth=0.15, relheight=0.05)

DepthMode_combobox = ttk.Combobox(justify='center', values=["Shallow", "Medium", "Deep", "Very Deep"])
DepthMode_combobox.place(relx=0.18, rely=0.35, relwidth=0.1, relheight=0.05)

MaxSwathAngle_Label = tk.Label(bg=(label_colour), text="Total Max Swath Angle (°):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
MaxSwathAngle_Label.place(relx=0.03, rely=0.41, relwidth=0.15, relheight=0.050)

MaxSwathAngle_Entry = tk.Entry(bg=(entry_colour), justify='center') 
MaxSwathAngle_Entry.place(relx=0.18, rely=0.41, relwidth=0.1, relheight=0.05)

MaxSwathCoverage_Label = tk.Label(bg=(label_colour), text="Max Swath Coverage (m):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
MaxSwathCoverage_Label.place(relx=0.03, rely=0.47, relwidth=0.15, relheight=0.050)

MaxSwathCoverage_Entry = tk.Entry(bg=(entry_colour), justify='center') 
MaxSwathCoverage_Entry.place(relx=0.18, rely=0.47, relwidth=0.1, relheight=0.05)

LineSpacing_Label = tk.Label(bg=(label_colour), text="Line Spacing (m):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
LineSpacing_Label.place(relx=0.03, rely=0.53, relwidth=0.15, relheight=0.050)

LineSpacing_Entry = tk.Entry(bg=(entry_colour), justify='center') 
LineSpacing_Entry.place(relx=0.18, rely=0.53, relwidth=0.1, relheight=0.05)

WaterDepth_Label = tk.Label(bg=(label_colour), text="Water Depth (m):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
WaterDepth_Label.place(relx=0.03, rely=0.59, relwidth=0.15, relheight=0.05)

WaterDepth_Entry = tk.Entry(bg=(entry_colour), justify='center') 
WaterDepth_Entry.place(relx=0.18, rely=0.59, relwidth=0.1, relheight=0.05)

#Column2:

Grid_Label = tk.Label(bg=(label_colour), text="Grid Size (m^2):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
Grid_Label.place(relx=0.35, rely=0.05, relwidth=0.15, relheight=0.05)

Grid_Entry = tk.Entry(bg=(entry_colour), justify='center') 
Grid_Entry.place(relx=0.50, rely=0.05, relwidth=0.1, relheight=0.05)

txmode_label = tk.Label(bg=(label_colour), text="Select Transmit Mode  :", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
txmode_label.place(relx=0.35, rely=0.11, relwidth=0.15, relheight=0.05)

txmode_combobox = ttk.Combobox(justify='center', values=["FM Enabled", "FM Disabled"])
txmode_combobox.place(relx=0.50, rely=0.11, relwidth=0.1, relheight=0.05)

SV_label = tk.Label(bg=(label_colour), text="Mean Sound Velocity (m/s):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
SV_label.place(relx=0.35, rely=0.17, relwidth=0.15, relheight=0.05)

SV_Entry = tk.Entry(bg=(entry_colour), justify='center') 
SV_Entry.place(relx=0.50, rely=0.17, relwidth=0.1, relheight=0.05)

Speed_label = tk.Label(bg=(label_colour), text="Vessel Survey Speed  (kts):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
Speed_label.place(relx=0.35, rely=0.23, relwidth=0.15, relheight=0.05)

Speed_Entry = tk.Entry(bg=(entry_colour), justify='center') 
Speed_Entry.place(relx=0.50, rely=0.23, relwidth=0.1, relheight=0.05)
    
mbesbutton = tk.Button(text="Calculate", bg='black', fg='white', font=('Calibri', 14, 'bold'), command=lambda: mbesresults()) #command=lambda: calculate()) #bg = background, fg = foreground
mbesbutton.place(relx=0.35, rely = 0.47, relwidth=0.25, relheight=0.11)





#===================1.4 MBES RESULTS DISPLAY===========================================================================================

#Column3:

SwathWidth_Label = tk.Label(bg=(label_colour), text="Swath Width (m):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
SwathWidth_Label.place(relx=0.67, rely=0.05, relwidth=0.15, relheight=0.05)

SawthWidth_Result = tk.Label(bg=(result_colour), textvariable=swathwidth, fg='white', justify='center', font=('Calibri', 14, 'bold'))
SawthWidth_Result.place(relx=0.82, rely=0.05, relwidth=0.1, relheight=0.05)

Coverage_Label = tk.Label(bg=(label_colour), text="Bathymetric Coverage (%):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
Coverage_Label.place(relx=0.67, rely=0.11, relwidth=0.15, relheight=0.05)

Coverage_Result = tk.Label(bg=(result_colour), textvariable=bathycoverage, fg='white', justify='center', font=('Calibri', 14, 'bold'))
Coverage_Result.place(relx=0.82, rely=0.11, relwidth=0.1, relheight=0.05)

Overlap_Label = tk.Label(bg=(label_colour), text="Bathymetric Overlap (%):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
Overlap_Label.place(relx=0.67, rely=0.17, relwidth=0.15, relheight=0.05)

Overlap_Result = tk.Label(bg=(result_colour), textvariable=bathyoverlap, fg='white', justify='center', font=('Calibri', 14, 'bold'))
Overlap_Result.place(relx=0.82, rely=0.17, relwidth=0.1, relheight=0.05)

EffectiveAngle_Label = tk.Label(bg=(label_colour), text="Effective Swath Angle (°):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
EffectiveAngle_Label.place(relx=0.67, rely=0.23, relwidth=0.15, relheight=0.05)

EffectiveAngle_Result = tk.Label(bg=(result_colour), textvariable=effectiveangle, fg='white', justify='center', font=('Calibri', 14, 'bold'))
EffectiveAngle_Result.place(relx=0.82, rely=0.23, relwidth=0.1, relheight=0.05)

SlantRange_Label = tk.Label(bg=(label_colour), text="Outer Slant Range (m):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
SlantRange_Label.place(relx=0.67, rely=0.29, relwidth=0.15, relheight=0.05)

SlantRange_Result = tk.Label(bg=(result_colour), textvariable=slantrange, fg='white', justify='center', font=('Calibri', 14, 'bold'))
SlantRange_Result.place(relx=0.82, rely=0.29, relwidth=0.1, relheight=0.05)



PingRate_Label = tk.Label(bg=(label_colour), text="Ping Rate (Hz):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
PingRate_Label.place(relx=0.67, rely=0.35, relwidth=0.15, relheight=0.05)

PingRate_Result = tk.Label(bg=(result_colour), textvariable=pingrate, fg='white', justify='center', font=('Calibri', 14, 'bold'))
PingRate_Result.place(relx=0.82, rely=0.35, relwidth=0.1, relheight=0.05)

SwathRate_Label = tk.Label(bg=(label_colour), text="Swath Rate (Hz):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
SwathRate_Label.place(relx=0.67, rely=0.41, relwidth=0.15, relheight=0.05)

SwathRate_Result = tk.Label(bg=(result_colour), textvariable=swathrate, fg='white', justify='center', font=('Calibri', 14, 'bold'))
SwathRate_Result.place(relx=0.82, rely=0.41, relwidth=0.1, relheight=0.05)

GridPing_Label = tk.Label(bg=(label_colour), text="Soundings per Grid:", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
GridPing_Label.place(relx=0.67, rely=0.47, relwidth=0.15, relheight=0.05)

GridPing_Result = tk.Label(bg=(result_colour), textvariable=gridping, fg='white', justify='center', font=('Calibri', 14, 'bold'))
GridPing_Result.place(relx=0.82, rely=0.47, relwidth=0.1, relheight=0.05)

PulseType_Label = tk.Label(bg=(label_colour), text="Pulse Type Used:", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
PulseType_Label.place(relx=0.67, rely=0.53, relwidth=0.15, relheight=0.05)

PulseType_Result = tk.Label(bg=(result_colour), textvariable=pulsetype, fg='white', justify='center', font=('Calibri', 14, 'bold'))
PulseType_Result.place(relx=0.82, rely=0.53, relwidth=0.1, relheight=0.05)

PulseLength_Label = tk.Label(bg=(label_colour), text="Pulse Length (secs):", justify='left', borderwidth=2, relief="groove", font=('Calibri', 14, 'bold'))
PulseLength_Label.place(relx=0.67, rely=0.59, relwidth=0.15, relheight=0.05)

PulseLength_Result = tk.Label(bg=(result_colour), textvariable=pulselength, fg='white', justify='center', font=('Calibri', 14, 'bold'))
PulseLength_Result.place(relx=0.82, rely=0.59, relwidth=0.1, relheight=0.05)


#===========================================1.5 FUNCTIONS======================================================
    
def mbesresults():
    
    MBES = "KM EM2040"
    Freq = (Freq_Combobox.get())
    BeamSpacing = (BeamSpacing_combobox.get())
    MaxSwathAngle = (MaxSwathAngle_Entry.get())
    MaxSwathCoverage = (MaxSwathCoverage_Entry.get())
    LineSpacing = (LineSpacing_Entry.get())
    txmode = txmode_combobox.get()
    WaterDepth = (WaterDepth_Entry.get())
    SV = (SV_Entry.get())
    Speed = (Speed_Entry.get())
    #Temp = (Temp_Entry.get())
    #Salinity = (Salinity_Entry.get())
    #Acidity = (Acidity_Entry.get())
    Depthmode = DepthMode_combobox.get()

###########################################EM2040#####################################################################################
    if MBES == "KM EM2040":

        MaxSwathAngle = float(MaxSwathAngle)
        MaxSwathCoverage = float(MaxSwathCoverage)
        LineSpacing = float(LineSpacing)
        WaterDepth = float(WaterDepth)
        SV = float(SV)
        Speed = float(Speed)
        MaxSwathAngleRads = float(math.radians(MaxSwathAngle))
        
        

        SwathDist = (MaxSwathCoverage)
        VertexAngular = (MaxSwathAngleRads/2)
        tanf = math.tan(VertexAngular)
        BaseAngular = 2*WaterDepth*tanf
        SwathDistAngular=(round(BaseAngular, 2)) #Swath Coverage Calculated from Max Swath Angle setting and Water Depth
        AngleDist = (math.atan((2*WaterDepth)/(MaxSwathCoverage))) #Swath Angle Calculated from Max Swath Coverage Distance setting and Water Depth
        AngleDist = math.degrees(AngleDist)
        
##############################Swath Width, Overlap, Swath Angle######################################################################
        if AngleDist < MaxSwathAngle:
            swathwidth1 = SwathDist
            swathwidth.set(SwathDist)
            SwathCoverage1 = ((SwathDist/LineSpacing)*100)
            Overlap = (SwathCoverage1)-100
            SwathCoverage1 = (round(SwathCoverage1, 2))
            Overlap = (round(Overlap, 2))
            bathyoverlap.set(Overlap)
            bathycoverage.set(SwathCoverage1)
            effectiveangle1=(180-((math.degrees((math.atan((2*WaterDepth)/(SwathDist)))))*2))
            effectiveangle1 = round(effectiveangle1, 2)
            effectiveangle.set(effectiveangle1)
            
            
        if SwathDistAngular < SwathDist:
            swathwidth1 = SwathDistAngular
            swathwidth.set(SwathDistAngular)
            SwathCoverage1 = ((SwathDistAngular/LineSpacing)*100)
            Overlap = (SwathCoverage1)-100
            SwathCoverage1 = (round(SwathCoverage1, 2))
            Overlap = (round(Overlap, 2))
            bathyoverlap.set(Overlap)
            bathycoverage.set(SwathCoverage1)
            effectiveangle1=(MaxSwathAngle)
            effectiveangle1 = round(effectiveangle1, 2)
            effectiveangle.set(effectiveangle1)
            
            
##############################Slant Range, Get SV######################################################################
        
        WD2 = float((WaterDepth_Entry.get()))
        EA2 = float(radians(effectiveangle1))
        sr = ((WD2)/(cos((EA2/2))))*1.2 ##Calculates outer swath slant range from WD and Effective Swath Angle. 1.3x to compensate for variations in terrain
        sr = (round(sr, 2))
        slantrange.set(sr)

        swathtype = Swathtype_Combobox.get()
        SV = SV_Entry.get()
        SV = float(SV)
        SV = round(SV, 2)



##############################EM2040 Tx Pulse Lengths######################################################################
        #all times in secs, BW in kHz
        pulse_200k_FM_verydeep = 0.012 #auto selects between 3/12ms based on attenuation. Larger value used for calculation
        pulse_300k_FM_verydeep = 0.006 #auto selects between 2/6ms based on attenuation. Larger value used for calculation
        BW_FM = 1.7 #1.7kHz sweep for 200 and 300 kHz

        pulse_200k_CW_shallow = 0.000038
        pulse_200k_CW_medium = 0.000108
        pulse_200k_CW_deep = 0.000324
    

        pulse_300k_CW_shallow = 0.000038
        pulse_300k_CW_medium = 0.000108
        pulse_300k_CW_deep = 0.000324
    

        pulse_400k_CW_shallow = 0.000027
        pulse_400k_CW_medium = 0.000054
        pulse_400k_CW_deep = 0.000108
        
        processing_delay = 0.020 


        

##############################PULSE TYPE######################################################################
           
    if txmode == "FM Enabled":
        if Depthmode == "Shallow":
            if (Freq) == "200":
                pulse = pulse_200k_CW_shallow
                pulsetype.set("CW")
                pulselength.set(pulse)

            if (Freq) == "300":
                pulse = pulse_300k_CW_shallow
                pulsetype.set("CW")
                pulselength.set(pulse)

            if (Freq) == "400":
                pulse = pulse_400k_CW_shallow
                pulsetype.set("CW")
                pulselength.set(pulse)


        if Depthmode == "Medium":
            if (Freq) == "200":
                pulse = pulse_200k_CW_medium
                pulsetype.set("CW")
                pulselength.set(pulse)

            if (Freq) == "300":
                pulse = pulse_300k_CW_medium
                pulsetype.set("CW")
                pulselength.set(pulse)

            if (Freq) == "400":
                pulse = pulse_400k_CW_medium
                pulsetype.set("CW")
                pulselength.set(pulse)

        if Depthmode == "Deep":
            if (Freq) == "200":
                pulse = pulse_200k_CW_deep
                pulsetype.set("CW")
                pulselength.set(pulse)

            if (Freq) == "300":
                pulse = pulse_300k_CW_deep
                pulsetype.set("CW")
                pulselength.set(pulse)

            if (Freq) == "400":
                pulse = pulse_400k_CW_deep
                pulsetype.set("CW")
                pulselength.set(pulse)


        if Depthmode == "Very Deep":
            if (Freq) == "200":
                pulse = pulse_200k_FM_verydeep
                pulsetype.set("FM")
                pulselength.set(pulse)

            if (Freq) == "300":
                pulse = pulse_300k_FM_verydeep
                pulsetype.set("FM")
                pulselength.set(pulse)

            if (Freq) == "400":
                pulse = pulse_400k_CW_deep
                pulsetype.set("CW - FM N/A")
                pulselength.set(pulse)


    


    if txmode == "FM Disabled":
        if Depthmode == "Shallow":
            if (Freq) == "200":
                pulse = pulse_200k_CW_shallow
                pulsetype.set("CW")
                pulselength.set(pulse)

            if (Freq) == "300":
                pulse = pulse_300k_CW_shallow
                pulsetype.set("CW")
                pulselength.set(pulse)

            if (Freq) == "400":
                pulse = pulse_400k_CW_shallow
                pulsetype.set("CW")
                pulselength.set(pulse)


        if Depthmode == "Medium":
            if (Freq) == "200":
                pulse = pulse_200k_CW_medium
                pulsetype.set("CW")
                pulselength.set(pulse)

            if (Freq) == "300":
                pulse = pulse_300k_CW_medium
                pulsetype.set("CW")
                pulselength.set(pulse)

            if (Freq) == "400":
                pulse = pulse_400k_CW_medium
                pulsetype.set("CW")
                pulselength.set(pulse)

        if Depthmode == "Deep":
            if (Freq) == "200":
                pulse = pulse_200k_CW_deep
                pulsetype.set("CW")
                pulselength.set(pulse)

            if (Freq) == "300":
                pulse = pulse_300k_CW_deep
                pulsetype.set("CW")
                pulselength.set(pulse)

            if (Freq) == "400":
                pulse = pulse_400k_CW_deep
                pulsetype.set("CW")
                pulselength.set(pulse)


        if Depthmode == "Very Deep":
            if (Freq) == "200":
                pulse = pulse_200k_CW_deep
                pulsetype.set("CW - FM Disabled")
                pulselength.set(pulse)

            if (Freq) == "300":
                pulse = pulse_300k_CW_deep
                pulsetype.set("CW - FM Disabled")
                pulselength.set(pulse)

            if (Freq) == "400":
                pulse = pulse_400k_CW_deep
                pulsetype.set("CW - FM N/A")
                pulselength.set(pulse)


###################################PING RATE/SWATH RATE#############################################################################
        #Max 50Hz. 
        #Tx limited to transmit <=6% of the time (1 sec: tx max = 60ms)
        #Outer Slant Range = x1.3 for terrain variation - controlled by range gate (not used in this program)
        #20ms processing delay per ping

    if swathtype == "Single":
        twowaytraveltime = (((sr/SV)*2)+(pulse))
        pr = (1/twowaytraveltime) 
        pr = round(pr, 2)
        srate = pr
        if pr < 50:
            pingrate.set(pr)
            swathrate.set(srate)

        if pr >= 50:
            pingrate.set("Max - 50")
            swathrate.set("Max - 50")



    if swathtype == "Dual":
        twowaytraveltime = ((sr/SV)*2)+(pulse*2)+(processing_delay)
        pr = 1/twowaytraveltime
        pr = round(pr, 2)
        srate = 2*pr
        if pr < 50:
            pingrate.set(pr)
            swathrate.set(srate)

        if pr >= 50:
            pingrate.set("Max - 50")
            swathrate.set("Max - 50")




##############################PINGS PER GRID######################################################################

    gridsize = float((Grid_Entry.get()))
    kts = Speed
    ms = Speed/1.9438444924406
    spacing = BeamSpacing_combobox.get()
    swathtype = Swathtype_Combobox.get()


    if spacing == "Equidistance":
        beams = 256
        width = float(swathwidth1)
        beamsperping.set(beams)
        across_beams_per_meter = beams/width
        along_beams_per_meter = srate/ms
        grids = ((across_beams_per_meter) + (along_beams_per_meter))*(gridsize)
        grids = round(grids, 2)
        gridping.set(grids)






    if spacing == "Equiangle":
        if swathtype == "Dual":
            beams = 500
        if swathtype == "Single":
            beams = 256
        width = float(swathwidth1)
        beamsperping.set(beams)
        across_beams_per_meter = beams/width
        along_beams_per_meter = srate/ms
        grids = (across_beams_per_meter + along_beams_per_meter)*gridsize
        grids = round(grids, 2)
        gridping.set(grids)

    
    if spacing == "High Density":
        if swathtype == "Dual":
            beams =800
        if swathtype == "Single":
            beams = 400
        width = float(swathwidth1)
        beamsperping.set(beams)
        across_beams_per_meter = beams/width
        along_beams_per_meter = srate/ms
        grids = (across_beams_per_meter + along_beams_per_meter)*gridsize
        grids = round(grids, 2)
        gridping.set(grids)



    if spacing == "Ultra High Density":
        if swathtype == "Dual":
            beams =1024
        if swathtype == "Single":
            beams = 512
        width = float(swathwidth1)
        beamsperping.set(beams)
        across_beams_per_meter = beams/width
        along_beams_per_meter = srate/ms
        grids = (across_beams_per_meter + along_beams_per_meter)*gridsize
        grids = round(grids, 2)
        gridping.set(grids)


#===================================================================================================================================
mainloop()