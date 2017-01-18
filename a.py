#! /usr/bin/python

from ffmpy import FFmpeg
from ffprobe import FFProbe
import os


def min2time(minutes):
    #m, s = divmod(int(seconds), 60)
    s = 0
    m = minutes
    h, m = divmod(m, 60)
    result = "%02d:%02d:%02d" % (h, m, s)
    return result

def sec2time(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    result = "%02d:%02d:%02d" % (h, m, s)
    return result

def getMinutes(seconds):
    return seconds / 60;

def pywalker(path):
    for root, dirs, files in os.walk(path):
        for file_ in files:
            print( "walking " + os.path.join(root,file_) )
            if isVideo(file_):
                generateScreenshot(file_)

def isVideo(file_):
    #print type(file_)
    if file_.endswith('.mp4') or file_.endswith('.avi'):
        return True
    return False

def generateScreenshot(file_):

    m=FFProbe(file_)
    for s in m.streams:
    	if s.isVideo():
    		framerate=s.frames()/s.durationSeconds()
    		print "framerate " + str(framerate)
    		print "frameSize " + str(s.frameSize())
    	print "durationSeconds " + str(s.durationSeconds())
    	print "frames " + str(s.frames())
    	print "isVideo " + str(s.isVideo())
        print "sec2time " + str(sec2time(s.durationSeconds()))
        minutes = getMinutes(s.durationSeconds())
        print "minutes " + str(minutes)
    #return 

    for i in range(5,int(minutes),5):
        print "minutes = " + str(i)
        hms = min2time(i)
        print "hms = " + hms
        longtime = hms.replace(':','')
        print "longtime = " + longtime
        timeasstring = hms
        image = file_ + '_' + longtime + '.jpg'
        print "target img= " + image
        inFile = file_
        outFile = image

        if os.path.isfile(outFile):
            print "skipping existing file " + outFile
            continue

        ff = FFmpeg(
            inputs={inFile : '-y -ss ' + timeasstring},
            outputs={outFile : '-vframes 1 -q:v 2'}
        )

        #         ffmpeg -y -ss 00:${i}:00 -i \""$file"\" -vframes 1 -q:v 2 \""${file}_00${i}00"\".jpg

        # -y = overwrite output file
        # -ss = seek to this time so not every frame is parsed


        print ff.cmd

        ff.run()


if __name__ == '__main__':
    pywalker('.')


