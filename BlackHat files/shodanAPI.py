import shodan, json
def countrycount(api = {}, countries = []):
    dict_count = {}
    for country in countries:
        count = api.count(country)
        dict_count[country] = count["total"]
    print(dict_count)

def UMDsites(api = {}, site = " "):
    for x in api.search_cursor(f'http.title:{site}'):
        print (x)
        
def bannercount(api = {}, banner = " "):
    try:
        bannersearch = api.count(banner)
        print("numver of results found:", bannersearch["total"])
    except Exception as e:
        print("error")
def main(): # makes instance of shodan
    f = open("path", 'r')
    apikey = f.readline().strip()
    f.close

    api =shodan.Shodan(apikey)