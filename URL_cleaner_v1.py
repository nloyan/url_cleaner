# simple URL cleaner for large lists

from urllib.parse import urlparse

with open("C:/Users/xxxx/desktop/url.txt") as text_data:
    for line in text_data:
        parsed_url = urlparse(line)
        cleaned_url = parsed_url.netloc
        url_fixed = cleaned_url.replace("[.]", ".")
        final_urls = url_fixed.replace("www.", "")
        print(final_urls)
        text_data.close()


