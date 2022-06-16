# simple URL cleaner for large lists

from urllib.parse import urlparse

with open("C:/Users/xxxx/desktop/url2.txt") as text_data:
    for line in text_data:
        parsed_url = urlparse(line)
        cleaned_url = parsed_url.netloc
        url_fixed = cleaned_url.replace("[.]", ".")
        url_fixed2 = url_fixed.replace("www.", "")
        print(url_fixed2)

text_data.close()
