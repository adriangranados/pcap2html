# pcap2html
This is Python script that generates an HTML view of the contents of a capture file.

![HTML View of Capture File](../master/pcap2html-example.png "HTML View of Capture File")

## Requirements

You need Python2 and [Wireshark](https://www.wireshark.org/).

## Usage

```bash
python pcap2html.py <input_file>
```
where ```<input_file>``` is a capture file.

The script generates an XML file that is then used to display the contents of the capture as HTML in Safari.

For example:

```bash
python pcap2html.py ~/Desktop/mycapture.pcap
```
generates ```~/Desktop/mycapture.pcap.xml``` and then launches Safari to display the contents of the capture file as HTML using the Wireshark's pdml2html.xls template.
