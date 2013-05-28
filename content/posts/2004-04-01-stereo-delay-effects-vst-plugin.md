author: yiyang
comments: true
date: 2004-04-01 17:24:58
layout: post
slug: stereo-delay-effects-vst-plugin
title: Stereo Delay Effects VST Plugin
wordpress_id: 4
tags: Audio,DSP

The stereo delay effects can be accomplished by the block diagram Fig2-1. Two basic circular delay line are used in the left and right channels and are coupled by introducing cross-feedback coefficients dL and dR[1]. 

![Stereo Delay Effects Filter Diagram](|filename|/images/stereodelayeffect.gif)
 Fig 2-1: Stereo Delay Effects Filter Diagram

List below is the digital signal processing code excerpt.

    
      :::cpp
       //...Initializtions  have be done in Constructor 
       void  Cstereo_delay_effects::processReplacing(float  **inputs, float **outputs,
                                                     long sampleFrames)
       {
         float *xL = inputs[0];
         float *xR = inputs[1];
         float *yL = outputs[0];
         float *yR = outputs[1];
     
        while(--sampleFrames >= 0)
        {
          sLL = wL[(pL+DL-wL)%(DL+1)];//DL-th tap in circular delay line buffer.
          sRR = wR[(pR+DR-wR)%(DR+1)];
          sL0 = bL * (*xL) + aL * sLL + dR * sRR;
          sR0 = bR * (*xR) + aR * sRR + dL * sLL;
          (*yL++) = cL * (*xL++) + sLL;
          (*yR++) = cR * (*xR++) + sRR;
    
          *pL-- = sL0; //wrap around circular buffer
          wrap(DL,wL,&pL);
          *pR--= sR0;
          wrap(DR,wR,&pR);
        }
      }
    
    



** Requirements: **
The [VST Plugin](http://en.wikipedia.org/wiki/Virtual_Studio_Technology) is a .dll (dynamic link library) file and must be load into a VST Host program such as [FruityLoops Studio. ](http://www.fruityloops.com/)Microsoft Visual C++ 6.0 was used to compile this project.

** References: **
[1]S.J. Orfanidis, Introduction to Signal Processing, Prentice-Hall 1996, p.467.

** Download: **
[stereo_delay_effects.zip(58KB)](/files/download/stereo_delay_effects.zip)

