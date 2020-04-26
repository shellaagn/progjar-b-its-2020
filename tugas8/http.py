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
        all_headers = [n for n in requests[1:] if n != '']
        j = baris.split(" ")

        try:
            method = j[0].upper().strip()

            if method == 'GET':
                object_address = j[1].strip()
                object_address = object_address.replace('/', '')
                return self.http_get(object_address)

            if method == 'POST':
                temp = requests[-1].rsplit("=")
                form = temp[1]
                return self.http_post(all_headers, form)

            else:
                return self.response(400, 'Bad Request', '', {})

        except IndexError:
            return self.response(400, 'Bad Request', '', {})

    def http_get(self, object_address):
        if object_address == 'sending.html':
            fp = open(object_address, 'r')
            isi = fp.read()
            headers = {'Content-type': "text/html"}

        else:
            return self.response(404, 'Not Found', '', {})

        return self.response(200, 'OK', isi, headers)

    def http_post(self, headers, form):
        head = headers
        headers = {}
        temp = ""

        for i in head:
            temp = temp + i + "\n"

        isi = form+"\n"+temp
        return self.response(200, 'OK', isi, headers)


if __name__ == "__main__":
    httpserver = HttpServer()
