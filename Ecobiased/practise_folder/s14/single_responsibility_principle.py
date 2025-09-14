# violates SRP

class Report:

    def generate_report(self):
        return "Report Content"

    def save_to_file(self, content):
        with open('report.txt', 'w') as file:
            file.write(content)


# follow SRP

class Report1:

    def generate_report(self):
        return "Report Content"


class FileSaver:

    def save(self, content):
        with open('report.txt', 'w') as file:
            file.write(content)