import requests

# Configuration
API_BASE = "https://api.jolpi.ca/ergast/f1/current"


def fetch_next_gp():
    """Retrieves information about the next Grand Prix.

    Returns:
        str: Formatted Grand Prix details, or None in case of an error.
    """
    try:
        response = requests.get(f"{API_BASE}/next.json")
        response.raise_for_status()
        data = response.json()
        race = data['MRData']['RaceTable']['Races'][0]

        message = (
            f"🏁 **{race['raceName']}** - {race['Circuit']['circuitName']}\n"
            f"📅 Date : {race['date']} à {race['time'][:5]} (Heure locale)"
        )
        return message

    except requests.RequestException as error:
        print(f"Erreur API Next GP: {error}")
        return None


def fetch_last_race_data():
    """Retrieves the results and DNFs of the last race.

    Returns:
        tuple: (top_10_course, dnf_count, dnf_names) or
               (None, None, None) if an error occurs.
    """
    try:
        response = requests.get(f"{API_BASE}/last/results.json")
        response.raise_for_status()
        data = response.json()['MRData']['RaceTable']['Races'][0]['Results']

        top_10_course = [
            driver['Driver']['familyName'].capitalize() for driver in data[:10]
        ]

        # Retrieves drivers who did not finish the race
        dnf_names = [
            driver['Driver']['familyName'].capitalize()
            for driver in data
            if driver['status'] not in ['Finished']
               and not driver['status'].startswith('+')
        ]

        return top_10_course, len(dnf_names), dnf_names

    except requests.RequestException as error:
        print(f"Erreur API Race: {error}")
        return None, None, None


def fetch_last_quali_data():
    """Retrieves the Top 3 of the last qualifications.

    Returns:
        list: The names of the first 3 drivers, or None in case of an error.
    """
    try:
        response = requests.get(f"{API_BASE}/last/qualifying.json")
        response.raise_for_status()
        data = response.json()
        races = data['MRData']['RaceTable']['Races'][0]
        quali_results = races['QualifyingResults']

        top_3_quali = [
            driver['Driver']['familyName'].capitalize()
            for driver in quali_results[:3]
        ]
        return top_3_quali

    except requests.RequestException as error:
        print(f"Erreur API Quali: {error}")
        return None