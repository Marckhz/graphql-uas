import requests
import pprint


from django.core.management.base import BaseCommand

from commerce.models  import Shop 

from django.db import transaction



def build_request(**kwargs):
    UNSPLASH_ENDPOINT = 'https://api.unsplash.com/'
    k =  {**kwargs}   
    req = requests.get(f'{UNSPLASH_ENDPOINT}/search/photos?client_id=uWSMSoPYS9cvf2Kv0FgGmWfy1Szc6TfaiKTsrPwNNfo&query={k["category"]}&orientation={k["orientation"]}&page={k["page"]}')
    
    return req.json()['results']


def get_restaurants_profile_photo(**kwargs):
    urls_counter = 0
    page = 1
    urls=[]
    k = {**kwargs}
    while len(urls) <100:
        data = build_request(category=k['category'], orientation=k['orientation'], page=k['page'])
        for result in data:
            if len(data) < 100:
                urls+=  [result['urls']['full']]
        page+=1
    return urls



class Command(BaseCommand):


    def add_arguments(self, parser):
        parser.add_argument('category',  type=str )
        parser.add_argument('orientation', type=str)
        parser.add_argument('page', type=int)

    def handle(self, *args, **kwargs):

        print("Starting Script...\n")
        print("Quering Database...")
        shop_objs = Shop.objects.all()

        print("Objects gathered..\n")
        print(f'Fetching Images urls from UNSPLASH...{len(shop_objs)} \n')
        
        restaurant_urls = get_restaurants_profile_photo(category=kwargs['category'],
                                                        orientation=kwargs['orientation'], 
                                                        page=kwargs['page']
                                                        )
        print("URls fetched \n", len(restaurant_urls))
        print("Staring update...\n")
        with transaction.atomic():
            print("updating..")
            for obj, img in  zip(shop_objs, restaurant_urls):
                obj.image = img
                obj.save()
        print("Finished")