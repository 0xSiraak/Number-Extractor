import sys, re

class Extractor:
    """ Principal number extractor class. """

    @staticmethod
    def get_numbers(file: str) -> str:
        """ Line recovery function. """
        numbers = file.readlines(
        )

        for number in numbers:

            regexs = [
                '336[0-9]{8}', r'337[0-9]{8}', r'06[0-9]{8}', r'07[0-9]{8}'
            ]

            for regex in regexs:
                if re.findall(regex, number):
                    list = re.findall(
                        regex, number
                    )
                    for x in list:
                        print(
                            f'[+] Number Extracted : {x}'
                        )
                        f = open(
                                 'output.txt', 'a'
                        )
                        f.write(
                            f'{x}\n'
                        )
                        f.close(
                        )

def main() -> None:
    """ Principal number extractor function. """

    try:
        """ Checks if the argument representing the file to read is written. """
        file = open(
            sys.argv[1], mode='r'
        )
    except:
        print(
            'you forgot your list... (python3 *.py *.txt)'
        )
        return

    Extractor.get_numbers(file)

    print('done.')

if __name__ == '__main__':
    main()
