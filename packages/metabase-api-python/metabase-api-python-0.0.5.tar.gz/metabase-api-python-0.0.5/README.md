# Metabase Overview

[Metabase](https://www.metabase.com/) is an open-source tool used for creating data dashboards and visualizations. It simplifies the process of exploring and understanding your data. By providing a user-friendly interface, it allows users to query data without needing extensive SQL knowledge. Metabase supports a variety of databases and has a robust API.


# [Metabase API: An Introduction](https://www.metabase.com/docs/latest/api-documentation)

Metabase is a powerful open-source tool for creating data dashboards and visualizations. It offers a RESTful API, allowing programmatic access and modification of many of its features.

To make use of this script, a local Metabase server needs to be set up. This process involves Docker, which needs to be installed and configured on your system.

## Getting Started 

Follow these steps to set up Metabase locally.

### Prerequisites

Before setting up Metabase locally, you need to have Docker installed on your system as we will be using it for the setup.

- If Docker is not already installed on your system, you can download it from the official Docker website. Here are the links:
	- [Docker for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)
    - [Docker for Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac/)
    - [Docker for Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    - [Docker for other Linux distributions](https://docs.docker.com/engine/install/)

- After installing Docker, you can check whether it's been installed correctly by opening a terminal and running the following command:


```shell
docker --version
```

### Steps

1. **Pull the Metabase image from Docker Hub**
    - Open a terminal and run the following command: `docker pull metabase/metabase`

2. **Run the Metabase Docker container**
    - Run the command: `docker run -d -p 3000:3000 --name metabase metabase/metabase`

3. **Access Metabase**
    - Open your browser and visit `http://localhost:3000`
    - You will be greeted with the Metabase setup wizard. Follow the prompts to set up an account and connect your data sources.

4. **Create and Save a Question**
    - In Metabase, create a new 'question' (a query or report), and save it to your 'Personal Collection' or any other collection.

