from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv
import requests

def calculate_relevance_score(search_input, forename, surname=""):
    name = f"{forename} {surname}"
    return fuzz.token_set_ratio(search_input, name)

def get_country(nationality_input):
    with open("database/nationalities.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            nationality, *country_name = line
            if nationality == nationality_input:
                return country_name[0]
    return None


def get_flag(country_input):
    with open("database/flags.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            *country, flag_url = line
            if country[0] == country_input:
                try:
                    return flag_url
                except ValueError:
                    return ""

def get_image(wiki_page_title):
    if wiki_page_title == "Sochi Autodrom":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Circuit_Sochi.svg/250px-Circuit_Sochi.svg.png"

    elif wiki_page_title == "Buddh International Circuit":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Buddh_Circuit_2.svg/250px-Buddh_Circuit_2.svg.png"

    elif wiki_page_title == "Indianapolis Motor Speedway":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Indianapolis_IndycarGP.svg/180px-Indianapolis_IndycarGP.svg.png"

    elif wiki_page_title == "Brands Hatch":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Brands_Hatch_2003.svg/200px-Brands_Hatch_2003.svg.png"

    elif wiki_page_title == "Bahrain International Circuit":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Bahrain_International_Circuit--Grand_Prix_Layout.svg/250px-Bahrain_International_Circuit--Grand_Prix_Layout.svg.png"

    base_url = 'https://en.wikipedia.org/w/api.php'
    params_search = {
        'action': 'query',
        'format': 'json',
        'generator': 'search',
        'gsrsearch': wiki_page_title,
        'gsrnamespace': 0,
        'gsrlimit': 1,
        'prop': 'pageimages',
        'piprop': 'thumbnail',
    }

    response = requests.get(base_url, params=params_search)
    data = response.json()

    if 'query' in data:
        pages = data['query']['pages']
        for page_id, page_info in pages.items():
            image_info = page_info.get('thumbnail')
            if image_info:
                return image_info['source']

    return None

def get_image_hd(wiki_page_title):
    if wiki_page_title == "Sochi Autodrom":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Circuit_Sochi.svg/250px-Circuit_Sochi.svg.png"

    elif wiki_page_title == "Buddh International Circuit":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Buddh_Circuit_2.svg/250px-Buddh_Circuit_2.svg.png"

    elif wiki_page_title == "Indianapolis Motor Speedway":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Indianapolis_IndycarGP.svg/180px-Indianapolis_IndycarGP.svg.png"

    elif wiki_page_title == "Brands Hatch":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Brands_Hatch_2003.svg/200px-Brands_Hatch_2003.svg.png"

    elif wiki_page_title == "Bahrain International Circuit":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Bahrain_International_Circuit--Grand_Prix_Layout.svg/250px-Bahrain_International_Circuit--Grand_Prix_Layout.svg.png"

    base_url = 'https://en.wikipedia.org/w/api.php'
    params_search = {
        'action': 'query',
        'format': 'json',
        'generator': 'search',
        'gsrsearch': wiki_page_title,
        'gsrnamespace': 0,
        'gsrlimit': 1,
        'prop': 'pageimages',
        'piprop': 'thumbnail',
        'pithumbsize': 80,
    }

    response = requests.get(base_url, params=params_search)
    data = response.json()

    if 'query' in data:
        pages = data['query']['pages']
        for page_id, page_info in pages.items():
            image_info = page_info.get('thumbnail')
            if image_info:
                return image_info['source']

    return None

def get_layout(track):
    with open("database/tracks.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            name,link = line
            if name == track:
                return link

def get_logo(team):
    team_logos = {
        "Mercedes": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Mercedes-Logo.svg/567px-Mercedes-Logo.svg.png",
        "Red Bull": "data:image/png;base64,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",
        "Ferrari": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c0/Scuderia_Ferrari_Logo.svg/80px-Scuderia_Ferrari_Logo.svg.png",
        "Williams": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Logo_Williams_F1.png/300px-Logo_Williams_F1.png",
        "McLaren": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/McLaren_Speedmark.svg/512px-McLaren_Speedmark.svg.png?20210317172444",
        "Renault": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Logo_Renault_F1.png/640px-Logo_Renault_F1.png",
        "Brawn": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Brawn_GP_logo.svg/640px-Brawn_GP_logo.svg.png",
        "Benetton": "https://upload.wikimedia.org/wikipedia/en/thumb/5/54/Benetton_Formula_logo.jpg/210px-Benetton_Formula_logo.jpg",
        "Lotus-Ford": "https://upload.wikimedia.org/wikipedia/commons/9/9e/TeamLotus.jpg",
        "McLaren-Ford": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/McLaren_Speedmark.svg/512px-McLaren_Speedmark.svg.png?20210317172444",
        "Lotus": "https://upload.wikimedia.org/wikipedia/commons/9/9e/TeamLotus.jpg",
        "Tyrrell": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Tyrrell.svg/220px-Tyrrell.svg.png",
        "Matra-Ford": "https://upload.wikimedia.org/wikipedia/en/4/4b/Matra_Sports.gif",
        "Brabham-Repco": "https://upload.wikimedia.org/wikipedia/en/5/53/Brabham91.png",
        "Lotus-Climax": "https://upload.wikimedia.org/wikipedia/commons/9/9e/TeamLotus.jpg",
        "BRM": "https://upload.wikimedia.org/wikipedia/en/b/bd/BritishRacingMotorsLogo.png",
        "Cooper-Climax": "https://upload.wikimedia.org/wikipedia/en/4/47/Cooper_Car_Company.png",
        "Vanwall": "https://upload.wikimedia.org/wikipedia/en/5/58/Vanwall_logo.jpg",
        "NULL": "",
    }

    return team_logos[team]

def capitalize(sentence):
    words = sentence.split()
    return " ".join(word.capitalize() for word in words)