author: yiyang
comments: true
date: 2005-10-11 19:46:25
layout: post
slug: another-usage-of-web-testing-tool-auto-browsing-for-checking-your-library-account-status
title: 'Another usage of web testing tool: Auto browsing for checking your library
  account status'
wordpress_id: 6
tags: Web

For those in favor of  reading, listening to music, or even watching DVD, [Calgary Public Library ](http://calgarypubliclibrary.com/) is definitely a great resource center. One thing I can not figure out is that the library web system will not notify you the expire of books loan by email,  it's not diffcult to forget to update and have to pay the fine  then.
To check your card status, you have to go through these steps:
1. open the browser,
2. go to  [Calgary Public Library Sign In page](https://catalogue.calgarypubliclibrary.com/ipac20/ipac.jsp?menu=account),
3.login by puntching your 14 digit card number and 4 digit pin number,
4. click Sign In,
5. click Items Out,
6. click "Return by"

Do we have to repeat all these step every time? Maybe not, at least for a lazy person like me :). With [Watir](http://wtr.rubyforge.org/), "a free, open-source functional testing tool for automating browser-based tests of web applications", writing a Ruby script could save us  from repeating these steps. <!-- more --> The script is list below

    
    <span style="color: #ff80ff;">require</span> <span style="color: #ffa500;">'</span><span style="color: #ffa0a0;">watir</span><span style="color: #ffa500;">'</span>
    
    <span style="color: #80a0ff;">#open the browser</span>
    ie = <span style="color: #40ffff;">Watir</span>::<span style="color: #40ffff;">IE</span>.new
    <span style="color: #80a0ff;">#go to the libary Sign In Page</span>
    ie.goto(<span style="color: #ffa500;">"</span><span style="color: #ffa0a0;"><a href="https://catalogue.calgarypubliclibrary.com/ipac20/ipac.jsp?menu=account">https://catalogue.calgarypubliclibrary.com/ipac20/ipac.jsp?menu=account</a></span><span style="color: #ffa500;">"</span>)
    <span style="color: #80a0ff;">#Keyin 14 digit Library Card number</span>
    ie.textField(<span style="color: #40ffff;">:name</span>, <span style="color: #ffa500;">"</span><span style="color: #ffa0a0;">sec1</span><span style="color: #ffa500;">"</span>).set(<span style="color: #ffa500;">"</span><span style="color: #ffa0a0;">12345678901234</span><span style="color: #ffa500;">"</span>)
    <span style="color: #80a0ff;">#Keyin 4 digit PIN number</span>
    ie.textField(<span style="color: #40ffff;">:name</span>, <span style="color: #ffa500;">"</span><span style="color: #ffa0a0;">sec2</span><span style="color: #ffa500;">"</span>).set(<span style="color: #ffa500;">"</span><span style="color: #ffa0a0;">1234</span><span style="color: #ffa500;">"</span>)
    <span style="color: #80a0ff;">#Click "Sign In"</span>
    ie.button(<span style="color: #40ffff;">:value</span>, <span style="color: #ffa500;">"</span><span style="color: #ffa0a0;">Sign In</span><span style="color: #ffa500;">"</span>).click
    <span style="color: #80a0ff;">#Click "Items Out"</span>
    ie.link(<span style="color: #40ffff;">:text</span>, <span style="color: #ffa500;">"</span><span style="color: #ffa0a0;">Items Out</span><span style="color: #ffa500;">"</span>).click
    <span style="color: #80a0ff;">#Click "Return by"</span>
    ie.link(<span style="color: #40ffff;">:text</span>, <span style="color: #ffa500;">"</span><span style="color: #ffa0a0;">Return by</span><span style="color: #ffa500;">"</span>).click


Then  save  these codes as  .rb file in windows desktop, just double click it every time you want to check your book loan statu, IE will be open and then login to the Items Out page with sorting expired date automatically.
