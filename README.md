# Twitter ETL and Data Warehousing Project

This project focuses on building an end-to-end ETL (Extract, Transform, Load) pipeline for Twitter data. The pipeline extracts raw data from Kaggle, processes it using AWS Glue, and loads it into Amazon Redshift. The entire process is automated using AWS Lambda functions and S3 event triggers.


For a detailed breakdown of the project, visit the <a href="https://devengine.notion.site/Twitter-ETL-and-Data-Warehousing-Project-19432fa5808880a3a425ca95f8f76894" target="_blank">Twitter ETL and Data Warehousing Project Documentation</a>

**Dataset:** https://www.kaggle.com/datasets/mmmarchetti/tweets-dataset



## Project Overview

The project involves the following steps:
1. **Data Extraction**: Download the Twitter dataset from Kaggle using the Kaggle API.
2. **Data Transformation**: Use AWS Glue to preprocess and transform the raw data.
3. **Data Cataloging**: Catalog the raw and processed data using AWS Glue Crawlers, making it queryable in Athena.
4. **Automation**: Automate the pipeline using AWS Lambda functions triggered by S3 events.
5. **Data Warehousing**: Load the processed data into Amazon Redshift for advanced analytics.

![Alt Text](https://github.com/suryadeipreddyk/twitter-etl-data-warehousing/blob/main/Twitter%20ETL%20%26%20Data%20Warehousing.png)

## Prerequisites

Before running the project, ensure you have the following:
1. **AWS Account**: With access to S3, Glue, Lambda, Athena, and Redshift.
2. **IAM Roles**: Create IAM roles with the necessary permissions for Glue, Lambda, and Redshift.
3. **Kaggle API**: Set up the Kaggle API to download the dataset.
4. **Python Libraries**: Install required libraries (`boto3`, `pandas`, `kagglehub`, etc.).


For a detailed breakdown of the project, visit the <a href="https://devengine.notion.site/Twitter-ETL-and-Data-Warehousing-Project-19432fa5808880a3a425ca95f8f76894" target="_blank">Twitter ETL and Data Warehousing Project Documentation</a>
