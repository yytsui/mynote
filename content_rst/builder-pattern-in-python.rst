A great book: Design Patterns in Ruby
#####################################
:date: 2008-08-05 17:52
:author: yiyang
:category: Ruby
:slug: builder-pattern-in-python

I have been reading  `Design Patterns in Ruby`_. It's a quite
intrestring read, the author explain the `GOF`_ patterns in a very clear
and readable way. For example,  in chapter 3 "Varying the Algorithm with
the Template Mothod", the author explaing the 'Template Method' pattern 
quite clearly by employing  a example project which I did have to do
something similiar many years ago-- spewing out reports with some
contents but in many different formats such as HTML, PDF, plain text
...etc.  In chapter 14 'Easier Object Construction with the Builder',
the author simulates the computer building process  by using  'Builder'
Pattern. The "Builders in the Wild" section in this chapter mentioned
that MailFacotory in Ruby is a builder pattern example which remind me
that `email.mimi.text.MIMEText`_ in Python is also a builder pattern
example. Anyway, it's good to see finally there is a design patterns
book from the perspective of dynamic language.

.. _Design Patterns in Ruby: http://www.tekverse.com
.. _GOF: http://www.amazon.com/Design-Patterns-Object-Oriented-Addison-Wesley-Professional/dp/0201633612/ref=pd_bbs_sr_1?ie=UTF8&s=books&qid=1218062695&sr=1-1
.. _email.mimi.text.MIMEText: http://docs.python.org/lib/node161.html
