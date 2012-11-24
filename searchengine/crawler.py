import os.path

def get_next_link(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	
	start_quote = page.find('"',start_link)
	end_quote = page.find('"',start_quote + 1)
	url = page[start_quote + 1: end_quote]
	return url,end_quote

def get_all_links(page):
	links = []
	while True:
		url, end_quote = get_next_link(page)
		if(url == None):
			break
		links.append(url)
		page = page[end_quote :]

	return links

def get_page(url):
	filename = url.split('/').pop()
	dir = 'tests/private_web'
	path = os.path.join(os.path.curdir, dir,filename)
	test_sample_page = open(path)
	page = test_sample_page.read()
	test_sample_page.close()
	return page

# Temporarily, get_page is suppose to return the pages from file system. This will be replace by proper url fetching later.
def test_get_page():
	print searchengine.crawler.get_page('testSample.html')
	print ('===============')
	print searchengine.crawler.get_page('flying.html')
	print ('===============')
	print searchengine.crawler.get_page('index.html')
	print ('===============')
	print searchengine.crawler.get_page('walking.html')
	print ('===============')
	
def crawl(seed):
	toCrawl = [seed]
	crawled = []
		
	while toCrawl:
		temp = toCrawl.pop()
				
		if temp not in crawled:
			page = get_page(temp)
			toCrawl.extend(get_all_links(page))
			crawled.append(temp)
				
	return crawled

def crawl_till_max_links(seed, max_links):
	page = get_page(seed)
	toCrawl = get_all_links(page)
	max_links = max_links - 1
	crawled = [seed]
		
	while toCrawl:
		temp = toCrawl.pop()
				
		if max_links > 0 and temp not in crawled:
			page = get_page(temp)
			toCrawl.extend(get_all_links(page))
			crawled.append(temp)
			max_links = max_links - 1
			
	return crawled

def crawl_till_max_depth(seed, max_depth):
	next_depth = [seed]
	crawled = []
	to_crawl = []
	
	while max_depth > 0 and next_depth:
		to_crawl = next_depth
		next_depth = []
		max_depth = max_depth - 1
		
		while to_crawl:
			temp = to_crawl.pop()
			
			if temp not in crawled:
				page = get_page(temp)
				union(next_depth,get_all_links(page))
				crawled.append(temp)
		
	return crawled	
		
			
			
			
			

def union(target, new_links):
	no_of_items_added = 0
	for link in new_links:
		if link not in target:
			target.append(link)
			no_of_items_added = no_of_items_added + 1
	
	return no_of_items_added