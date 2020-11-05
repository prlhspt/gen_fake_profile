from random import random, randrange, choice
from faker import Faker


def gen_profile(count, disease):
    profile = []
    fake = Faker("ko_KR")

    for i in range(count):
        ida = []
        p = fake.profile()
        ida.append(p['name'])
        ida.append(p['ssn'])
        ida.append('M' + str(randrange(10000000, 99999999, 1)))
        ida.append(p['mail'])
        ida.append(p['residence'])
        ida.append(fake.phone_number())

        if random() > 0.5:
            ida.append(str(randrange(11, 26, 1)) + '-' + str(randrange(60, 99, 1)) + '-' +
                       str(randrange(100000, 999999)) + '-' + str(randrange(1, 9, 1)) + str(randrange(1, 5, 1)))
        else:
            ida.append(str(randrange(11, 26, 1)) + '-' + str(randrange(0, 9, 1)) + str(randrange(0, 9, 1)) +
                       '-' + str(randrange(100000, 999999)) + '-' + str(randrange(1, 9, 1)) + str(randrange(1, 5, 1)))

        ida.append(randrange(10000000, 99999999, 1))

        if p['ssn'][0] == '0':
            ida.append(2020 - (int(p['ssn'][0:2]) + 2000))
        else:
            ida.append(2020 - (int(p['ssn'][0:2]) + 1900))

        if p['sex'] == 'M':
            ida.append(randrange(160, 190, 1))
            ida.append(randrange(55, 100, 1))
        else:
            ida.append(randrange(150, 180, 1))
            ida.append(randrange(45, 80, 1))

        ida.append(choice(disease))

        profile.append(ida)

    return profile
