from urllib import request
URL = "https://www.w3schools.com/"
Base_url = "https://www.w3schools.com"
webpage = request.urlopen(URL)
web_read = webpage.read()
webHTML = web_read.decode("cp1252")
Links = []
start_p = 0
no_of_links = webHTML.count("<a", start_p)
for a in range(no_of_links):
    a_start = webHTML.find("<a", start_p)
    href_start = webHTML.find("href", a_start)
    href_end = webHTML.find('"', href_start+6)
    href = webHTML[href_start+6: href_end]
    if not href.startswith("http"):
        href = Base_url + href

    Links.append(href)
    start_p = href_end

counter = 1
print("These are the links found:")
for link in Links:
    print(f"{counter}.", link)
    counter += 1

print(f"There are a total of {len(Links)} links found")
