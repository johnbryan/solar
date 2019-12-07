from datetime import datetime, timezone
import json
import math
import os
import urllib.request

# API docs
# https://www.solaredge.com/sites/default/files/se_monitoring_api.pdf
def get_current_generation(request):
  siteId = '1344511'
  apiKey = 'FZ9I7JU457CVMJ3Y8VASQQ8F6ZHZU23S'  #os.environ.get('SOLAR_API_KEY')
  apiKeyParam = 'api_key='+apiKey

  baseUrl = 'https://monitoringapi.solaredge.com/site/' + siteId
  overviewUrl = baseUrl + '/overview?' + apiKeyParam
  # detailsUrl = baseUrl + '/details?' + apiKeyParam
  # energyUrl = baseUrl + '/energy?timeUnit=DAY&startDate=2019-11-28&endDate=2019-12-10&' + apiKeyParam
  # powerUrl = baseUrl + '/power?startTime=2013-05-5%2011:00:00&endTime=2013-05-05%2013:00:00&' + apiKeyParam

  response = urllib.request.urlopen(overviewUrl).read()
  resp = json.loads(response)
  overviewData = resp['overview']
  currentPower = overviewData['currentPower']['power']
  lifeTimeEnergy = overviewData['lifeTimeData']['energy']

  reply = 'Currently ' + str(currentPower) + ' watts. Total ' + str(lifeTimeEnergy)
  replyObj = {"fulfillmentText": reply}
  return str(replyObj)

print(get_current_generation(""))

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
