#!/usr/bin/python

import random
import string

letters = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
numbers = '1234567890'
special = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ!@#$%&^'
chars = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ!@#$%&^1234567890'

def RandomPasswordGenerator(passLen=10):
    password= ''
    for c in range(passLen):
        password += random.choice(chars)

    return password