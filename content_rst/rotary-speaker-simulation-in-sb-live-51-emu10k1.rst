Rotary Speaker Simulation in SB live 5.1 (EMU10k1)
##################################################
:date: 2004-04-15 23:00
:author: yiyang
:category: Audio, DSP
:slug: rotary-speaker-simulation-in-sb-live-51-emu10k1

The loudspeaker rotary effect can be simulated by using a combination of
modulation and delay line modulation, as shown in Fig3-1[1]. The
modulated delay line and amplitude modulation simulates the pitch
modifications effects and intensity modifications effect respectively.

| |RotarySpeaker|
|  Fig 3-1 Rotary Speaker Effects Diagram

List below is the EMU10K1 Assembly code:

::

            input in;x
            output outL,outR;yL,yR
            control frequency = 0.5; //frequency = wd
            control delay = 0.5;

            const MaxDelaySample = 0x1f4000 ; dec2hex((1000) *2^11) 
            static zcos,zsin = 0.5;
            static wd,dd1,dd2,osc1,osc2; wd = angular frequency,
            ; dd1 = Left delay sample address; 
            ; dd2 = Right delay sample address; 
            ; osc1 = oscllation amplitude = sin; 
            ; osc2 = -sin;
            static sm1,sm2; internal state
            static q1,q2; internal state 
            itramsize 2006; Circular Delay Line Size (1000+1+2)*2
            idelay write dwL at 0;Left Channel Circulat Buffer 
            
            idelay read drL1 at 1002;
            idelay read drL2 at 1002; 

            idelay write dwR at 1003;Right Channel Circular Buffer
            
            idelay read drR1 at 2005;
            idelay read drR2 at 2005;
            
            macs wd,0,frequency, 0.001;//frequency scaling work around
            
       
            ;--------sine wave generation---------------- 
            macsn zcos,zcos,wd,zsin;
            macs zsin,zsin,wd,zcos;
            macs osc1,0.5,zsin,1; 
            macsn osc2,0,osc1,1;
            ;--------------------------------------------
            
             macintw dd1,0,dd1,0x100000;
            Left channel:Left shift  11 bit  fractional address
            
            interp sm1,drL1,dd1,drL2;Left Channel:Linear Interpolation
            
            macintw dd2,0,dd2,0x100000;Right channel
            interp sm2,drR1,dd1,drR2;Right Channel 
            
            macs q1,sm1,sm1,osc1; q1 = sm1(1+sin(wd*n))
            macs q2,sm2,sm2,osc2; 
            
            macs outL,q1,0.7,q2;
            macs outR,q2,0.7,q1;
            
            ;---------delay corresponding address calculation--------- 

             macs dd1,0,delay,MaxDelaySample;
            macs dd1,&dwL,dd1,osc1;
            macints &drL1,dd1,0x800,0x1;
            macints &drL2,dd1,0x800,0x2;

          
            macs dd2,0,delay,MaxDelaySample;
            macs dd2,&dwR,dd2,osc2;
            macints &drR1,dd2,0x800,0x1;
            macints &drR2,dd2,0x800,0x2;
           
            macs dwL,in,0,0; feed left channel input 
            macs dwR,in,0,0; feed right channel input
         
            end
          

| In addition, a simple low frequency sine wave generator sinegen.da is
also implemented as audio test source. Fig3-2 is the audio unit
connection diagram and user control interface.
|  |image1|
|  Fig 3-2 Rotary oudspeaker simulation configuration diagram.

| \ **Requirements:**\ 
|  Hardware:\ `EMU10K1`_ based audio card (`Sound Blaster Live 5.1,
Audigy`_) installed in PC.
|  Driver:\ `KX Audio Driver`_
|  For more detail information, please refer to `KX project.`_\ 
|  \ **References:**\ 
|  [1] S. Disch and U. Zölzer, Modulation and delay line based digital
audio effect, Proc. DAFX-99 *Digital Audio Effects Workshop*, Trodheim,
December 1999.
|  \ **Download:**\ 
|  \ `RotarySpeaker.da(3KB)`_\ 
|  \ `sinegen.da(1KB)`_\ 

.. _EMU10K1: http://emu10k1.sourceforge.net/as10k1-manual/
.. _Sound Blaster Live 5.1, Audigy: http://www.soundblaster.com/
.. _KX Audio Driver: http://kxproject.lugosoft.com/
.. _KX project.: http://kxproject.lugosoft.com/
.. _RotarySpeaker.da(3KB): /files/download/RotarySpeaker.da
.. _sinegen.da(1KB): /files/download/sinegen.da

.. |RotarySpeaker| image:: /files/pictures/RotarySpeaker_scale.jpg
.. |image1| image:: /files/pictures/RS4xDSPschematic.gif
