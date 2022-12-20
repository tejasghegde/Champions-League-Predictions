import requests
from bs4 import BeautifulSoup
import string
import pandas as pd 


def team_stats():
    """returns a pandas data frame of players' basic info from the website
    whoscored.com. The players all started playing after 2000.
    """
    players = []
    group_length = 8
    base_url = 'https://www.whoscored.com/Regions/250/Tournaments/12/Seasons/'
    year_codes = [9086, 8623, 8177, 7804, 7352, 6842, 6349, 
                    5848, 4333, 3872, 3416, 2944, 2474, 1868]
    
    stages_list = [20961, 
                    20088, 
                    18972, 
                    17937,
                    16652,
                    15482,
                    14167,
                    12857,
                    11505,
                    8150,
                    6849,
                    5748,
                    4753,
                    3333]
    for i in year_codes:
        # insert code to loop through list + 'Stages/'
        new_url = base_url
        new_url += str(i) + "/Stages/"
        # 2022/2023: 20961 (for group A, add 1 for each group, 8 groups)
        for j in stages_list:
            for k in range(group_length):
                url = new_url
                url += str(j + k) + "/TeamStatistics"
                print(url)
        
                page_request = requests.get(url)
                soup = BeautifulSoup(page_request.text,"lxml")
                summary = soup.find("table", {"class": "grid"})
            # print(soup)
    #     if table:
    #         table_body = table.find('tbody')
    #         for row in table_body.findAll('tr'):
    #             player_url = row.find('a')
    #             player_names = player_url.text
    #             player_pages = player_url['href']
    #             cells = row.findAll('td') # all data for all players uniform across database
    #             # print(cells)
    #             active_from = int(cells[0].text)
    #             active_to = int(cells[1].text)
    #             position = cells[2].text
    #             height = cells[3].text
    #             weight = cells[4].text
    #             birth_date = cells[5].text
    #             college = cells[6].text    
    #             player_entry = {'url': player_pages,
    #                             'name': player_names,
    #                             'active_from': active_from,
    #                             'active_to': active_to,
    #                             'position': position,
    #                             'college': college,
    #                             'height': height,
    #                             'weight': weight,
    #                             'birth_date': birth_date}
    #             if int(active_from) > 1989:
    #                 players.append(player_entry)
    # return pd.DataFrame(players)

def attempt():
    url = "https://fr.whoscored.com/Regions/250/Tournaments/12/Seasons/9086/Stages/20961/TeamStatistics/Europe-Champions-League-2022-2023"
    # proxy = {
    # 'http': "indianajones09%40live.de:muck09HA@au796.nordvpn.com",
    # 'https': "indianajones09%40live.de:muck09HA@au796.nordvpn.com"
    # }
    # page_request = requests.get(url, proxies=proxy)
    page_request = requests.get(url)

    soup = BeautifulSoup(page_request.text,"lxml")
    print(soup)
    summary = soup.find("tbody", {"id": "top-team-stats-summary-content"})
    print(summary)

def main():
    attempt()

if __name__=="__main__":
    main()



    
