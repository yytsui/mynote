author: yiyang
comments: true
date: 2004-03-06 10:49:35
layout: post
slug: allpass-lowpass-reverberator-in-adsp-2181-ez-kit-lite
title: 'Allpass-Lowpass Reverberator in ADSP-2181 EZ-KIT Lite '
wordpress_id: 3
tags: Audio,DSP

The reverberator shown in Fig 1-1 is built by cascading allpass filters(AP1-AP4) and lowpass filters(LP1-LP4). The strategy is shorter reverberation times in early allpass loops and longer reverberation times in later ones. Also, the cutoff frequency for each successive lowpass filter is gradually lower, simulating the increasing loss of high frequency energy[1].<!-- more -->

![](/files/pictures/alpreverbrator_scale.jpg)
Fig1-1. Allpass-Lowpass Reverbrator

The transfer function of all pass filter is H(z) = (-a + z^(-D))/(1-a*z^(-D)) [2]. The values "a" increases from AP1 to AP4 ,since the reverberation times value increases. For lowpass filter(LP1-LP4), 1st order lowpass filter is used to simulate the gradual decreasing of high frequency signal. Given 3db frequency f3db, one can easily design a 1st order low pass filter H(z) = b0*(1+z^(-1))/(1-a1*z^(-1)) by bilinear transformation. In fact, the [MATLAB filter design toolbox](http://www.mathworks.com/access/helpdesk/help/toolbox/filterdesign/filterdesign.shtml) can be used to decide the coefficients b0 and a1.

Requirements:
To compile this project, you will need Analog Device [VisualDSP++.](http://www.analog.com/processors/resources/crosscore/visualDspDevSoftware.html) After building executable binary, you can use VisualDSP++ to load the program into [ADSP-2181](http://www.analog.com/processors/epProductPage/0,2461,21xx-EZLITE,00.html)for execution.

[![](/files/pictures/EzKitLite.jpg)](http://www.analog.com/processors/epProductPage/0,2461,21xx-EZLITE,00.html)

References:
[1]R, Boulanger ed.,The CSOUND book, MIT Press 2000, p475.
[2]S.J. Orfanidis, Introduction to Signal Processing, Prentice-Hall 1996, p.369.
Download:
[allpass_lowpass_reverbrator.zip(17KB)](/files/download/allpass_lowpass_reverbrator.zip)
