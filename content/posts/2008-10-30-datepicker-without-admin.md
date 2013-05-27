author: yiyang
comments: true
date: 2008-10-30 17:06:20
layout: post
slug: datepicker-without-admin
title: datepicker without admin
wordpress_id: 78
tags: Django,Elsewhere

[#](http://lowkster.blogspot.com/2008/10/datepicker-without-admin.html)

"""I use something like this (after adding in the JS) to create a form with a date field that works like the admin:

from django import forms
from django.contrib.admin import widgets
class FooForm(forms.Form):
bar = forms.DateField(widget=widgets.AdminDateWidget)

"""
