import logging
import requests
import os
import threading


def download_gambar(url, i):
    if url is None:
        return False

    ff = requests.get(url)
    tipe = dict()
    tipe['image/png'] = 'png'
    tipe['image/jpg'] = 'jpg'
    tipe['image/jpeg'] = 'jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)

    if content_type in list(tipe.keys()):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi} thread {i}")

        fp = open(f"{namafile}.{ekstensi}", "wb")
        fp.write(ff.content)
        fp.close()

    else:
        return False


if __name__ == '__main__':
    file = ['https://www.its.ac.id/wp-content/uploads/2020/03/Hari-Musik-Nasional-01.jpg',
            'https://cafedelites.com/wp-content/uploads/2018/11/Creamy-Mash-Potatoes-IMAGE-4.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png']
    threads = []
    count = len(file)

    for i in range(count):
        t = threading.Thread(target=download_gambar, args=(file[i], i))
        threads.append(t)

    for thr in threads:
        thr.start()
