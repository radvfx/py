#!/usr/local/bin/python2.3

product = 'chr_hit.pit'
version = 3
spref = 'spref_eval "{' + product + "?ver=" + str(version) + '}"'
print spref

spref2 = 'spref_eval "{' + "%s?ver=%d" % (product,version) + '}"'
print spref2

