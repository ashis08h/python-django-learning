# violates SRP


class Report:

    def generate_report(self):
        return "Report content"

    def save_file(self, content):
        with open('save.txt', 'w') as file:
            file.write(content)


# follow SRP


class Report1:

    def generate_report(self):
        return "Report content"


class FileSaver:

    def save_to_file(self, content):
        with open('report.txt', 'w') as file:
            file.write(content)

