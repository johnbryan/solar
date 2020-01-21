import os
import requests
from flask import Flask
import datetime

app = Flask(__name__)

# Dialogflow invokes with POST
@app.route('/',  methods=['GET', 'POST'])
def index():
  return get_current_generation()

# API docs
# https://www.solaredge.com/sites/default/files/se_monitoring_api.pdf
def get_current_generation(request=''):
  # Environment variables set in the Cloud Run config.
  siteId = os.environ.get('SITE_ID')
  apiKey = os.environ.get('SOLAR_API_KEY')

  apiKeyParam = 'api_key='+apiKey
  baseUrl = 'https://monitoringapi.solaredge.com/site/' + siteId
  overviewUrl = baseUrl + '/overview?' + apiKeyParam

  resp = requests.get(overviewUrl).json()
  overviewData = resp['overview']
  currentKw = round(overviewData['currentPower']['power'] / 1000, 1)
  lastDayKwh = round(overviewData['lastDayData']['energy'] / 1000)
  lifeTimeKwh = round(overviewData['lifeTimeData']['energy'] / 1000)

  now = datetime.datetime.now()
  prefix = 'So far today, '
  if now.hour >= 16 and currentPower == 0:
    prefix = 'Today was '

  reply = prefix + str(lastDayKwh) + ' kilowatt-hours.'

  # Format the reply in the way Google Assistant needs it.
  replyObj = {'fulfillmentText': reply}
  return str(replyObj)

if __name__ == '__main__':
  # copied from https://cloud.google.com/run/docs/quickstarts/build-and-deploy:
  app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))

#print(get_current_generation())
