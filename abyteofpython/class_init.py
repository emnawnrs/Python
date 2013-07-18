#!/usr/bin/env python
# Filename:class_init.py

class Person:
    def __init__(self, name):
        self.na=name
        self.foo='bar'
    def sayHi(self):
        print 'Hello, my name is', self.na
        print 'Hello, my name not is', self.foo

p=Person('xiaox')
p.sayHi()
