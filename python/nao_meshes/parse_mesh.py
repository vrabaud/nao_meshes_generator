#!/usr/bin/env python
import xml.etree.ElementTree as ET
import os
import urllib2

def main():
    print os.path.exists('NaoV4H21.rsi2')
    if not os.path.exists('NaoV4H21.rsi2'):
        url = 'https://raw.github.com/bhuman/BHuman2013/master/Config/Scenes/NaoV4H21.rsi2'
        f = urllib2.urlopen(url)
        local_file = open(os.path.basename(url), "wb")
        local_file.write(f.read())
    tree = ET.parse('NaoV4H21.rsi2')

if __name__ == '__main__':
    main()
