from nytimesarticle import articleAPI
api = articleAPI('f35b4af2b1754dbe923584c54daed682')

articles = api.search(q = 'Ben Carson',
               fq = {'headline':'Ben Carson', 'source':['The New York Times']},
               begin_date = 20170101,
               end_date = 20180101,
               sort='oldest'
               )

def parse_articles(articles):
    '''
    This function takes in a response to the NYT api and parses
    the articles into a list of dictionaries
    '''
    news = []
    for i in articles['response']['docs']:
        dic = {}
        dic['id'] = i['_id']
        if i['abstract'] is not None:
            dic['abstract'] = i['abstract'].encode("utf8")
        dic['headline'] = i['headline']['main'].encode("utf8")
        dic['desk'] = i['news_desk']
        dic['date'] = i['pub_date'][0:10] # cutting time of day.
        dic['section'] = i['section_name']
        if i['snippet'] is not None:
            dic['snippet'] = i['snippet'].encode("utf8")
        dic['source'] = i['source']
        dic['type'] = i['type_of_material']
        dic['url'] = i['web_url']
        dic['word_count'] = i['word_count']
        # locations
        locations = []
        for x in range(0,len(i['keywords'])):
            if 'glocations' in i['keywords'][x]['name']:
                locations.append(i['keywords'][x]['value'])
        dic['locations'] = locations
        # subject
        subjects = []
        for x in range(0,len(i['keywords'])):
            if 'subject' in i['keywords'][x]['name']:
                subjects.append(i['keywords'][x]['value'])
        dic['subjects'] = subjects   
        news.app
        end(dic)
    return(news)

def get_articles(query):
    '''
    This function accepts a year in string format (e.g.'1980')
    and a query (e.g.'Amnesty International') and it will 
    return a list of parsed articles (in dictionaries)
    for that year.
    '''
    all_articles = []
    for i in range(0,100): #NYT limits pager to first 100 pages. But rarely will you find over 100 pages of results anyway.
        articles = api.search(q = query,
               fq = {'headline.search':[query], 'source':['The New York Times']},
               begin_date = '20141031',
               end_date = '20151031',
               sort='newest',
               page = str(i))
        articles = parse_articles(articles)
        all_articles = all_articles + articles
    return(all_articles)


Bernie_Sanders =  get_articles('Bernie Sanders')
Bernie_Sanders_df = pd.DataFrame(Bernie_Sanders)
Bernie_Sanders_df.head()