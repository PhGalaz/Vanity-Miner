from bitcoin import *
import timeit
import random


def main():
    privkey = random.randrange(2**256)
    search_for = '1abc'
    address = ''
    count = 0
    start = timeit.default_timer()
    pubkey_point = ''

    print "Searching for %s" % search_for

    while not search_for in address:
        privkey += 1
        pubkey_point = fast_multiply(G, privkey)
        address = pubkey_to_address(pubkey_point)
        count += 1
        if not count % 1000:
            print "Searched %d in %d seconds" % (count, timeit.default_timer()-start)

    print "Found address %s" % address
    print "Private key HEX %s" % encode_privkey(privkey,'hex')


if __name__ == '__main__':
	main()