Solar stuff to ask the Google Home about current production

API docs
https://www.solaredge.com/sites/default/files/se_monitoring_api.pdf

Build container image then run locally to test, and upload to cloud registry:
- `docker build -t solar-check .`
- `docker push us.gcr.io/check-b9591/solar-check` (gcr is Google Container Registry)
- `docker run -d -p 5000:5000 solar-check` (-d runs as daemon, remove to run in terminal where you stop with ctrl+c)
- `docker ps -a` (view recently run/currently running containers)
- `gunicorn solar:app` (run locally as a non-containerized program)
