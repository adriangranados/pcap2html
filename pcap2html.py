#
# pcap2html.py
# This script generates an HTML view of the contents of a PCAP file.
# Based on Eric Garnel's BASH script.
# Version 1.0
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. YOU MAY
# NOT COPY, MODIFY, SUBLICENSE, OR DISTRIBUTE THIS SOFTWARE.
#
# Copyright (c) 2017 Adrian Granados. All rights reserved.
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

