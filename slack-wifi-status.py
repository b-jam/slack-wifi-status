#!/usr/local/bin/python3

from datetime import datetime, date, time
import subprocess
from urllib import parse, request
import os

END_OF_DAY_HOUR = 18
START_OF_DAY_HOUR = 7
SLACK_TOKEN = ""

LOCATION_CONFIG = {
    "DEFAULT": {"status_text": "Working remotely", "status_emoji": ":house_with_garden:"},
    "CSGUEST": {"status_text": "At Customs", "status_emoji": ":customsnz:"},
    "ssn": {"status_text": "At Customs", "status_emoji": ":pride-sprout:"},
}


def get_wifi_ssid():
    process = subprocess.Popen(
        ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'],
        stdout=subprocess.PIPE
    )
    out, err = process.communicate()
    process.wait()

    # Get the line with SSID:, and then cut that part out to just get the SSID
    match = [line.strip() for line in out.split(b'\n') if b' SSID' in line][0]
    return match.partition(b'SSID: ')[2].decode("utf-8")


def get_matching_key(ssn_substring):
    try:
        return next(value for key, value in LOCATION_CONFIG.items() if ssn_substring.lower() in key.lower())
    except StopIteration:
        print(f"No config for {ssn_substring}, matching with default config")
        return LOCATION_CONFIG['DEFAULT']


def main():
    current_time = datetime.now()
    end_of_day = datetime.combine(
        date.today(),
        time(END_OF_DAY_HOUR))
    end_of_day_epoch = end_of_day.strftime('%s')

    start_of_day = datetime.combine(
        date.today(),
        time(START_OF_DAY_HOUR))

    if current_time > end_of_day or current_time < start_of_day:
        exit(0)

    wifi_ssid = get_wifi_ssid()
    print(f"Found wifi with ID {wifi_ssid}")

    matching_config = get_matching_key(wifi_ssid)
    matching_config['status_expiration'] = end_of_day_epoch
    params = parse.urlencode({"token": SLACK_TOKEN or os.environ["SLACK_TOKEN"], "profile": matching_config})
    req = request.Request("https://slack.com/api/users.profile.set", params.encode('ascii'), {})

    response = request.urlopen(req)


if __name__ == "__main__":
    main()
