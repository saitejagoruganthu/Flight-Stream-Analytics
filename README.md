# Flight Stream Analytics – End-to-End Real-Time Pipeline

This project demonstrates how to build a **real-time flight data analytics pipeline** using:
- **Apache Kafka** for streaming ingestion
- **Apache Iceberg** for table format and storage
- **Presto** for interactive querying
- **MinIO** as the object storage
- **Apache Superset** for dashboards and visualizations
- **Kubernetes (Minikube)** for orchestration
- **Helm** for Kubernetes Package Manager

The pipeline fetches live flight data, writes it to Kafka, persists it in Iceberg tables, queries it with Presto, and visualizes it in Superset. The setup is modular, so you can run it locally in Minikube with persistent storage and visualize KPIs like flight density, unique flights over time, and average velocity.

---
## :open_file_folder: Project Structure
| Step | File                                                                                  | Description                                                         |
| ---- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 0    | [Architecture and Tools](./notes/0%20-%20Architecture%20and%20Tools.md)               | Architecture diagram showing all components and their interactions. |
| 1    | [Setup Minikube Cluster](./notes/1%20-%20Setup%20Minikube%20Cluster.md)               | Install & start Minikube, verify cluster readiness.                 |
| 2    | [Setup MinIO](./notes/2%20-%20Setup%20Minio.md)                                       | Deploy MinIO for object storage, configure persistent volumes.      |
| 3    | [Setup Apache Kafka](./notes/3%20-%20Setup%20Apache%20Kafka.md)                       | Install Kafka using Helm, configure brokers & topics.               |
| 4    | [Setup Presto](./notes/4%20-%20Setup%20Presto.md)                                     | Deploy Presto for querying flight data.                             |
| 5    | [Configure Presto for Iceberg](./notes/5%20-%20Configure%20Presto%20for%20Iceberg.md) | Add Iceberg catalog and S3 (MinIO) configurations to Presto.        |
| 6    | [Fetch and Write Data](./notes/6%20-%20Fetch%20and%20Write%20Data.md)                 | Python scripts to fetch live flight data and send it to Kafka.      |
| 7    | [Sanity Check Data](./notes/7%20-%20Sanity%20Check%20Data.md)                         | Verify Iceberg table creation and data ingestion.                   |
| 8    | [Setup Apache Superset](./notes/8%20-%20Setup%20Apache%20Superset.md)                 | Deploy Superset, connect to Presto, and configure datasets.         |
| 9    | [Add Charts and Dashboard](./notes/9%20-%20Add%20Charts%20and%20Dashboard.md)         | Create map charts for flight density, KPIs, and line/bar charts.    |

---
## :rocket: Quick Start

1. **Clone the repository** 
	
```
	git clone https://github.com/<your-username>/<repo-name>.git
	cd <repo-name>
```

2. **Follow the steps in order** starting from Step 1 to Step 9.
	Each `.md` file contains detailed commands, YAML configurations, and screenshots.
	
3. **View Dashboards:**
	Once Superset is up, access it and explore the dashboard for real-time flight analytics.

---

## :globe_with_meridians: API Endpoint
This project fetches real-time flight data from the OpenSky Network API.

#### REST API Endpoint:  
https://opensky-network.org/api/states/all

This API provides live state vectors for all aircraft within OpenSky’s coverage.
For details on API parameters and usage, refer to their [API Documentation](https://openskynetwork.github.io/opensky-api/index.html).

---

## :bar_chart: Example Visualizations
#### Flight Density Map
Shows high-density regions of flights on a map.
#### Unique Flights Over Time
Line chart of active flights by timestamp.
#### Average Velocity KPI
Real-time KPI of average flight speed.
#### Top Countries by Flight Count
Bar chart of origin countries.

![Pasted image 20250811171120.png](./notes/images/Pasted%20image%2020250811171120.png)

---
## :bulb: Notes
All services run inside Minikube except Superset, run locally.
MinIO uses persistent volumes to store Iceberg table data.
Presto queries Iceberg tables directly via the MinIO S3 endpoint.
Superset connects to Presto to visualize aggregated results.

---
## :scroll: Credits
This project uses real-time data provided by the OpenSky Network.  
The OpenSky Network is a non-profit association providing open access to ADS-B and Mode S data for research and non-commercial use.