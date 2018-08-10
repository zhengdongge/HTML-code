#!/usr/bin/python2.7
#chmod a+x basic-form.py
import cgitb
import cgi
cgitb.enable()
print "Content-type:text/html"
print ""
the_form=cgi.FieldStorage()
#print "your name is :" + the_form["name"]
print "<!--"
for key in the the_form.keys():
	value= the_form[key]
	print key + " " + the_form[key].value

print "-->"

print '''<html><body>name='''
print the_form["name"].value
print '''</body></html>'''   