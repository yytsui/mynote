author: yiyang
comments: true
date: 2004-04-01 17:24:58
layout: post
slug: stereo-delay-effects-vst-plugin
title: Stereo Delay Effects VST Plugin
wordpress_id: 4
tags: Audio,DSP

The stereo delay effects can be accomplished by the block diagram Fig2-1. Two basic circular delay line are used in the left and right channels and are coupled by introducing cross-feedback coefficients dL and dR[1]. <!-- more -->

![Stereo Delay Effects Filter Diagram](/files/pictures/stereodelayeffect.gif)
 Fig 2-1: Stereo Delay Effects Filter Diagram

List below is the digital signal processing code excerpt.

    
    
    <font color="#804040"> 1</font>  <font color="#0000ff">//...Initializtions  have be done in Constructor </font>
    <font color="#804040"> 2</font>  <font color="#2e8b57"><b>void</b></font>  Cstereo_delay_effects::processReplacing(<font color="#2e8b57"><b>float</b></font>  **inputs, <font color="#2e8b57"><b>float</b></font> **outputs,
    <font color="#804040"> 3</font>                                                <font color="#2e8b57"><b>long</b></font> sampleFrames)
    <font color="#804040"> 4</font>  {
    <font color="#804040"> 5</font>    <font color="#2e8b57"><b>float</b></font> *xL = inputs[<font color="#ff00ff">0</font>];
    <font color="#804040"> 6</font>    <font color="#2e8b57"><b>float</b></font> *xR = inputs[<font color="#ff00ff">1</font>];
    <font color="#804040"> 7</font>    <font color="#2e8b57"><b>float</b></font> *yL = outputs[<font color="#ff00ff">0</font>];
    <font color="#804040"> 8</font>    <font color="#2e8b57"><b>float</b></font> *yR = outputs[<font color="#ff00ff">1</font>];
    <font color="#804040"> 9</font>
    <font color="#804040">10</font>    <font color="#804040"><b>while</b></font>(--sampleFrames >= <font color="#ff00ff">0</font>)
    <font color="#804040">11</font>    {
    <font color="#804040">12</font>      sLL = wL[(pL+DL-wL)%(DL+<font color="#ff00ff">1</font>)];<font color="#0000ff">//DL-th tap in circular delay line buffer.</font>
    <font color="#804040">13</font>      sRR = wR[(pR+DR-wR)%(DR+<font color="#ff00ff">1</font>)];
    <font color="#804040">14</font>      sL0 = bL * (*xL) + aL * sLL + dR * sRR;
    <font color="#804040">15</font>      sR0 = bR * (*xR) + aR * sRR + dL * sLL;
    <font color="#804040">16</font>      (*yL++) = cL * (*xL++) + sLL;
    <font color="#804040">17</font>      (*yR++) = cR * (*xR++) + sRR;
    <font color="#804040">18</font>
    <font color="#804040">19</font>      *pL-- = sL0; <font color="#0000ff">//wrap around circular buffer</font>
    <font color="#804040">20</font>      wrap(DL,wL,&pL);
    <font color="#804040">21</font>      *pR--= sR0;
    <font color="#804040">22</font>      wrap(DR,wR,&pR);
    <font color="#804040">23</font>    }
    <font color="#804040">24</font>  }
    <font color="#804040">25</font>
    



Requirements:
The [VST Plugin](http://en.wikipedia.org/wiki/Virtual_Studio_Technology) is a .dll (dynamic link library) file and must be load into a VST Host program such as [FruityLoops Studio. ](http://www.fruityloops.com/)Microsoft Visual C++ 6.0 was used to compile this project.
References:
[1]S.J. Orfanidis, Introduction to Signal Processing, Prentice-Hall 1996, p.467.
Download:
[stereo_delay_effects.zip(58KB)](/files/download/stereo_delay_effects.zip)

