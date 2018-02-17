import os
path = "/home/chris/Dropbox/K6"
def fcount(path):
    """ Counts the number of files in a directory """
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return (count-2)+100 

count_files = (fcount(path))

wrongnumber = open("/home/chris/Dropbox/K6/wrongnumber.xml", "w")

wrongnumber.write("It's 2037 and  the future has stopped. The sights have ceased  and all that remains are the sounds. Sounds of the last one hundred years playing on repeat. This is a 1937 K6 telephone box connected to a computer simulation of my voice. After this message please replace the handset and then dial any number between 101 and %d. Dial rather slowly and carefully and then wait for approximately 10 seconds of silence, yes, at least 10 whole seconds of silence, don't forget, 10 seconds during which you can drum your fingers, look through the windows, oar just dream. If the connection fails, you will hear beep, beep, beep, just try, try again. Thank you." % count_files)

poemnumber = open("/home/chris/Dropbox/K6/poemnumber.txt", "w")

poemnumber.write("%d" % count_files)

number_as_string = str(count_files)

print("%d" %count_files)






