from ecc import S256Point, G, N
from helper import hash256
e = 12345
z = int.from_bytes(hash256(b'Programming Bitcoin!'), 'big')
k = 1234567890
r = (k*G).x.num
k_inv = pow(k, N-2, N)
s = (z+r*e) * k_inv % N
print(e*G)
S256Point(f01d6b9018ab421dd410404cb869072065522bf85734008f105cf385a023a80f, \
0eba29d0f0c5408ed681984dc525982abefccd9f7ff01dd26da4999cf3f6a295)
print(hex(z))
0x969f6056aa26f7d2795fd013fe88868d09c9f6aed96965016e1936ae47060d48
print(hex(r))
0x2b698a0f0a4041b77e63488ad48c23e8e8838dd1fb7520408b121697b782ef22
print(hex(s))
0x1dbc63bfef4416705e602a7b564161167076d8b20990a0f26f316cff2cb0bc1a
