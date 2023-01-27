from urllib import request
url = "http://olympus.realpython.org/profiles/dionysus"
Base_url = "http://olympus.realpython.org"
web_page = request.urlopen(url)
web_read = web_page.read()
webHTML = web_read.decode("utf-8")
Links = []
start_p = 0
no_of_img = webHTML.count("<img", start_p)

#For extracting link
for img in range(no_of_img):
    img_start = webHTML.find("<img", start_p)
    src_start = webHTML.find("src", img_start)
    src_end = webHTML.find('"', src_start+5)
    src = webHTML[src_start+5: src_end]

    if not src.startswith("http"):
        src = Base_url + src

    Links.append(src)
    start_p = src_end

counter = 0

#For Downloading image
for img in Links:
    img_data = request.urlopen(img)
    img_read = img_data.read()
    img_file = open(f"{counter}.jpg", "wb")
    img_file.write(img_read)
    img_file.close()
    counter += 1

print(counter)
print(Links)