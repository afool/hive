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
    try:
        url = "%s/%s" %(host_url, post_url)
        soup = get_soup_from_htmlstream(url)
        
        title_block_list = soup.findAll("td", "mw_basic_view_subject")
        title = title_block_list.pop()
        content_block_list = soup.findAll("td","mw_basic_view_content")
        content = content_block_list.pop()#td_list = soup.findAll('td')
        
        # replace relative url to absolute url
        str_content = str(content)    
        str_content = str_content.replace("../", "%s/" %(host_url))
        str_content = str_content.replace("&lt;/xml&gt;&lt;/xmp&gt;", "")
        
        str_title = str(title)
        str_title = str_title.replace("<h1>", "<h3>")
        
        return ( str_title +"<br/>" + str_content )
    except:
        return "Error Occured On retrieving Contents From (%s)" %(url)

def get_post_list(host_url=SEARCH_HOST, board_url=DOGDRIP_BEST_URL):
    url = "%s/%s" %(host_url, board_url)
    soup = get_soup_from_htmlstream(url)
    subject_td_list = soup.findAll("td", "mw_basic_list_subject")
    post_url_list = []
    for subject_td in subject_td_list:
        url = subject_td.findAll("a")[0].get('href')
        if( url.find('best=1') > -1 ):
            post_url_list.append(url[3:])
    
    return post_url_list

#example code
#post_list = get_post_list()
#content = get_contents_from_post(post_url=post_list[3])





