import re


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def extract_emails(self):
        def extract_email(text):
            pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(ru|com|org|net)'
            match = re.search(pattern, text)
            if match:
                return match.group(0)
            return None

        emails = []
        for t in self.text.split():
            email = extract_email(t)
            if email:
                emails.append(email)

        emails = set(emails)
        return sorted(emails)


input_text = input()
processor = TextProcessor(input_text)

found_emails = processor.extract_emails()
if found_emails:
    print("\n".join(found_emails))
else:
    print("Не найдено")
