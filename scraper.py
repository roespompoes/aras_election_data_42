###################################################################################
# Twitter API scraper - designed to be forked and used for more interesting things
###################################################################################

import scraperwiki
import simplejson
import urllib2


QUERY = 'explosion'
GEOINFO = '515176,9.9167km'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'de'
NUM_PAGES = 150 

for page in range(1, NUM_PAGES+1):
    base_url = 'http://search.twitter.com/search.json?q=%s&geocode=%s&rpp=%s&lang=%s&page=%s' \
         % (urllib2.quote(QUERY), urllib2.quote(GEOINFO), RESULTS_PER_PAGE, LANGUAGE, page)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        for result in results_json['results']:
            data = {}
            data['to_user'] = result['to_user']
            data['id'] = result['id']
            data['text'] = result['text']
            data['from_user'] = result['from_user']
            data['from_user_id'] = result['from_user_id']
            data['to_user_id'] = result['to_user_id']
            data['source'] = result['source']
            data['iso_language_code'] = result['iso_language_code']
            data['profile_image_url'] = result['profile_image_url']
            data['created_at'] = result['created_at']
            data['geo'] = result['geo']
            print data['from_user'], data['text']
            scraperwiki.sqlite.save(["id"], data) 
    except:
        print 'Oh dear, failed to scrape %s' % base_url
        
    
