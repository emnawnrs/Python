#!/usr/bin/env python
# Filename:objvar.py

class Person:
    '''Represents a person'''
    population=0

    def __init__(self, name):
        '''Initializes the person's data.'''
        self.na=name
        print '(Initializing %s)' % self.na
        Person.population += 1

    def __del__(self):
        '''i am dying'''
        print '%s says bye.' % self.na
        Person.population -= 1
        
        if Person.population == 0:
            print 'i am the last one.'
        else:
            print 'there are still %d people left.' % Person.population

    def sayHi(self):
        print 'hi, my name is %s.' % self.na

    def howMany(self):
        if Person.population == 1:
            print 'i am the only person here.'
        else:
            print 'we have %d persons here.' % Person.population


swaroop = Person('sw')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('ka')
kalam.sayHi()
kalam.howMany()
