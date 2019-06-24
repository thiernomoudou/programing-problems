import os, sys
import hashlib

def find_duplicates(parentFolder):
    # duplicate in format {hash:[names]}
    
    if not os.path.exists(parentFolder):
        return '{} is not a valid path, please verify'.format(parentFolder)

    dups = {}
    # Duplicate list
    duplicate_list = []
    for dirName, subdirs, filelist in os.walk(parentFolder):
        print('Scanning {}'.format(dirName))
        for filename in filelist:
            # Pick the path of the file
            path = os.path.join(dirName, filename)
            # Getting the last time inode
            date = os.path.getctime(path)
            # Determine the hash
            file_hash = hash_file(path)
            # Add the file path to the duplicate dictionnary
            if file_hash in dups:
                dups[file_hash].append((path, date))
            else:
                dups[file_hash] = [(path, date)]

    for key in dups:
        if len(dups[key]) > 1:
            # Sort the list by creation date to alwas get the original file
            # at the end of the list
            value = sorted(dups[key], key = lambda l: l[1], reverse=True)
            tup = []
            for element in value:
                tup.append(element[0])
            duplicate_list.append(tuple(tup))

    return duplicate_list


def hash_file(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buff = afile.read(blocksize)
    while len(buff) > 0:
        hasher.update(buff)
        buff = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

path='dup'
print(find_duplicates(path))