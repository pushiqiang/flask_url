## Django-Style URL Patterns for Flask


### 1. Configuration
ROOT_URLCONF = 'example.urls'

### 2. Auto register urls to flask app
```python
from flask import Flask
from url_resolvers import auto_register_urls
from example import config

app = Flask(__name__)
app.config.from_object(config)

# 自动注册urls路径
auto_register_urls(app)
```

### 3. Define centralized routing file: urls.py

```python
from url_resolvers import url, include

from example.views import index, upload, PostListView


urlpatterns = [
    url('index/', index, name='index'),
    url('upload/', upload, name='upload', methods=['POST']),
    url('list/', PostListView.as_view('test'), name='list'),
]
```
