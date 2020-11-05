from disease import disease
from gen_profile import gen_profile
import csv


def write_csv(pro):
    with open('output.csv', 'w', newline='', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerows(pro)


if __name__ == '__main__':
    disease = disease()
    count = int(input())
    profile = gen_profile(count, disease)
    write_csv(profile)
