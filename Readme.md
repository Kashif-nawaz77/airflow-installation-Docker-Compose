# Project Showcase - Apache Airflow Setup

Welcome to the showcase of our Apache Airflow project setup. 🚀 This guide will help you quickly set up Apache Airflow using Docker Compose.

## Getting Started

To pull the Docker Compose file, execute the following command in your project folder:

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.0/docker-compose.yaml'
```

If you encounter the "Invoke-WebRequest" error, run the following command first:

```bash
Remove-item alias:curl
```

Then, rerun the `curl` command to download the Docker Compose file.

## Docker Compose Configuration

In the Docker Compose file, configure environment variables and create necessary directories:

```bash
mkdir ./dags, ./plugins, ./logs
```

Ensure permissions match between your containers and machine. if not you should create a new `.env` file in project directory and add these details in the `.env` file:

```env
AIRFLOW_UID=50000
AIRFLOW_GID=0
```

## Initializing Airflow Instance

Execute the following command to create the Docker container:

```bash
docker-compose up airflow-init
```

This initializes the Airflow instance, pulling the updated image if not found, and creates the user with credentials.

## Running Services

To run all services, execute:

```bash
docker-compose up
```

Check the status of running containers:

```bash
docker ps
```

## Accessing Airflow

Open a browser and navigate to [http://localhost:8080/login/](http://localhost:8080/login/). Log in with:

- Username: airflow
- Password: airflow

You should see the list of example DAGs.

## Command Line Interface

To access the command-line interface, find the container ID of the Airflow webserver/scheduler/worker:

```bash
docker ps
```

Copy the container ID and execute:

```bash
docker exec [container ID] [command to execute]
docker exec 3a0dcb1a243b airflow version
```

Enjoy using Apache Airflow for efficient workflow orchestration! 🌐🛠️