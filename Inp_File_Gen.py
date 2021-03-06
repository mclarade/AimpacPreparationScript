import os

filelist = os.listdir(os.curdir)
filelist.sort()
for file in filelist:
        if file.endswith(".wfn"):
                with open(file, 'r') as infile:
                        lines = infile.readlines()
                for i, line in enumerate(lines):
                        if i > 1:
                                splitline = line.split()
                                atomtype = splitline[0]
                                atomnumber = splitline[1]
                                if atomtype == 'CENTRE':
                                        break
                                outfile = open(file + atomtype + atomnumber + '.inp', 'w')
# This is to make sure there are 3 & 4 spaces when appropriate
                                if len(atomnumber) == 2:
                                        outfile.write(atomtype + atomnumber + '\n' + '  ' + atomtype + '   ' + atomnumber)
                                else:
                                        outfile.write(atomtype + atomnumber + '\n' + '  ' + atomtype + '    ' + atomnumber)
# These are options for aimpac, please consult the domcumentation for aimpac to understand what this is for
                                outfile.write('\nPROMEGA\n128 96 192\n')
                                outfile.write('OPTIONS\nINTEGER 2\n')
                                outfile.write('2 20\n4 3\n')
                                outfile.write('REAL 4\n1 18.0\n4 1.0D-12\n6 0.0001\n7 0.0005')
