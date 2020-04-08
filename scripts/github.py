#!/usr/local/bin/python3

from requests import get
from datetime import date, datetime
from bs4 import BeautifulSoup as bs


def main():
    link = "https://github.com/alexanderluna"
    parsed_html = bs(get(link).content, 'html.parser')
    calender = get_calender(parsed_html)
    days_without_commit = get_inactive_days(calender)
    print_info_message(days_without_commit)
    print_dates(days_without_commit)


def get_calender(html):
    dates = html.findAll('rect')
    return dates


def get_inactive_days(days):
    inactive_days = [
        day['data-date']
        for day in days
        if int(day['data-count']) < 1
    ]
    return inactive_days


def print_info_message(days):
    last_commit = datetime.strptime(days[0], '%Y-%m-%d')
    days_since_commit = date.today() - last_commit.date()
    print(f'Last uncommited date: {days[0]} ({days_since_commit.days} days)')
    print(f'Dates missing commits: {len(days)}')


def print_dates(days):
    for index, day in enumerate(days):
        if not (index % 5):
            print()
        print(day, end='\t')
    print()


if __name__ == "__main__":
    main()
