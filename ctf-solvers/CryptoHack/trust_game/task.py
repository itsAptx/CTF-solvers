#!/usr/bin/env python3.8
from Crypto.Cipher import AES
from os import urandom
from Crypto.Util.number import bytes_to_long
from json import loads

FLAG = 'crypto{??????????????????????}'


class LCG:
    def __init__(self, a, b, m, seed):
        self.a = a
        self.b = b
        self.m = m
        self.state = seed
        self.counter = 0

    def refresh(self):
        self.counter = 0
        self.state = bytes_to_long(urandom(6))

    def next_state(self):
        self.state = (self.a * self.state + self.b) % self.m

    def get_random_bits(self, k):
        if self.counter == 16:
            self.refresh()
        self.counter += 1
        self.next_state()
        return self.state >> (48 - k)

    def get_random_bytes(self, number):
        bytes_sequence = b''
        for i in range(number):
            bytes_sequence += bytes([self.get_random_bits(8)])
        return bytes_sequence


class Challenge():
    def __init__(self):
        a = 0x1337deadbeef
        b = 0xb
        m = 2**48
        seed = bytes_to_long(urandom(6))
        self.G = LCG(a, b, m, seed)
        self.plaintext = self.G.get_random_bytes(16)
        self.key = self.G.get_random_bytes(16)
        self.IV = self.G.get_random_bytes(16)
        self.before_input = f"Let's play a game, Player {self.G.get_random_bytes(8).hex()}. If you can encrypt the plaintext that I will give you with my secret key, you will be worthy of my trust and a reward."

    def challenge(self, your_input):
        if your_input['option'] == 'get_a_challenge':
            msg = 'Try encrypting this plaintext with the given IV and my secret key!'
            self.plaintext = self.G.get_random_bytes(16)
            self.key = self.G.get_random_bytes(16)
            self.IV = self.G.get_random_bytes(16)
            return {'msg': msg, 'plaintext': self.plaintext.hex(), 'IV': self.IV.hex()}

        if your_input['option'] == 'validate':
            self.exit = True
            if 'ciphertext' not in your_input:
                return {'msg': 'You must provide a ciphertext...'}

            received_ct = bytes.fromhex(your_input['ciphertext'])
            cipher = AES.new(self.key, AES.MODE_CBC, self.IV)
            my_ct = cipher.encrypt(self.plaintext)
            if my_ct == received_ct:
                return {'msg': f'Here is a well deserved flag: {FLAG}'}
            else:
                return {'msg': f'The expected ciphertext was: {my_ct.hex()}. I knew you could not be trusted...'}

chal = Challenge()
print(chal.before_input)
while 1:
    inp = loads(input())
    print(chal.challenge(inp))