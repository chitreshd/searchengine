import os.path
import searchengine.crawler
from nose.tools import *

def get_page_content():
	filename = 'testSample.html'
	dir = 'tests/private_web'
	path = os.path.join(os.path.curdir, dir,filename)
	test_sample_page = open(path)
	page = test_sample_page.read()
	test_sample_page.close()
	return page
	
def test_get_next_link():
	page = get_page_content()
		
	url, nxtPosn = searchengine.crawler.get_next_link(page)
	assert_equal(url,'https://www.google.com/')
	
	page = page[nxtPosn:]
	url, nxtPosn = searchengine.crawler.get_next_link(page)
	assert_equal(url,'http://www.yahoo.com/')
		
	page = page[nxtPosn:]
	url, nxtPosn = searchengine.crawler.get_next_link(page)
	assert_equal(url,'http://www.xkcd.com/')
	
	page = page[nxtPosn:]
	url, nxtPosn = searchengine.crawler.get_next_link(page)
	assert_equal(url,None)

def test_get_all_links():
	page = get_page_content()
	
	links = searchengine.crawler.get_all_links(page)
	
	assert_equal(links[0],'https://www.google.com/')
	assert_equal(links[1],'http://www.yahoo.com/')
	assert_equal(links[2],'http://www.xkcd.com/')
			


def test_crawl():
	links = searchengine.crawler.crawl('http://www.udacity.com/cs101x/index.html')
	assert 'http://www.udacity.com/cs101x/index.html' in links
	assert 'http://www.udacity.com/cs101x/flying.html' in links
	assert 'http://www.udacity.com/cs101x/walking.html' in links
	assert 'http://www.udacity.com/cs101x/crawling.html' in links
	assert 'http://www.udacity.com/cs101x/kicking.html' in links
	assert 'http://www.google.com/cs101x/kicking.html' not in links

def test_crawl_till_max_links():
	links = searchengine.crawler.crawl_till_max_links('http://www.udacity.com/cs101x/index.html',1)
	assert_equal(len(links),1)
	assert 'http://www.udacity.com/cs101x/index.html' in links	
	
	links = searchengine.crawler.crawl_till_max_links('http://www.udacity.com/cs101x/index.html',2)
	assert_equal(len(links),2)
	assert 'http://www.udacity.com/cs101x/index.html' in links	
	assert 'http://www.udacity.com/cs101x/flying.html' in links
	
	links = searchengine.crawler.crawl_till_max_links('http://www.udacity.com/cs101x/index.html',10)
	assert_equal(len(links),5)
	assert 'http://www.udacity.com/cs101x/index.html' in links
	assert 'http://www.udacity.com/cs101x/flying.html' in links
	assert 'http://www.udacity.com/cs101x/walking.html' in links
	assert 'http://www.udacity.com/cs101x/crawling.html' in links
	assert 'http://www.udacity.com/cs101x/kicking.html' in links
	
def test_union():
	target = [1,2,3,4]
	new_link = [1,8,9]
	no_of_links_added = searchengine.crawler.union(target,new_link)
	assert_equal(target, [1,2,3,4,8,9])
	assert_equal(no_of_links_added, 2)
	
	target = []
	new_link = [1,8,9]
	no_of_links_added = searchengine.crawler.union(target,new_link)
	assert_equal(target, [1,8,9])
	assert_equal(no_of_links_added, 3)
	
	target = [1,2,3,4]
	new_link = []
	no_of_links_added = searchengine.crawler.union(target,new_link)
	assert_equal(target, [1,2,3,4])
	assert_equal(no_of_links_added, 0)

def test_crawl_till_max_depth():
	links = searchengine.crawler.crawl_till_max_depth('http://www.udacity.com/cs101x/index.html',10)
	assert_equal(len(links),5)
	assert 'http://www.udacity.com/cs101x/index.html' in links
	assert 'http://www.udacity.com/cs101x/flying.html' in links
	assert 'http://www.udacity.com/cs101x/walking.html' in links
	assert 'http://www.udacity.com/cs101x/crawling.html' in links
	assert 'http://www.udacity.com/cs101x/kicking.html' in links
	
	links = searchengine.crawler.crawl_till_max_depth('http://www.udacity.com/cs101x/index.html',0)
	assert_equal(len(links),0)
	
	links = searchengine.crawler.crawl_till_max_depth('http://www.udacity.com/cs101x/index.html',1)
	assert_equal(len(links),1)
	assert 'http://www.udacity.com/cs101x/index.html' in links
	
	links = searchengine.crawler.crawl_till_max_depth('http://www.udacity.com/cs101x/index.html',2)
	assert_equal(len(links),4)
	assert 'http://www.udacity.com/cs101x/index.html' in links
	assert 'http://www.udacity.com/cs101x/flying.html' in links
	assert 'http://www.udacity.com/cs101x/walking.html' in links
	assert 'http://www.udacity.com/cs101x/crawling.html' in links
	assert 'http://www.udacity.com/cs101x/kicking.html' not in links
