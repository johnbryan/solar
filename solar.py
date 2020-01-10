import os
import requests
from flask import Flask

app = Flask(__name__)

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
  # detailsUrl = baseUrl + '/details?' + apiKeyParam
  # energyUrl = baseUrl + '/energy?timeUnit=DAY&startDate=2019-11-28&endDate=2019-12-10&' + apiKeyParam
  # powerUrl = baseUrl + '/power?startTime=2013-05-5%2011:00:00&endTime=2013-05-05%2013:00:00&' + apiKeyParam

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

# {
#   "overview": {
#     "lastUpdateTime":"2013-10-01 02:37:47",
#     "lifeTimeData":{
#       "energy":761985.75,
#       "revenue":946.13104
#     },
#     "lastYearData":{
#       "energy":761985.8,
#       "revenue":0.0
#     },
#     "lastMonthData":{
#       "energy":492736.7,
#       "revenue":0.0
#     },
#     "lastDayData":{
#       "energy":0.0,
#       "revenue":0.0
#     },
#     "currentPower":{
#       "power":0.0
#     }
#   }
# }
