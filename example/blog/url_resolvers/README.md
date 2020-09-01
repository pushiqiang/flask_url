## Django-Style URL Patterns for Flask


### Config
ROOT_URLCONF = 'example.urls'

### Centralized routing file: urls.py

```json
from url_resolvers import url, include

from example.views import index, upload, PostListView


urlpatterns = [
    url('index/', index, name='index'),
    url('upload/', upload, name='upload', methods=['POST']),
    url('list/', PostListView.as_view('test'), name='list'),
]
```
