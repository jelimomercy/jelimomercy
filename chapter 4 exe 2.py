from ecc import PrivateKey
priv = PrivateKey(5001)
print(priv.point.sec(compressed=True).hex())
0357a4f368868a8a6d572991e484e664810ff14c05c0fa023275251151fe0e53d1
priv = PrivateKey(2019**5)
print(priv.point.sec(compressed=True).hex())
02933ec2d2b111b92737ec12f1c5d20f3233a0ad21cd8b36d0bca7a0cfa5cb8701
priv = PrivateKey(0xdeadbeef54321)
print(priv.point.sec(compressed=True).hex())
0296be5b1292f6c856b3c5654e886fc13511462059089cdf9c479623bfcbe77690