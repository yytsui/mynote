Stereo Delay Effects VST Plugin
###############################
:date: 2004-04-01 17:24
:author: yiyang
:category: Audio, DSP
:slug: stereo-delay-effects-vst-plugin

The stereo delay effects can be accomplished by the block diagram
Fig2-1. Two basic circular delay line are used in the left and right
channels and are coupled by introducing cross-feedback coefficients dL
and dR[1].

| |Stereo Delay Effects Filter Diagram|
|  Fig 2-1: Stereo Delay Effects Filter Diagram

List below is the digital signal processing code excerpt.

::

     1  //...Initializtions  have be done in Constructor 
     2  void  Cstereo_delay_effects::processReplacing(float  **inputs, float **outputs,
     3                                                long sampleFrames)
     4  {
     5    float *xL = inputs[0];
     6    float *xR = inputs[1];
     7    float *yL = outputs[0];
     8    float *yR = outputs[1];
     9
    10    while(--sampleFrames >= 0)
    11    {
    12      sLL = wL[(pL+DL-wL)%(DL+1)];//DL-th tap in circular delay line buffer.
    13      sRR = wR[(pR+DR-wR)%(DR+1)];
    14      sL0 = bL * (*xL) + aL * sLL + dR * sRR;
    15      sR0 = bR * (*xR) + aR * sRR + dL * sLL;
    16      (*yL++) = cL * (*xL++) + sLL;
    17      (*yR++) = cR * (*xR++) + sRR;
    18
    19      *pL-- = sL0; //wrap around circular buffer
    20      wrap(DL,wL,&pL);
    21      *pR--= sR0;
    22      wrap(DR,wR,&pR);
    23    }
    24  }
    25

| Requirements:
|  The `VST Plugin`_ is a .dll (dynamic link library) file and must be
load into a VST Host program such as `FruityLoops Studio.`_\ Microsoft
Visual C++ 6.0 was used to compile this project.
|  References:
|  [1]S.J. Orfanidis, Introduction to Signal Processing, Prentice-Hall
1996, p.467.
|  Download:
|  `stereo\_delay\_effects.zip(58KB)`_

.. _VST Plugin: http://en.wikipedia.org/wiki/Virtual_Studio_Technology
.. _FruityLoops Studio.: http://www.fruityloops.com/
.. _stereo\_delay\_effects.zip(58KB): /files/download/stereo_delay_effects.zip

.. |Stereo Delay Effects Filter Diagram| image:: /files/pictures/stereodelayeffect.gif
