import csv

headerlist = ["№", "request", "answer"]


class History():

    def refresh_csv_file():
        with open("calculation_history.csv", "wt", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headerlist)

    def write_answer_in_file(answer):
        with open("calculation_history.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(answer)

    def count_lines_in_csv():
        lines = 0
        with open("calculation_history.csv", "r") as f:
            for line in f:
                lines += 1
            return(lines)

    def read_history_file():
        with open("calculation_history.csv", "r") as f:
            history_reader = csv.reader(f)
            for row in history_reader:
                print(", ".join(row))
