# Python

# m3uextrator

# Version 1.0
# written by Maudam
# license Gplv2

# importing module(s)
import sys
import re  # regular expressions
import argparse
# import os
# import pdb
# import cmd


# Arguments passed at command line
# argparse module

parser = argparse.ArgumentParser(description="Usage syntax:",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# parser.add_argument("-a", "--archive", action="store_true", help="archive mode")
# parser.add_argument("-v", "--verbose", action="store_true", help="increase verbosity")
# parser.add_argument("-B", "--block-size", help="checksum blocksize")
# parser.add_argument("--ignore-existing", action="store_true", help="skip files that exist")
# parser.add_argument("--exclude", help="files to exclude")
parser.add_argument("input", help="Source location")
parser.add_argument("output", help="Destination location")
args = parser.parse_args()
# config = vars(args)
# print(config)

filetoproc = args.input
fileout = args.output

print('Input file:  ' + filetoproc)
print('Output file: ' + fileout)

# print('We are after parsing')
# sys.exit()

file1 = open(filetoproc, 'r', errors="ignore", encoding="utf8")
file2 = open(fileout, 'w', encoding="utf8")
Filecontent = file1.readlines()
Numlines = len(Filecontent)
print('Lines in input file: ' + str(Numlines))

# pdb.set_trace()

Count = 0
Outputrow = 0

while Count < Numlines:
    Rigo1 = Filecontent[Count]
    if Rigo1[:7] == '#EXTINF':
        # Row starting with #EXTINF found
        Rigo2 = Filecontent[Count+1]
        if Rigo2[:4] != 'http':
            print('Error!')
            print('Last two lines:')
            print(Rigo1)
            print(Rigo2)
            sys.exit(1)

        print('Input file row: ' + str(Count) + ' -- Output file row: ' + str(Outputrow))
        print(Rigo1.rstrip())
        print(Rigo2.rstrip())

        # Search fields

        # tvg-id
        searchtvgid = re.search(r"tvg-id=\"([^\"]+)\"", Rigo1)
        if searchtvgid:
            tvgid = searchtvgid[1]
        else:
            tvgid = ''

        # tvg-name
        searchtvgname = re.search(r"tvg-name=\"([^\"]+)\"", Rigo1)
        if searchtvgname:
            tvgname = searchtvgname[1]
        else:
            tvgname = ''

        # tvg-logo
        searchtvglogo = re.search(r"tvg-logo=\"([^\"]+)\"", Rigo1)
        if searchtvglogo:
            tvglogo = searchtvglogo[1]
        else:
            tvglogo = ''

        # group-title
        searchgrouptitle = re.search(r"group-title=\"([^\"]+)\"", Rigo1)
        if searchgrouptitle:
            grouptitle = searchgrouptitle[1]
        else:
            grouptitle = ''

        # lastgroup
        lastgroup = Rigo1.rsplit(',', 1)[1].rstrip()

        # baseurl
        baseurl = Rigo2.rstrip()
        Filename = baseurl.rsplit('/', 1)[1].rstrip()
        try:
            Filesuf = Filename.rsplit('.', 1)[1].rstrip()
        except IndexError:
            Filesuf = ''

        print('  tvg-id= ' + tvgid)
        print('  tvg-name= ' + tvgname)
        print('  tvg-logo= ' + tvglogo)
        print('  group-title= ' + grouptitle)
        print('  lastgroup= ' + lastgroup)
        print('  baseurl= ' + baseurl)
        print('  filename= ' + Filename)
        print('  filesuf= ' + Filesuf)
        print('--')

        # Write to output file

        Outputrow +=1

        if Filesuf == '':
            Outputrowdelimited = '"' + baseurl + '#name=' + tvgname + '"'
            Outputrownotdelimited = baseurl + '#name=' + tvgname
        else:
            Outputrowdelimited = '"' + baseurl + '#name=' + tvgname + '.' + Filesuf + '"'
            Outputrownotdelimited = baseurl + '#name=' + tvgname + '.' + Filesuf


        print('  Output row not delimited: ' + Outputrownotdelimited)
        print('------------------------------------------------------')
        # print('---------')
        file2.write(Outputrownotdelimited + '\n')

    Count += 1


file1.close
file2.close
