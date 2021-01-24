This AWS lambda function automatically deletes all unused / unattached elastic block store volumes.

Line 1-11: Starting out by looping through all of the regions from our ec2 client then looping through the regions from the ec2 resource itself.

Line 13-21: Based off our ec2 instance we want to filter for the EBS volumes that are unattached >> available, after filtering for that we then just want to delete that volume.
The output gives the volume ID + volume size upon deletion for verification purposes.


