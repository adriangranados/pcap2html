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

For example:

```bash
python pcap2html.py ~/Desktop/mycapture.pcap
```
generates ```~/Desktop/mycapture.pcap.html```.

## Notes

The conversion requires an intermediate transformation to XML, which is currently done in memory. As a result, conversion of large files may be very slow.
