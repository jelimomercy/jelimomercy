def verify_input(self, input_index):
    tx_in = self.tx_ins[input_index]
    script_pubkey = tx_in.script_pubkey(testnet=self.testnet)
    z = self.sig_hash(input_index)
    combined = tx_in.script_sig + script_pubkey
    return combined.evaluate(z)