author: yiyang
comments: true
date: 2004-04-15 23:00:16
layout: post
slug: rotary-speaker-simulation-in-sb-live-51-emu10k1
title: Rotary Speaker Simulation in SB live 5.1 (EMU10k1)
wordpress_id: 5
tags: Audio,DSP

The loudspeaker rotary effect can be simulated by using a combination of modulation and delay line modulation, as shown in Fig3-1[1]. The modulated delay line and amplitude modulation simulates the pitch modifications effects and intensity modifications effect respectively. <!-- more -->

![RotarySpeaker](/files/pictures/RotarySpeaker_scale.jpg)
Fig 3-1 Rotary Speaker Effects Diagram

List below is the EMU10K1 Assembly code:

    
    
            <font size="-1">input in;</font><font color="#009900">x</font><br></br>
            <font face="Arial, Helvetica, sans-serif" size="-1">output outL,outR;</font><font color="#009900">yL,yR</font><br></br>
            control frequency = 0.5; <font color="#009900">//frequency = wd</font><br></br>
            control delay = 0.5;<br></br>
    
            const MaxDelaySample = 0x1f4000 ; <font color="#009900">dec2hex((1000) *2^11) </font>
            <br></br>static zcos,zsin = 0.5;<br></br>
            static wd,dd1,dd2,osc1,osc2; <font color="#009900">wd = angular frequency,</font><br></br>
            <font color="#009900">; dd1 = Left delay sample address; <br></br>
            ; dd2 = Right delay sample address; <br></br>
            ; osc1 = oscllation amplitude = sin; <br></br>
            ; osc2 = -sin;</font><br></br>
            static sm1,sm2; <font color="#009900">internal state</font><br></br>
            static q1,q2; <font color="#009900">internal state </font>
           <font size="-1"> itramsize 2006; </font><font color="#009900">Circular Delay Line Size (1000+1+2)*2</font><br></br>
            idelay write dwL at 0;<font color="#009900">Left Channel Circulat Buffer 
            </font><br></br>
            idelay read drL1 at 1002;<br></br>
            idelay read drL2 at 1002; <br></br>
    
            idelay write dwR at 1003;<font color="#009900">Right Channel Circular Buffer
            </font><br></br>
            idelay read drR1 at 2005;<br></br>
            idelay read drR2 at 2005;<br></br>
            <br></br>
            macs wd,0,frequency, 0.001;<font color="#009900">//frequency scaling work around
            </font><br></br>
       
            <font color="#009900">;--------sine wave generation---------------- </font><br></br>
            macsn zcos,zcos,wd,zsin;<br></br>
            macs zsin,zsin,wd,zcos;<br></br>
            macs osc1,0.5,zsin,1; <br></br>
            macsn osc2,0,osc1,1;<br></br>
            <font color="#009900">;--------------------------------------------<br></br>
            </font>
             macintw dd1,0,dd1,0x100000;
            <font color="#009900">Left channel:Left shift  11 bit  fractional address
            </font>
            interp sm1,drL1,dd1,drL2;<font color="#009900">Left Channel:Linear Interpolation</font><br></br>
            <br></br>
            macintw dd2,0,dd2,0x100000;<font color="#009900">Right channel</font><br></br>
            interp sm2,drR1,dd1,drR2;<font color="#009900">Right Channel </font><br></br>
            <br></br>
            macs q1,sm1,sm1,osc1; <font color="#009900">q1 = sm1(1+sin(wd*n))</font><br></br>
            macs q2,sm2,sm2,osc2; <br></br>
            <br></br>
            macs outL,q1,0.7,q2;<br></br>
            macs outR,q2,0.7,q1;<br></br>
            <br></br>
            <font color="#009900">;---------delay corresponding address calculation--------- </font>
    
             macs dd1,0,delay,MaxDelaySample;<br></br>
            macs dd1,&dwL,dd1,osc1;<br></br>
            macints &drL1,dd1,0x800,0x1;<br></br>
            macints &drL2,dd1,0x800,0x2;<br></br>
    
          
            macs dd2,0,delay,MaxDelaySample;<br></br>
            macs dd2,&dwR,dd2,osc2;<br></br>
            macints &drR1,dd2,0x800,0x1;<br></br>
            macints &drR2,dd2,0x800,0x2;<br></br>
           
            macs dwL,in,0,0;<font color="#009900"> feed left channel input </font><br></br>
            macs dwR,in,0,0; <font color="#009900">feed right channel input</font>
         
            end
          
    


In addition, a simple low frequency sine wave generator sinegen.da is also implemented as audio test source. Fig3-2 is the audio unit connection diagram and user control interface. 
![](/files/pictures/RS4xDSPschematic.gif)
Fig 3-2 Rotary oudspeaker simulation configuration diagram.

**Requirements:**
Hardware:[ EMU10K1](http://emu10k1.sourceforge.net/as10k1-manual/) based audio card ([Sound Blaster Live 5.1, Audigy](http://www.soundblaster.com/)) installed in PC.
Driver:[ KX Audio Driver](http://kxproject.lugosoft.com/)
For more detail information, please refer to [KX project.](http://kxproject.lugosoft.com/) 
**References:**
[1] S. Disch and U. Zolzer, Modulation and delay line based digital audio effect, Proc. DAFX-99 _Digital Audio Effects Workshop_, Trodheim, December 1999.  
**Download:**
[RotarySpeaker.da(3KB)](/files/download/RotarySpeaker.da)
[sinegen.da(1KB)](/files/download/sinegen.da)


