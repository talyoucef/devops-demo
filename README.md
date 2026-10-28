# \# DevOps Demo: Docker \& Monitoring

# 

# A simple DevOps showcase project featuring a Flask application containerized with Docker, monitored by Prometheus, and visualized in Grafana. System and container metrics are collected using Node Exporter and cAdvisor.

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

# │   ├── prometheus.yml      # Scrape configuration

# │   └── grafana/

# │       └── provisioning/

# │           ├── datasources/

# │           │   └── prometheus.yml

# │           └── dashboards/

# │               ├── dashboard.yml

# │               └── demo.json   # Pre-built dashboard

# ├── docker-compose.yml

# └── README.md

# ```

# 

# \## Quick Start

# 

# \### 1. Clone the repository

# 

# Replace `YOUR\_USERNAME` with your GitHub username.

# 

# ```bash

# git clone https://github.com/YOUR\_USERNAME/devops-demo.git

# cd devops-demo

# ```

# 

# \### 2. Build and start the containers

# 

# ```bash

# docker compose up -d --build

# ```

# 

# \### 3. Access the services

# 

# Once the containers are running, access the services at the following URLs:

# 

# | Service | URL | Credentials |

# |---|---|---|

# | Flask App | \[http://localhost:5000](http://localhost:5000) | — |

# | Prometheus | \[http://localhost:9090](http://localhost:9090) | — |

# | Grafana | \[http://localhost:3000](http://localhost:3000) | `admin` / `admin123` |

# 

# > \*\*Note:\*\* The Grafana credentials above assume your Docker Compose configuration sets these default credentials. Change them before exposing Grafana to an untrusted network.

# 

# \## Generating Traffic

# 

# To populate the Grafana dashboard with metrics, generate some basic traffic using the following command:

# 

# ```bash

# for i in {1..20}; do

# &#x20; curl http://localhost:5000/

# &#x20; curl http://localhost:5000/api/data

# &#x20; curl http://localhost:5000/health

# done

# ```

# 

# After generating traffic, open Grafana and inspect your dashboard to view the collected metrics.

# 

# \## Teardown

# 

# Stop and remove the containers:

# 

# ```bash

# docker compose down

# ```

# 

# To also remove persistent data volumes:

# 

# ```bash

# docker compose down -v

# ```

# 

# > \*\*Warning:\*\* The `-v` option deletes the Compose-managed persistent volumes, which may contain your Prometheus or Grafana data.



