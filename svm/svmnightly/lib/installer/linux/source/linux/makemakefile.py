# Write the actual Makefile.

import os
import string

def writevars(outfp, makevars, target):
    outfp.write("# Makefile generated by freeze.py script\n\n")

    keys = makevars.keys()
    keys.sort()
    for key in keys:
        outfp.write("%s=%s\n" % (key, makevars[key]))
    outfp.write("\nall: %s\n\n" % target)
    outfp.write("\nclean:\n\t-rm -f *.o %s\n" % target)

def writerules(outfp, files, suffix, dflag, target):
    deps = []
    for i in range(len(files)):
        file = files[i]
        if file[-2:] == '.c':
            base = os.path.basename(file)
            dest = base[:-2] + suffix + '.o'
            outfp.write("%s: %s\n" % (dest, file))
            outfp.write("\t$(CC) %s $(CFLAGS) -c %s -o %s\n" % (dflag, file, dest))
            files[i] = dest
            deps.append(dest)

    outfp.write("\n%s: %s\n" % (target, string.join(deps)))
    outfp.write("\t$(CC) %s -o %s $(LDLAST)\n" % 
                (string.join(files), target))


