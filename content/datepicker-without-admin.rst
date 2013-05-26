datepicker without admin
########################
:date: 2008-10-30 17:06
:author: yiyang
:category: Django, Elsewhere
:slug: datepicker-without-admin

`#`_

"""I use something like this (after adding in the JS) to create a form
with a date field that works like the admin:

| from django import forms
|  from django.contrib.admin import widgets
|  class FooForm(forms.Form):
|  bar = forms.DateField(widget=widgets.AdminDateWidget)

"""

.. _#: http://lowkster.blogspot.com/2008/10/datepicker-without-admin.html
