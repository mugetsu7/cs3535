#!/usr/bin/env python
# encoding: utf-8
"""
simple_stretch.py

Compress or exapand the entire track, beat by beat.  

Created by Thor Kell on 2013-11-18
"""
import math
import os
import sys
import dirac
from echonest.remix import audio

usage = """
Usage:
    python stretch.py <input_filename> <output_filename> <ratio> 
Example:
    python stretch.py CryMeARiver.mp3 StrechMeARiver.mp3
Notes:
    Ratio must be greater than 0.5
"""

def main(input_filename, output_filename, ratio):
    audiofile = audio.LocalAudioFile(input_filename)
    tatums = audiofile.analysis.tatums
    collect = []

    for tatum in tatums:
        tatum_audio = tatum.render()
        scaled_tatum = dirac.timeScale(tatum_audio.data, ratio)
        ts = audio.AudioData(ndarray=scaled_tatum, shape=scaled_tatum.shape, 
                        sampleRate=audiofile.sampleRate, numChannels=scaled_tatum.shape[1])
        collect.append(ts)

    out = audio.assemble(collect, numChannels=2)
    out.encode(output_filename)

if __name__ == '__main__':
    import sys
    try:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        ratio = float(sys.argv[3])
        if ratio < 0.5:
            print "Error:  Ratio must be greater than 0.5!"
            sys.exit(-1)
    except:
        print usage
        sys.exit(-1)
    main(input_filename, output_filename, ratio)
