# simple URL cleaner for large lists

import urllib.parse

with open("C:/Users/xxxx/desktop/urls.txt") as text_data:
    for line in text_data:
        parsed_url = urllib.parse.urlparse(line)
        cleaned_url = parsed_url.netloc
        url_fixed = cleaned_url.replace("[.]", ".")
        final_urls = url_fixed.replace("www.", "")
        print(final_urls)
        
text_data.close()


