import json
import requests

from requests.auth import HTTPBasicAuth

host = 'https://app.mode.com'
ws = 'cohire'
un = '6c935be7859d'
pw = 'd021afe559303cf52c2851d0'

def get_all_reports_tokens():
  url = '%s/api/%s/spaces?filter=all' % (host, ws)
  r = requests.get(url, auth=HTTPBasicAuth(un, pw))
  result = r.json()
  spaces = result['_embedded']['spaces']
  space_tokens = [s['token'] for s in spaces]
  all_tokens = []
  for s in space_tokens:
    page = 1
    report_tokens = make_request(s, page)
    all_tokens += report_tokens
    while(len(report_tokens)==30):
      page += 1
      report_tokens = make_request(s, page)
      all_tokens += report_tokens

  return all_tokens


def make_request(space_token, page):
  url = '%s/api/%s/spaces/%s/reports?page=%d' % (host, ws, space_token, page)
  r = requests.get(url, auth=HTTPBasicAuth(un, pw))
  results = r.json()
  reports = results['_embedded']['reports']
  print(reports)
  report_tokens = [r['token'] for r in reports]
  return report_tokens


print(get_all_reports_tokens())
