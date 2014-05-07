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
#> { 'total_count': 2950 }

shares = facebook.getShares(url)
print shares
#> { 'share_count': 114 }

comments = facebook.getComments(url)
print comments
#> { 'comment_count': 720 }

likes = facebook.getLikes(url)
print likes
#> { 'like_count': 2116 }
```

#### Pinterest

Grabs the number of Pins for a URL.

```python
from socialanalytics import pinterest

url = 'http://allrecipes.com/recipe/crispy-edamame/detail.aspx'
pin_count = pinterest.getPins(url)
print pins_count
#> { 'pin_count': 962508 }
```

#### Twitter

Grabs the number of Twitter shares for a URL.

```python
from socialanalytics import twitter

url = 'http://www.mindbodygreen.com/0-13633/an-11-minute-breathing-exercise-for-stronger-abs-a-clearer-mind.html'
share_count = pinterest.getPins(url)
print share_count
#> { 'share_count': 52 }
```

#### Google+

Grabs the number of Google+ +1's for a URL.

```python
from socialanalytics import google_plus

url = 'http://www.theatlantic.com/business/archive/2014/03/how-you-i-and-everyone-got-the-top-1-percent-all-wrong/359862/'
plus_count = google_plus.getPlusOnes(url)
print plus_count
#> { 'plus_count': 434 }
```

