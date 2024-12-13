import csv

def check_id(id, candidate) -> str:
    """
    Method to see if id has been used to vote before
    :param id:
    :param candidate:
    :return: Already voted or voted successfully
    """
    try:
        with open("votes.csv", "r") as input_csv_file:
            csv_reader = csv.reader(input_csv_file)
            for line in csv_reader:
                if line:
                    if int(line[0]) == id:
                        return "Already Voted"
            if int(candidate) == 1:
                candidate = "Jane"
            elif int(candidate) == 2:
                candidate = "John"
        return vote(id, candidate)
    except FileNotFoundError:
        with open("votes.csv", "w", newline = ""):
            pass
        check_id(id, candidate)


def vote(id, candidate)-> str:
    """
    Method to add vote to csv file
    :param id:
    :param candidate:
    :return: Voted successfully
    """
    with open('votes.csv', 'a', newline = '') as output_csv_file:
        content = csv.writer(output_csv_file)
        content.writerow([id, candidate])
        return "Voted Successfully"

