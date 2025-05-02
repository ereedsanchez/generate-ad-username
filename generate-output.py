"""
This script is based on the following naming convention :

NameSurname
Name.Surname
NamSur (3letters of each)
Nam.Sur
NSurname
N.Surname
SurnameName
Surname.Name
SurnameN
Surname.N
3 random letters and 3 random numbers (abc123) --> This one is not implemented

https://book.hacktricks.wiki/en/windows-hardening/active-directory-methodology/index.html#recon-active-directory-no-credssessions
"""

import csv
import argparse

parser = argparse.ArgumentParser(description='Generate AD username based on Name and Surname')
parser.add_argument('csvfilename', metavar="CSVFile", type=str, help='CSV File containing list of users')
parser.add_argument('-o', '--output', type=str, help='Output file to save usernames', default='usernames.txt')
args = parser.parse_args()


def opencsv(csvfilename):
    dict = []
    with open(csvfilename, 'r', encoding='utf-8-sig') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            dict.append([row[0], row[1]])
    return dict


def main():
    dict = opencsv(args.csvfilename)
    usernames = []

    for row in dict:
        name = row[0].lower()
        surname = row[1].lower()

        # Add all username combinations to the list
        usernames.append(name + surname)  # NameSurname
        usernames.append(name + "-" + surname)  # Name-Surname
        usernames.append(name + "." + surname)  # Name.Surname
        usernames.append(name[0:3] + surname[0:3])  # NamSur
        usernames.append(name[0:3] + "-" + surname[0:3])  # Nam-Sur
        usernames.append(name[0:3] + "." + surname[0:3])  # Nam.Sur
        usernames.append(name[0] + surname)  # NSurname
        usernames.append(name[0] + "-" + surname)  # N-Surname
        usernames.append(name[0] + "." + surname)  # N.Surname
        usernames.append(surname + name)  # SurnameName
        usernames.append(surname + "-" + name)  # Surname-Name
        usernames.append(surname + "." + name)  # Surname.Name
        usernames.append(surname[0:3] + name[0:3])  # SurNam
        usernames.append(surname[0:3] + "-" + name[0:3])  # Sur-Nam
        usernames.append(surname[0:3] + "." + name[0:3])  # Sur.Nam
        usernames.append(surname[0] + name)  # Sname
        usernames.append(surname[0] + "-" + name)  # S-name
        usernames.append(surname[0] + "." + name)  # S.name
        usernames.append(surname + name[0])  # SurnameN
        usernames.append(surname + "-" + name[0])  # Surname-N
        usernames.append(surname + "." + name[0])  # Surname.N

    # Print to console and save to file
    with open(args.output, 'w') as outfile:
        for username in usernames:
            print(username)
            outfile.write(username + '\n')

    print(f"\nGenerated {len(usernames)} username combinations saved to {args.output}")


if __name__ == "__main__":
    main()