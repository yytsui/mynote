Another usage of web testing tool: Auto browsing for checking your library account status
#########################################################################################
:date: 2005-10-11 19:46
:author: yiyang
:category: Web
:slug: another-usage-of-web-testing-tool-auto-browsing-for-checking-your-library-account-status

| For those in favor of reading, listening to music, or even watching
DVD, `Calgary Public Library`_ is definitely a great resource center.
One thing I can not figure out is that the library web system will not
notify you the expire of books loan by email, it's not diffcult to
forget to update and have to pay the fine then.
|  To check your card status, you have to go through these steps:
|  1. open the browser,
|  2. go to `Calgary Public Library Sign In page`_,
|  3.login by puntching your 14 digit card number and 4 digit pin
number,
|  4. click Sign In,
|  5. click Items Out,
|  6. click "Return by"

Do we have to repeat all these step every time? Maybe not, at least for
a lazy person like me :). With `Watir`_, "a free, open-source functional
testing tool for automating browser-based tests of web applications",
writing a Ruby script could save us from repeating these steps. The
script is list below

::

    require 'watir'

    #open the browser
    ie = Watir::IE.new
    #go to the libary Sign In Page
    ie.goto("https://catalogue.calgarypubliclibrary.com/ipac20/ipac.jsp?menu=account")
    #Keyin 14 digit Library Card number
    ie.textField(:name, "sec1").set("12345678901234")
    #Keyin 4 digit PIN number
    ie.textField(:name, "sec2").set("1234")
    #Click "Sign In"
    ie.button(:value, "Sign In").click
    #Click "Items Out"
    ie.link(:text, "Items Out").click
    #Click "Return by"
    ie.link(:text, "Return by").click

Then save these codes as .rb file in windows desktop, just double click
it every time you want to check your book loan statu, IE will be open
and then login to the Items Out page with sorting expired date
automatically.

.. _Calgary Public Library: http://calgarypubliclibrary.com/
.. _Calgary Public Library Sign In page: https://catalogue.calgarypubliclibrary.com/ipac20/ipac.jsp?menu=account
.. _Watir: http://wtr.rubyforge.org/
