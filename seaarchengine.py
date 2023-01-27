import os
import time


class search:
    def __init__(self, address):
        self.path = os.scandir(address)

    def __str__(self):
        print('Date Created\t\t   Date Accessed\t      Date Modified\t\t Size(in bytes)\t    Name')
        return f'{self.info()}'

    def dir_check(self, entry):
        if entry.is_dir():
            path = os.scandir(entry)
            for entry in path:
                if entry.is_dir():
                    self.dir_check(entry)
                if entry.is_file():
                    return entry.name, entry.path
        if entry.is_file():
            return entry.name, entry.path

    def isdir(self, path):
        path = os.scandir(path)
        for entry in path:
            if entry.is_dir():
                self.isdir(entry.path)
            elif entry.is_file():
                self.name = entry.name
                path = entry.path
                info = os.stat(path)
                self.size = info.st_size
                self.ctime = time.ctime(info.st_ctime)
                self.mtime = time.ctime(info.st_mtime)
                self.atime = time.ctime(info.st_atime)
                print(f'{self.ctime}   {self.atime}   {self.mtime}   ''%15d' % self.size, f'   {self.name}')

    def info(self):
        for entry in self.path:
            if entry.is_dir():
                self.isdir(entry.path)
            elif entry.is_file():
                self.name = entry.name
                path = entry.path
                print(path)
                info = os.stat(path)
                self.size = info.st_size
                self.ctime = time.ctime(info.st_ctime)
                self.mtime = time.ctime(info.st_mtime)
                self.atime = time.ctime(info.st_atime)
                print(f'{self.ctime}   {self.atime}   {self.mtime}   ''%15d' % self.size, f'   {self.name}')


a = search('C:\\')
print(a)