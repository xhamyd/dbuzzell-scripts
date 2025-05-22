import requests
import yaml
from datetime import datetime

GEOCODIO_API_KEY = None
LEGISLATORS_YAML_URL = "https://unitedstates.github.io/congress-legislators/legislators-current.yaml"

coordinates = [
    (36.082382, -83.331902),
    (35.882048, -84.666805),
    (35.387548, -86.265530),
    (35.957485, -83.172971),
    (35.598233, -84.534972)
]


def is_current_term(term):
    """Return True if the term is current (end date in future or missing)."""
    end_date = term.get('end')
    if end_date is None:
        return True

    end_dt = datetime.strptime(end_date, '%Y-%m-%d')
    return end_dt > datetime.now()


def get_legislators_yaml():
    """Fetch and parse the YAML legislators file, returning current House members."""
    response = requests.get(LEGISLATORS_YAML_URL)
    response.raise_for_status()
    data = yaml.safe_load(response.text)

    legislators = dict()
    for leg in data:
        terms = leg.get('terms', [])
        rep_terms = [t for t in terms if t.get('type') == 'rep' and is_current_term(t)]
        if rep_terms:
            # Use the latest current term
            term = sorted(rep_terms, key=lambda t: t.get('start', ''), reverse=True)[0]
            state = term.get('state')
            district = str(term.get('district'))
            key = f"{state}-{district}"
            legislators[key] = {
                'first_name': leg.get('name', {}).get('first', ''),
                'last_name': leg.get('name', {}).get('last', ''),
                'party': term.get('party', '')
            }
    return legislators


def get_district(lat, lon):
    """Get congressional district using Geocodio"""
    url = "https://api.geocod.io/v1.8/reverse"
    params = {
        'q': f"{lat},{lon}",
        'api_key': GEOCODIO_API_KEY,
        'fields': 'cd'
    }

    # params_str = "&".join(list(f"{k}={v}" for k, v in params.items()))
    # print(f"{url}?{params_str}")

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return f"Error: {response.status_code}"

    data = response.json()
    cd_info = data['results'][0]['fields']['congressional_districts'][0]
    return {
        'state': data['results'][0]['address_components']['state'],
        'district': cd_info['district_number'],
        'congress': cd_info['congress_number']
    }

def ordinal(n: int):
    # Source: https://codegolf.stackexchange.com/questions/4707/outputting-ordinal-numbers-1st-2nd-3rd#answer-4712
    return "%d%s" % (n, "tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

def main():
    legislators = get_legislators_yaml()
    
    for lat, lon in coordinates:
        district_info = get_district(lat, lon)
        # print(f"({lat:.6f}, {lon:.6f}): {ordinal(district_info['district'])} congressional district of {district_info['state']}")

        if isinstance(district_info, dict):
            key = f"{district_info['state']}-{district_info['district']}"
            rep = legislators.get(key)
            if rep:
                print(f"Coordinates: {lat}, {lon}")
                print(f"District: {district_info['state']}-{district_info['district']}")
                print(f"Representative: {rep['first_name']} {rep['last_name']} ({rep['party']})\n")
            else:
                print(f"No representative found for {lat}, {lon}")
        else:
            print(district_info)

if __name__ == "__main__":
    main()
