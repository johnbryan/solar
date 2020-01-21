Solar stuff to ask the Google Home about current production

API docs
https://www.solaredge.com/sites/default/files/se_monitoring_api.pdf

Build container image then run locally to test, and upload to cloud registry:
- `docker build -t solar-check .`
- `docker push us.gcr.io/check-b9591/solar-check` (gcr is Google Container Registry)
- `docker run -d -p 5000:5000 solar-check` (-d runs as daemon, remove to run in terminal where you stop with ctrl+c)
- `docker ps -a` (view recently run/currently running containers)
- `gunicorn solar:app` (run locally as a non-containerized program)
- Then create Cloud Run service via GCP console - did not work...

Actually this is how I got it working:
- `gcloud builds submit --tag us.gcr.io/check-b9591/solar-check` instead of docker build/push
- `gcloud run deploy --image us.gcr.io/check-b9591/solar-check --platform managed`
  to start a service. I was originally starting via cloud console. Never figured
  out the difference but this worked for me and that did not.

Then I have it set up in DialogFlow/Actions on Google. There is a fulfillment webhook
that hits the URL of the run service.
