import boto3
import time

# instantiate a boto3 client for RDS
rds = boto3.client('rds')

# user defined variable
username = 'dctuser1'
password = 'Ashish123'
db_subset_group = 'vpc-hol'
db_cluster_id = 'rds-hol-cluster'

# Create the DB cluster
try:
    response = rds.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
    print(f"The DB cluster named '{db_cluster_id}' already exists. Skipping creating.")
except rds.exceptions.DBClusterNotFoundFault:
    response = rds.create_db_cluster(
        Engine='aurora-mysql',
        EngineVersion='5.7.mysql_aurora.2.08.3',
        DBClusterIdentifier=db_cluster_id,
        MasterUsername=username,
        MasterUserPassword=password,
        DatabaseName='rds_hol_db',
        DBSubnetGroupName=db_subset_group,
        EngineMode='serverless',
        EnableHttpEndpoint=True,
        ScalingConfiguration={
            'MinCapacity': 1,
            'MaxCapacity': 8,
            'AutoPause': True,
            'SecondsUntilAutoPause': 300
        }
    )
    print(f"The DB cluster named '{db_cluster_id}' has been created.")

    # Wait for the DB cluster to become available
    while True:
        response = rds.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
        status = response['DBClusters'][0]['Status']
        print(f"The status of the cluster is '{status}'.")
        if status == 'available':
            break
        print('Waiting for the DB Cluster to become available...')
        time.sleep(40)

# Modify the DB cluster. Update the scaling configuration for the cluster.
response = rds.modify_db_cluster(
    DBClusterIdentifier=db_cluster_id,
    ScalingConfiguration={
        'MinCapacity': 1, # Minimum ACU
        'MaxCapacity': 16, # Maximum ACU
        'SecondsUntilAutoPause': 600 # Pause after 10 minutes of inactivity.
    }
)
print(f"Updated the scaling configuration for DB cluster '{db_cluster_id}'.")

# Delete the DB cluster.
response = rds.delete_db_cluster(
    DBClusterIdentifier=db_cluster_id,
    SkipFinalSnapshot=True
)
print(f"The '{db_cluster_id}' is being deleted.")