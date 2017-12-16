#!/usr/bin/python


#printing a string 
print "printing hello: hello"

#assinging a string variable 
a = "i am a string"
print a

#string functionalities 

	#getting the length of the string 
print len(a)

	#getting indexs of a sting 
print "string index of 5 usint a[5]: ",  a[5] 

	#slicing is the same as a substring 
print "grab everything from 3 up to 6", a[3:6]

	#using slicing to reverse a string
h = "hello" 
f = h[::-1]
print "reverse the word hello:", f

	#using string concatination to add to a current string variable
h += " world"
print h