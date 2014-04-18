# [socialanalytics](https://pypi.python.org/pypi/socialanalytics)

socialanalytics provides insight into how a specific URL performs on a variety of social networks.

## Installation

To install socialanalytics, simply:

`$ pip install socialanalytics`

## Documentation

#### Facebook

Grabs metrics from the Facebook Graph API for a URL

```python
from socialanalytics import facebook

url = 'http://espn.go.com/nfl/playoffs/2013/story/_/id/10395131/super-bowl-xlviii-seattle-seahawks-michael-bennett-doug-baldwin-talk-win'

fb_obj = facebook.getObject(url)
print fb_obj
#> {u'comment_count': 720, u'like_count': 2114, u'share_count': 114}

total = facebook.getTotalInteractions(url)
print total
#> 2948

shares = facebook.getShares(url)
print shares
#> 114

comments = facebook.getComments(url)
print comments
#> 720

likes = facebookgetLikes(url)
print likes
#> 2114
```

#### Pinterest

Grabs the number of Pins for a URL.

```python
from socialanalytics import pinterest

url = 'http://allrecipes.com/recipe/crispy-edamame/detail.aspx'
pins_count = pinterest.getPins(url)
print pins_count
#> 958634
```



