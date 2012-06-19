import argparse
import shutil
import glob
import re
import os.path

description = 'Rename files by extension'

parser = argparse.ArgumentParser(description)
parser.add_argument('dir', metavar='Dir', type=str, help='the directory to rename files in')
parser.add_argument('oldExtension', metavar='Old-Extension', type=str, help='the extension to rename from')
parser.add_argument('newExtension', metavar='New-Extension', type=str, help='the extension to rename to')

if __name__ == '__main__':
    args = parser.parse_args()
    files = glob.glob(args.dir+"/*."+args.oldExtension)
    print args.dir+"/*."+args.newExtension
    regex = re.compile(r'^(.*)\.(\w+)$')
    for name in files:
        base, ext = os.path.splitext(name)
        newName = base + '.' + args.newExtension
        print 'renaming %(nm)s to %(nn)s' % {'nm':name, 'nn':newName}
        