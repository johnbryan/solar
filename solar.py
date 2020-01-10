import os
import requests
from flask import Flask

app = Flask(__name__)

# Dialogflow invokes with POST
@app.route('/',  methods=['GET', 'POST'])
def index():
  return get_current_generation()

# API docs
# https://www.solaredge.com/sites/default/files/se_monitoring_api.pdf
def get_current_generation(request=''):
  siteId = '1344511'
  apiKey = 'FZ9I7JU457CVMJ3Y8VASQQ8F6ZHZU23S'  #os.environ.get('SOLAR_API_KEY')
  apiKeyParam = 'api_key='+apiKey

  baseUrl = 'https://monitoringapi.solaredge.com/site/' + siteId
  overviewUrl = baseUrl + '/overview?' + apiKeyParam

  resp = requests.get(overviewUrl).json()
  overviewData = resp['overview']
  currentPower = overviewData['currentPower']['power']
  lastDayKwh = overviewData['lastDayData']['energy'] / 1000
  lifeTimeKwh = overviewData['lifeTimeData']['energy'] / 1000

  reply = ('Currently ' + str(currentPower) + ' watts. '
          'Today was ' + str(lastDayKwh) + ' kilowatt-hours. '
          'Lifetime total ' + str(lifeTimeKwh) + ' kilowatt-hours.')
  replyObj = {'fulfillmentText': reply}
  return str(replyObj)

if __name__ == '__main__':
  # copied from https://cloud.google.com/run/docs/quickstarts/build-and-deploy:
  app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))

#print(get_current_generation())
