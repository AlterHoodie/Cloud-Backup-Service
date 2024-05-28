# BackUp Cloud Service

This project is a robust backup service designed to regularly back up a user-defined directory to a Google Drive folder. The service leverages Kubernetes to ensure reliable deployments, making it suitable for both personal and professional use cases where data integrity and accessibility are paramount.

## Key Features

* **Automated Backups**: The service automatically performs backups at user-defined intervals, ensuring that your data is always up-to-date.
* **Cloud Storage**: Backups are stored in a Google Drive folder, providing easy access and sharing capabilities
* **Change Monitoring**: An observer script monitors changes in the specified directory and logs these events, providing a comprehensive record of file modifications.
* **User Interface**: A Streamlit-based web interface allows users to view logs and track the status of their backups.

## Prerequisites

* Docker
* DockerHub account
* Minikube
* Kubernetes
* Google Drive API credentials

## Components

* **./data/myDir**: The directory being backed up to Google Drive.
* **Dockerfile**: Defines the container that runs the backup script (`backup_script.py`). This script is executed at regular intervals by the Kubernetes CronJob.
* **observer.py**: Monitors changes in the directory and logs them to `file_events.log`.
* **app.py**: A Streamlit application for viewing the backup logs.
* **cron_pvc.yaml**: Kubernetes configuration file for creating and scheduling the backup service pods.

## Setup and Running Instructions

1. **Install Dependencies**

      ```bash
       pip install -r requirements.txt
2. **Configure Secrets**

    - Add your Google Drive API credentials to secrets.yaml in base64 encoded format.
3. **Build the Container Image**
    - Build the Container Image:

      ```bash
       docker build -t <username>/backup:latest . 
    - **Push the Image to DockerHub**

        ```bash
       docker push <username>/backup:latest 
4. Start MiniKube

       minikube start
5. Mount Directory
    - Mount the Directory to MiniKube in another terminal and keep it running 

        ```bash 
        minikube mount ./data:/data
6. Setup Kubernetes Resources
    - Create a Persistant Volume

         ```bash
        kubectl apply -f ./pv.yaml
    - Create a Persistent Volume Claim

        ```bash
       kubectl apply -f ./pvc.yaml
    - Create a Kubernetes Secret for Google Drive Tokens:

        ```bash
       kubectl apply -f ./secrets.yaml
    - Schedule Cron Job for BackUps:

        ```bash
       kubectl apply -f ./cron_pvc.yaml
7. Start Observer and StreamLit App
    - Start the Observer Script:

        ```bash
       python ./observer.py
    - Run the Streamlit App to view Logs:

        ```bash
       streamlit run app.py

## Usage Example

To Configure the Backup Schedule, modify the ` cron_pvc.yaml ` file with your desired schedule using the Cron Syntax
> Current Configuration is set to 1 Minute Backups
