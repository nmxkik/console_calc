import csv


class History():

    def create_calculation_history_csv_with_headers():
        with open("calculation_history.csv", "wt", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["№", "request", "answer"])

    def write_line_in_calculation_history_csv(answer):
        with open("calculation_history.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(answer)

    def get_nomber_of_lines():
        number = 0
        with open("calculation_history.csv", "r") as f:
            for line in f:
                number += 1
            return(number)

    def get_calculation_history():
        with open("calculation_history.csv", "r") as f:
            history_reader = csv.reader(f)
            for row in history_reader:
                print(", ".join(row))
