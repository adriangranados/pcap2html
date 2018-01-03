#
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
from shutil import copyfile
from subprocess import call

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: pcap2html <input_file>")
        sys.exit(-1)

    pcapfile = sys.argv[1]
    xmlfile = pcapfile + ".xml"

    # Copy pdml2html.xsl
    template_source = "/Applications/Wireshark.app/Contents/Resources/share/wireshark/pdml2html.xsl"
    template_target = os.path.dirname(pcapfile) + "/pdml2html.xsl"
    copyfile(template_source, template_target)

    # Convert pcap to html
    f = open(xmlfile, "wb")
    call(["tshark", "-I", "-T", "pdml", "-r", pcapfile], stdout=f)
    call(["open", "-a", "Safari", xmlfile])

