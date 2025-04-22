#!/bin/env python3

name = 'Tom'
bal = 25.5688888
# Display: name has bal 

# Method 1: using concatunation
print(name+' has '+str(bal))

# Method 2: using comma (or string joining)
print(name,'has',bal)

# Method 3: using format modes
print('%s has %f'%(name,bal))
print('%s has %.2f'%(name,bal))
print('%10s has %12.2f'%(name,bal))
print('%-10s has %-12.2f'%(name,bal))

# Method 4: using the string format function
print('{} has {}'.format(name, bal))
print('{} has {:.3f}'.format(name, bal))
print('{:>10} has {:15.3f}'.format(name, bal))
print('{:<10} has {:^15.3f}'.format(name, bal))
print('{:*<10} has {:$^15.3f}'.format(name, bal))

# Method 5: using f-string 
print(f'{name} has {bal}')
print(f'{name} has {bal:.3f}')
print(f'{name:>10} has {bal:15.3f}')
print(f'{name:<10} has {bal:^15.3f}')
print(f'{name:*<10} has {bal:$^15.3f}')







