__author__ = 'karnikamit'
from simpleconfigparser import simpleconfigparser
import os
import StringIO
from flask import send_file
configfile = simpleconfigparser()


class Download:
    def __init__(self, path):
        app_route = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
        configfile.read(app_route+'/Downloads/down.ini')
        self.path = path
        self.f_name = (self.path.split('.')[0]).split('/')[-1]
        self.extn = self.path.split('.')[-1]

    def download_file(self):
        file_open = open(self.path, 'rb')
        f = file_open.read()

        # Downloading the file
        strIO = StringIO.StringIO()
        strIO.write(f)
        strIO.seek(0)
        file_open.close()
        return send_file(strIO,
                         attachment_filename=self.f_name+'.'+self.extn,
                         as_attachment=True)
