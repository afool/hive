from BeautifulSoup import BeautifulSoup
import html5lib
from html5lib import sanitizer
from html5lib import treebuilders
import urllib

SEARCH_HOST = 'http://www.dogdrip.com'
DOGDRIP_BEST_URL = 'bbs/board.php?bo_table=dogdrip&best=1'

def get_soup_from_htmlstream(url):
    fp = urllib.urlopen(url)
    parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("beautifulsoup"), tokenizer=sanitizer.HTMLSanitizer)
    
    # Load the source file's HTML into html5lib
    html5lib_object = parser.parse(fp)
    # In theory we shouldn't need to convert this to a string before passing to BS. Didn't work passing directly to BS for me however.
    html_string = str(html5lib_object)
    # Load the string into BeautifulSoup for parsing.
    soup = BeautifulSoup(html_string)
    return soup

def get_contents_from_post(post_url, host_url=SEARCH_HOST):
    url = "%s/%s" %(host_url, post_url)
    print url
    soup = get_soup_from_htmlstream(url)
    
    content_block_list = soup.findAll("td","mw_basic_view_content")
    #td_list = soup.findAll('td')
    #for tdtag in td_list:
    #    if tdtag.get('class') == 'mw_basic_view_content' :
    #        print tdtag
    return content_block_list

def get_post_list(host_url=SEARCH_HOST, board_url=DOGDRIP_BEST_URL):
    url = "%s/%s" %(host_url, board_url)
    soup = get_soup_from_htmlstream(url)
    subject_td_list = soup.findAll("td", "mw_basic_list_subject")
    post_url_list = []
    for subject_td in subject_td_list:
        url = subject_td.findAll("a")[1].get('href')
        if( url.find('best=1') > -1 ):
            post_url_list.append(url[3:])
    
    return post_url_list

#Example code 
#for url in get_post_list():
#    print "==================================="
#    print get_contents_from_post(post_url=url)






