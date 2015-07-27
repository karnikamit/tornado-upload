__author__ = 'karnikamit'
import StringIO
from flask import send_file


class Download:
    def __init__(self, path):
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
