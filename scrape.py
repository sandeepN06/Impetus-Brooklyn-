from bs4 import BeautifulSoup
import requests
  


web_links = {
                'url_1' : 'https://web-geeks.herokuapp.com/',
                'url_2' : 'https://web-geeks.herokuapp.com/sonnet1.html',
                'url_3' : 'https://web-geeks.herokuapp.com/sonnet2.html',
                'url_4' : 'https://web-geeks.herokuapp.com/sonnet3.html',
                'url_5' : 'https://web-geeks.herokuapp.com/web4.html',
                'url_6' : 'https://web-geeks.herokuapp.com/web5.html'
            }
    
    
f = open('hints.txt','w')    

for url_key in web_links:

    URL = web_links[url_key]

    hint_keywords = set()

    page = requests.get( URL )
        
    soup = BeautifulSoup( page.content , 'html.parser')

        
    tags = {tag.name for tag in soup.find_all()}

        
    
          

    for tag in tags:
            
        for i in soup.find_all( tag ):

            if i.has_attr( "class" ):
            
                if len( i['class'] ) != 0:
                    hint_keywords.add(" ".join( i['class']))         
            
            
      

    s = str(hint_keywords)
    f.write(s + "\n")
    # print(s)

    

    


