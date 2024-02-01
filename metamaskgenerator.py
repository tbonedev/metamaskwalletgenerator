from sha3 import keccak_256
from coincurve import PublicKey
from secrets import token_bytes
from mnemonic import Mnemonic

def generate_ethereum_wallet():
    mnemo = Mnemonic('english')
    seed_phrase = mnemo.generate(128)
    seet = mnemo.to_seed(seed_phrase)
    private_key = keccak_256(token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]

    private_key_hex = private_key.hex()
    public_key_hex = public_key.hex()
    address_hex = addr.hex()

    print('private_key:', private_key_hex)
    print('eth addr: 0x' + address_hex)
    print('seed_phrase:', seed_phrase)

    return private_key_hex, public_key_hex, address_hex, seed_phrase

wallets = [generate_ethereum_wallet() for i in range(1)] # Here you can change quantity of wallets.

with open('wallets.py', 'w') as file:
    for private_key, _, address, seed_phrase in wallets:
        file.write(f'private_key: {private_key}\neth_addr: 0x{address}\nseed_phrase: {seed_phrase}\n\n')
