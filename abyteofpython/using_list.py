#!/usr/bin/python
# Filename:using_list.py

shoplist = ['apple', 'mango', 'carrot', 'banana']
if __name__ == '__main__':
    print 'i have', len(shoplist), 'items to purchase.'
    
    print 'These item are:',
    for item in shoplist:
        print item,
    print '\nI also have to buy rice.'
    shoplist.append('rice')
    print 'my shopping list is now', shoplist
    
    print 'i will sort my list now'
    shoplist.sort()
    print 'sorted shopping list is', shoplist
    
    print 'the first item i will buy is', shoplist[0]
    olditem =shoplist[0]
    del shoplist[0]
    print 'i bought the', olditem
    print 'my shopping list is now', shoplist
