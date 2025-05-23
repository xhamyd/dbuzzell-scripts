from datetime import datetime
from pathlib import Path
import os
import re
from typing import Optional

from dotenv import load_dotenv
from openpyxl import load_workbook
import requests
import yaml

# Load environmental variables from ".env"
load_dotenv()

GEOCODIO_API_KEY = os.environ["GEOCODIO_API_KEY"]
LEGISLATORS_YAML_URL = "https://unitedstates.github.io/congress-legislators/legislators-current.yaml"
COORDINATES_XLSX = Path(f"./{os.environ['COORDINATES_XLSX']}")
OUTPUT_FILE = Path("./legislators_from_latlon.txt")
LAT_LON_REGEX = r'^(?P<lat>[\d\.-]+)\u00B0?,\s*(?P<lon>[\d\.-]+)\u00B0?$'


def get_coordinates():
    workbook = load_workbook(COORDINATES_XLSX)
    sheet = workbook.active
    if sheet is None:
        raise RuntimeError(f"Failed to load worksheet {COORDINATES_XLSX}")

    data = [row for row in sheet.iter_rows(min_row=2, max_row=None, min_col=2, max_col=4, values_only=True)]
    assert data[0] == ('Project Number', 'PROJECT NAME', 'Geo Coordinates')  # assuming a fixed format for now
    assert data[1] == (None, 'TOTAL', '-')  # extra info that we don't need

    return [[row_i] + list(row[1:]) for row_i, row in enumerate(data[2:], start=1)]


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
    # output_text.append(f"{url}?{params_str}")

    response = requests.get(url, params=params)
    data = response.json()
    if response.status_code != 200:
        return f"Error {response.status_code}: {data['error']}"

    results = data['results'][0]
    state = results['address_components']['state']
    country = results['address_components']['country']
    if country == "CA":
        # Skip canadian addresses
        district = congress = None
    else:
        cd_info = results['fields']['congressional_districts'][0]
        district = cd_info['district_number']
        congress = cd_info['congress_number']
    
    return dict(state=state,
                country=country,
                district=district,
                congress=congress)


def ordinal(n: Optional[int]):
    # Source: https://codegolf.stackexchange.com/questions/4707/outputting-ordinal-numbers-1st-2nd-3rd#answer-4712
    if n is None:
        return "#N/A"
    else:
        return "%d%s" % (n, "tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])


def main():
    print("Getting legislators...")
    legislators = get_legislators_yaml()
    print("Loading coordinates...")
    coordinates = get_coordinates()
    print("Done!\n")

    output_text = list()
    for proj_num, proj_name, lat_lon in coordinates:
        if int(proj_num) > 245:
            # Reached end of list
            break

        output_text.append(f"{proj_num}: {proj_name}")
        if lat_lon is None:
            output_text.append("*** No coordinates provided!\n")
            continue

        if (lat_lon_match := re.match(LAT_LON_REGEX, lat_lon)):
            lat = float(lat_lon_match.group("lat"))
            lon = float(lat_lon_match.group("lon"))
        else:
            breakpoint()

        district_info = get_district(lat, lon)
        # output_text.append(f"({lat:.6f}, {lon:.6f}): {ordinal(district_info['district'])} congressional district of {district_info['state']}")
        if isinstance(district_info, str):
            # Error message popped up, quit and debug manually
            output_text.append(district_info)
            break
        elif district_info["country"] == "CA":
            output_text.append("*** Found Canadian address, skipping congressional district!\n")
        else:
            key = f"{district_info['state']}-{district_info['district']}"
            rep = legislators.get(key)
            if rep:
                output_text.append(f"Coordinates: {lat}, {lon}")
                output_text.append(f"District: {district_info['state']}-{district_info['district']}")
                output_text.append(f"Representative: {rep['first_name']} {rep['last_name']} ({rep['party']})\n")
            else:
                output_text.append(f"No representative found for {lat}, {lon}\n")
        
        for line in output_text:
            print(line)
        with OUTPUT_FILE.open(mode='a') as out_f:
            out_f.writelines(f"{line}\n" for line in output_text)
        output_text = []


if __name__ == "__main__":
    main()
