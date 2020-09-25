from bs4 import BeautifulSoup
import requests


def flipkart(product_name):
        url = "https://www.flipkart.com/"
        query = "search?q=" + product_name
        url = url + query
        price_min = 1000000000
        site = 'Flipkart'

        result = requests.get(url)
        soup = BeautifulSoup(result.content, 'html.parser')

        flipkart_details = []

        if soup.find_all(class_='_31qSD5'):
            for i,mob in enumerate(soup.find_all(class_ = '_31qSD5')):
                try:
                    name = mob.find(class_ = '_3wU53n').text.strip()
                    price = mob.find(class_ = '_1vC4OE _2rQ-NK').text.strip()
                    l = int(price.replace(',','')[1:])
                    # try:
                    #     # img_det = re.findall("keySpecs(.*?)jpeg", result.text)[i]
                    #     # details = re.findall("\[\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\".*url\":\"(.*)", img_det)[0]
                    #     url = details[5]
                    #     url = re.sub("{@width}|{@height}", '250', url) + 'jpeg'
                    # except:
                    #     url = ''
                    try:
                        prod_url = mob.attrs['href']
                        prod_url = "https://www.flipkart.com" + prod_url
                    except:
                        prod_url = ''
                    # try:
                    #     rating = mob.find('div', class_ = 'hGSR34 _2beYZw').text.strip()
                    # except:
                    #     rating = ''
                    # try:
                    #     no_of_ratings = re.findall('(.*)Ratings',mob.find_all('span', class_ = '_38sUEc')[0].text)[0].strip()
                    # except:
                    #     no_of_ratings = ''
                        #no_of_reviews = re.findall('\xa0&\xa0(.*)Reviews',mob.find_all('span', class_ = '_38sUEc')[0].text)[0].strip()
                    # flipkart_details.append([name, price, rating, no_of_ratings, site, url, prod_url])
#                    print(site, name, price, url, prod_url)
                    if price_min > l:
                        price_min = l
                        k = i-1
                    flipkart_details.append([name,price,'','','','',prod_url,{'min':False}])
                except:
                    pass


        else:
            for i,mob in enumerate(soup.find_all('div', class_='_3liAhj _1R0K0g')):
                if i == 5:  break
                try:
                    name = mob.find(class_ = '_2cLu-l').text.strip()
                    price = mob.find(class_ = '_1vC4OE').text.strip()
                    l = int(price.replace(',','')[1:])
                    # try:
                    #     img_det = re.findall("keySpecs(.*?)jpeg", result.text)[i]
                    #     details = re.findall("\[\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\".*url\":\"(.*)", img_det)[0]
                    #     url = details[5]
                    #     url = re.sub("{@width}|{@height}", '250', url) + 'jpeg'
                    # except:
                    #     url = ''
                    try:
                        prod_url = mob.find(class_ = 'Zhf2z-')
                        prod_url = prod_url.attrs['href']
                        prod_url = "https://www.flipkart.com" + prod_url
                    except:
                        prod_url = ''
                    # try:
                    #     rating = mob.find(class_ = 'hGSR34 _2beYZw').text.strip()
                    # except:
                    #     rating = ''
                    # try:
                    #     no_of_ratings = mob.find(class_ = '_38sUEc').text.strip('()')
                    # except:
                    #     no_of_ratings = ''
                    if price_min > l:
                        price_min = l
                        k = i-1
                    flipkart_details.append([name,price,'','','','',prod_url,{'min':False}])
#                    print(site, name, price, url, prod_url)
                except:
                    pass


        if len(flipkart_details) == 0:
            # soup.find_all(class_='_3O0U0u')
            for i , pro in enumerate(soup.find_all(class_='_3O0U0u')):
                if i == 5:  break
                price = pro.find(class_='_1vC4OE').text.strip()
                l = int(price.replace(',','')[1:])
                try:
                    name = pro.find(class_='_2cLu-l').text.strip()
                except:
                    name = pro.find(class_='_2mylT6').text.strip()
                try:
                    prod_url = pro.find(class_='_2mylT6')
                    prod_url = prod_url.attrs['href']
                    prod_url = "https://www.flipkart.com" + prod_url
                except:
                    prod_url = pro.find(class_='_2cLu-l')
                    prod_url = prod_url.attrs['href']
                    prod_url = "https://www.flipkart.com" + prod_url
                # print(prod_url,end='\n\n\n')

                if price_min > l:
                    price_min = l
                    k = i-1
                flipkart_details.append([name,price,'','','','',prod_url,{'min':False}])

        flipkart_details=flipkart_details[:4]
        flipkart_details[k][7]['min'] = True
        # print(flipkart_details)
        return flipkart_details

def amazon(product_name):
#         url = "https://www.amazon.in/"

        site = 'Amazon'

        url = "https://www.amazon.in/"
        query = "s?k=" + product_name
        url = url + query

        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        r = requests.get(url, headers = header)

        driver = BeautifulSoup(r.content,"html5lib")

        amazon_details = []
        price_min = 100000000

        if driver.find_all(class_='s-main-slot'):
            for i,mob in enumerate(driver.find_all(class_='s-result-item')):
                if i == 5:  break
                if not mob.find(class_='a-price-whole') is None:
                    price = mob.find(class_='a-price-whole').text.strip()
                    l = int(price.replace(',',''))
                    try:
                        name = mob.find(class_="a-size-medium a-color-base a-text-normal").text.strip()
                    except:
                        try:
                            name = mob.find(class_="a-size-base-plus").text.strip()
                        except:
                            name = mob.find(class_="a-text-normal").text.strip()
                    prod_url = mob.find(class_='a-link-normal')
                    prod_url = prod_url.attrs['href']
                    prod_url = "https://www.amazon.in" + prod_url
#                    print(name,price,"link = ",prod_url)

                    if price_min > int(l):
                        price_min = int(l)
                        k = i-1
                    amazon_details.append([name,price,'','',prod_url,{'min':False}])
        amazon_details[k][5]['min'] = True
        # print(amazon_details)
        return amazon_details



