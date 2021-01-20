import boto3 

def lambda_handler(event,context):
    ec2_client = boto3.client("ec2")

    regions = [region["RegionName"]
                for region in ec2_client.describe_regions()["Regions"]]
    
    for region in regions:
        ec2 = boto3.resource("ec2", region_name=region)
        print(f"region is: {region}")

        #to list all the unattached volumes - ones in use vs ones that are not 

        volumes = ec2.volumes.filter(
            Filters=[{"Name": "status", "Values": ["available"]}])

        for volume in volumes:
            v = ec2.volume(volume.id)
            print(f"Deleting EBS volume: {v.id}, Size: {v.size} GiB")
            v.delete()