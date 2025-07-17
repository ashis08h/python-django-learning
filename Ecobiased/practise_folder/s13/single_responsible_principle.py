# Violates SRP

class Report:
    def generate(self):
        return "Report content"

    def save_to_file(self, content):
        with open('report.txt', 'w') as file:
            file.write(content)


# follow SRP

class Report1:
    def generate(self):
        return "Report content"


class FileSaver:
    def save(self, content):
        with open('report.txt', 'w') as file:
            file.write(content)

