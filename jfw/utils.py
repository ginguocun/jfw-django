import base64
from pathlib import Path
import rsa

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class NormalResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page': self.page.number,
            'num_pages': self.page.paginator.num_pages,
            'page_size': self.page.paginator.per_page,
            'results': data
        })


def rsa_encrypt(d_str):
    # 生成公钥和私钥
    if not Path('public.pem').exists():
        pubkey, privkey = rsa.newkeys(1024)
        pub = pubkey.save_pkcs1()
        pubfile = open('public.pem', 'wb')
        pubfile.write(pub)
        pubfile.close()
        pri = privkey.save_pkcs1()
        prifile = open('private.pem', 'wb')
        prifile.write(pri)
        prifile.close()
    else:
        with open('public.pem', 'rb') as publickfile:
            p = publickfile.read()
            pubkey = rsa.PublicKey.load_pkcs1(p)
    # 将字符串进行编码
    content = d_str.encode('utf-8')
    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    print('加密后', base64.b64encode(crypto))
    print(type(base64.b64encode(crypto)))
    return base64.b64encode(crypto)


def rsa_decrypt(crypto):
    with open('private.pem', 'rb') as privatefile:
        p = privatefile.read()
        privkey = rsa.PrivateKey.load_pkcs1(p)
    # 解密
    content = rsa.decrypt(base64.b64decode(crypto), privkey)
    # 解码
    content = content.decode('utf-8')
    print('解密结果', content)
    return content


if __name__ == '__main__':
    a = rsa_encrypt('+86 (122123)')
    rsa_decrypt(a)
