def parse(cls, s, testnet=False):
        version = little_endian_to_int(s.read(4))
        return cls(version, None, None, None, testnet=testnet)
