import os.path
from glob import glob
from datetime import datetime


class HttpServer:
    def __init__(self):
        self.sessions = {}
        self.types = {'.pdf': 'application/pdf',
                      '.jpg': 'image/jpeg',
                      '.txt': 'text/plain',
                      '.html': 'text/html'}

    def response(self, kode=404, message='Not Found', messagebody=bytes(), headers={}):
        tanggal = datetime.now().strftime('%c')

        resp = ["HTTP/1.0 {} {}\r\n".format(kode, message),
                "Date: {}\r\n".format(tanggal),
                "Connection: close\r\n",
                "Server: myserver/1.0\r\n",
                "Content-Length: {}\r\n".format(len(messagebody))]

        for kk in headers:
            resp.append("{}:{}\r\n".format(kk, headers[kk]))

        resp.append("\r\n")
        response_headers = ''

        for i in resp:
            response_headers = "{}{}".format(response_headers, i)

        # menggabungkan resp menjadi satu string dan menggabungkan dengan messagebody yang berupa bytes
        # response harus berupa bytes
        # message body harus diubah dulu menjadi bytes

        if type(messagebody) is not bytes:
            messagebody = messagebody.encode()

        response = response_headers.encode() + messagebody

        # response adalah bytes
        return response

    def proses(self, data):
        requests = data.split("\r\n")
        baris = requests[0]

        all_headers = [n for n in requests[1:] if n != '']
        j = baris.split(" ")

        try:
            method = j[0].upper().strip()

            if method == 'GET':
                object_address = j[1].strip()
                return self.http_get(object_address, all_headers)

            if method == 'POST':
                object_address = j[1].strip()
                return self.http_post(object_address, all_headers)

            else:
                return self.response(400, 'Bad Request', '', {})

        except IndexError:
            return self.response(400, 'Bad Request', '', {})

    def http_get(self, object_address, headers):
        files = glob('./*')
        thedir = '.'

        if thedir + object_address not in files:
            return self.response(404, 'Not Found', '', {})

        fp = open(thedir + object_address, 'rb')
        # rb => artinya adalah read dalam bentuk binary
        # harus membaca dalam bentuk byte dan BINARY

        isi = fp.read()
        fext = os.path.splitext(thedir + object_address)[1]
        content_type = self.types[fext]
        headers = {'Content-type': content_type}

        return self.response(200, 'OK', isi, headers)

    def http_post(self, object_address, headers):
        headers = {}
        isi = "kosong"
        return self.response(200, 'OK', isi, headers)


if __name__ == "__main__":
    httpserver = HttpServer()
