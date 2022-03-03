<div id="top"></div>
<p align="center">
  <img src="https://img.shields.io/github/contributors/w4ne/iDork.svg?style=for-the-badge"/>
  <img src="https://img.shields.io/github/forks/w4ne/iDork.svg?style=for-the-badge"/>
  <img src="https://img.shields.io/github/stars/w4ne/iDork.svg?style=for-the-badge"/>
  <img src="https://img.shields.io/github/issues/w4ne/iDork.svg?style=for-the-badge"/>
</p>
  
---------------------------------------
  
<br/>
<div align="center">
  <a href="https://github.com/w4ne/iDork">
    <img src="https://www.radarfirst.com/wp-content/uploads/2019/12/RadarFirst-Icon-1.png" alt="Logo" width="100" height="100">
  </a>
  
  <h2 align="center">iDork</h3>

  <p align="center">
    A Python library used to search content on Google and find websites with keywords.
    <br />
    <br />
    <img src="https://img.shields.io/badge/Version-1.0.0-7DCDE3?style=for-the-badge" alt="Version">
  </p>
</div>
  
# 🔨 Installation
```
python3 -m pip install idork
```

# ⚙️ Usage
### Examples
```python
from idork import Google

dork = Google(proxy_url=None)
dork.search("Cooking Recipes", results=10)
```

---

```python
from idork import Google

dork = Google(proxy_url=None)
resp = dork.search("inurl: \"robots.txt\" filetype:txt", lang="en", results=100)

for result in resp:
    ...
```

# 📝 Todo
* [ ] Add better proxy support
* [ ] Support more search engines

# Other
* [Pypi](https://pypi.org/project/idork/1.0.0/)
* [MIT Licence](https://github.com/w4ne/iDork/blob/main/LICENCE)
