#!/bin/env python3

name = 'Tom'
bal = 12.295
# display always: name has bal

# Method 1: Using concatunation 
print(name+' has '+str(bal))

# Mthod 2: Printing multiple arguments
print(name,'has',bal)

# Method 3: Using format modes %s %f %d 
print('%s has %f'%(name,bal))
print('%s has %.3f'%(name,bal))
print('%10s has %15.3f'%(name,bal))
print('%-10s has %15.3f'%(name,bal))

# Method 4: Using format() function from string 
print('{} has {}'.format(name,bal))
print('{:15} has {:20.4f}'.format(name,bal))
print('{:>15} has {:^20.4f}'.format(name,bal))
print('{:_<15} has {:$^20.4f}'.format(name,bal))

# Method 5: USing f-string 
print(f'{name} has {bal}')
print(f'{name:#^12} has {bal:$>15.2f}')












