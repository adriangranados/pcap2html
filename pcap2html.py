#!/usr/bin/python

# pcap2html.py
# This script generates an HTML view of the contents of a PCAP file.
# Based on Eric Garnel's BASH script.
# Version 1.0
#
# Copyright (c) 2018 Adrian Granados. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Notes:
# - It requires Wireshark (www.wireshark.org) installed.
#

import os
import sys
import re
import tempfile
import lxml.etree as et
from shutil import copyfile
from subprocess import call

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: pcap2html <input_file>")
        sys.exit(-1)

    pcapfile = sys.argv[1]
    xmlfile = pcapfile + ".xml"
    htmlfile = pcapfile + ".html"

    # Create temporary file
    temp = tempfile.NamedTemporaryFile(dir='/tmp')

    try:
        # Convert pcap to pdml
        call(["tshark", "-I", "-T", "pdml", "-r", pcapfile], stdout=temp)

        # Convert pdml to html
        dom = et.parse(temp.name)
        xslt = et.parse("/Applications/Wireshark.app/Contents/Resources/share/wireshark/pdml2html.xsl")
        transform = et.XSLT(xslt)
        html = et.tostring(transform(dom), pretty_print=True)

        # Fix title
        html = re.sub('<title>.*</title>', '<title>' + pcapfile + '</title>', html)

        # Fix javascript declaration
        html = html.replace('type="text/javascript"/>', 'type="text/javascript"/></script>', 1)

        # Fix javascript functions
        html = html.replace('length &gt; 0', 'length > 0')

        with open(htmlfile, "wb") as f:
            f.write(html)

    finally:
        temp.close()
