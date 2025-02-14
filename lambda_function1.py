import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')

    # Start Glue Crawler for Raw Data
    try:
        glue.start_crawler(Name="twitter-raw-crawler")
        print("Started Glue Crawler: twitter-raw-crawler")
    except Exception as e:
        print(f"Error starting Glue Crawler (raw): {str(e)}")

    # Start Glue Job for Data Preprocessing
    try:
        glue.start_job_run(JobName="twitter-raw-preprocess")
        print("Started Glue Job: twitter-raw-preprocess")
    except Exception as e:
        print(f"Error starting Glue Job: {str(e)}")