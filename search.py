import sys
import requests

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://oagq.qc.ca',
    'Referer': 'https://oagq.qc.ca/trouver-un-arpenteur-geometre/?servicestypes=Hydrographie%20/%20Bathym%C3%A9trie&ord=random',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

data = {
    'action': 'members_directory_search_ajax',
    'filters[fullName]': '',
    'filters[registrationNumber]': '',
    'filters[location]': '',
    'filters[position]': '',
    'filters[distanceRadius]': '',
    'filters[services][label]': 'Hydrographie / Bathymétrie',
    'filters[services][value]': 'Hydrographie / Bathymétrie',
    'filters[customers]': '',
    'filters[isFirmEmployee]': '0',
    'filters[isPublicEmployee]': '0',
    'filters[paged]': '1',
    'filters[orderBy]': 'random',
}

r = requests.post("https://oagq.qc.ca/wp-admin/admin-ajax.php",headers=headers,data=data)

if r.status_code == 200:
	jsonData = r.json()

	print("Nom|Titre|Lien|Firme|Addresse|Latitude|Longitude|Courriel|Telephone|Extension|Fax")

	for item in jsonData['items']:
		print(f"{item['full_name']}|{item['title']}|{item['link']}|{item['firm']}|{item['address']}|{item['lat']}|{item['lng']}|{item['email']}|{item['phone']}|{item['phone_ext']}|{item['fax']}")
else:
	sys.stderr.write(f"Erreur lors de la recherche: {r.status_code}")
