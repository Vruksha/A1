'''This code will convert the user's input in seconds into number of
hours, minutes, and seconds.'''

#Ask the user to input number of seconds.
seconds = int(input('Seconds: '))

#The following will convert 
hours, seconds = seconds / 3600, seconds % 3600
minutes, seconds = seconds / 60, seconds % 60
print (round (hours), ':', round (minutes),':', round (seconds))


'''Since time is not read with decimal places, the above line ensures that the
hours, minutes, and seconds are rounded.'''
