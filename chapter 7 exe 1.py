def sig_hash(self, input_index):
    s = int_to_little_endian(self.version, 4)
    s += encode_varint(len(self.tx_ins))
    for i, tx_in in enumerate(self.tx_ins):
        if i == input_index:
            s += TxIn(
                prev_tx=tx_in.prev_tx,
                prev_index=tx_in.prev_index,
                script_sig=tx_in.script_pubkey(self.testnet),
                sequence=tx_in.sequence,
            ).serialize()
        else:
            s += TxIn(
                prev_tx=tx_in.prev_tx,
                prev_index=tx_in.prev_index,
                sequence=tx_in.sequence,
            ).serialize()
    s += encode_varint(len(self.tx_outs))
    for tx_out in self.tx_outs:
        s += tx_out.serialize()
    s += int_to_little_endian(self.locktime, 4)
    s += int_to_little_endian(SIGHASH_ALL, 4)
    h256 = hash256(s)
    return int.from_bytes(h256, 'big')