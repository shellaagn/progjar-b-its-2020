from datetime import datetime


class HttpServer:
    def __init__(self):
        self.sessions = {}
        self.types = {'.pdf': 'application/pdf',
                      '.jpg': 'image/jpeg',
                      '.txt': 'text/plain',
                      '.html': 'text/html'}

    def response(self, kode=404, message='Not Found', messagebody='', headers={}):
        tanggal = datetime.now().strftime('%c')
        resp = ["HTTP/1.0 {} {}\r\n".format(kode, message),
                "Date: {}\r\n".format(tanggal),
                "Connection: close\r\n",
                "Server: myserver/1.0\r\n",
                "Content-Length: {}\r\n".format(len(messagebody))]

        for kk in headers:
            resp.append("{}:{}\r\n".format(kk, headers[kk]))

        resp.append("\r\n")
        resp.append("{}".format(messagebody))
        response_str = ''

        for i in resp:
            response_str = "{}{}".format(response_str, i)

        return response_str

    def proses(self, data):
        requests = data.split("\r\n")
        baris = requests[0]
        print(baris)
        j = baris.split(" ")

        try:
            method = j[0].upper().strip()

            if method == 'GET':
                object_address = j[1].strip()
                return self.http_get(object_address)

            else:
                return self.response(400, 'Bad Request', '', {})

        except IndexError:
            return self.response(400, 'Bad Request', '', {})

    def http_get(self, object_address):
        isi = '<h1>SERVER HTTP</h1>'
        headers = {}

        return self.response(200, 'OK', isi, headers)


if __name__ == "__main__":
    httpserver = HttpServer()

