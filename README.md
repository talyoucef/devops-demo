# \# DevOps Demo: Docker \& Monitoring

# 

# A simple DevOps showcase project featuring a Flask application containerized with Docker, scraped by Prometheus, with data visualized in Grafana. System and container metrics are collected via Node Exporter and cAdvisor.

# 

# \## Project Structure

# 

# ```text

# devops-demo/

# ├── app/

# │   ├── app.py              # Flask app with Prometheus metrics

# │   ├── Dockerfile

# │   └── requirements.txt

# ├── monitoring/

# │   ├── prometheus.yml      # Scrape config

# │   └── grafana/

# │       └── provisioning/

# │           ├── datasources/prometheus.yml

# │           └── dashboards/

# │               ├── dashboard.yml

# │               └── demo.json   # Pre-built dashboard

# ├── docker-compose.yml

# └── README.md

# ```

# 

# \## Quick Start

# 

# 1\. Clone the repository:

# &#x20;  ```bash

# &#x20;  git clone \[https://github.com/YOUR\_USERNAME/devops-demo.git](https://github.com/YOUR\_USERNAME/devops-demo.git)

# &#x20;  cd devops-demo

# &#x20;  ```

# 

# 2\. Build and start the containers:

# &#x20;  ```bash

# &#x20;  docker compose up -d --build

# &#x20;  ```

# 

# 3\. Access the services:

# &#x20;  - \*\*App:\*\* http://localhost:5000

# &#x20;  - \*\*Prometheus:\*\* http://localhost:9090

# &#x20;  - \*\*Grafana:\*\* http://localhost:3000 (admin / admin123)

# 

# \## Generating Traffic

# 

# To populate the Grafana dashboard with metrics, generate some basic traffic:

# 

# ```bash

# for i in {1..20}; do

# &#x20; curl http://localhost:5000/

# &#x20; curl http://localhost:5000/api/data

# &#x20; curl http://localhost:5000/health

# done

# ```

# 

# \## Teardown

# 

# ```bash

# docker compose down

# \# Include -v to also remove persistent data volumes

# docker compose down -v

# ```

