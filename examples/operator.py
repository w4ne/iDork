from idork import Google

dork = Google("http://127.0.0.1")
resp = dork.search("inurl: \"robots.txt\" filetype:txt", lang="en", results=100)

for result in resp:
    ...
    
