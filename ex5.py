# -*- coding:utf-8 -*-
name = 'Phong'
age = 23
height = 170 #centemeter
weight = 57 #kilo
eyes = 'Black'
teeth = 'White'
hair = 'Black'
height_inch = height * 0.393700787
weight_pount = weight * 2.20462262
result = height < weight

print str(age)
print repr(age)

print str(result)
print repr(result)

print "Let's talk about %s." % name
print "He's %d inchs tall" %height_inch
print "He's %d pound heavy." %weight_pount
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" %(eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

#this line is tricky, try to get it exactly right.
print "If I add %d, %d and %d I get %d" %(age, height_inch, weight_pount,
        age + weight_pount)

print round(1.4345123)
print round(1.5653)
