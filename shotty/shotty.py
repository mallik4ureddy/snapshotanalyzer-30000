import boto3 #boto3 is the python SDK to handle and communicate with AWS resources
import click #We are importing click to use the click commands

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.command() #This will give our scirpt a nice help option and also takes control of the list_instances function beneath
def list_instances():
    "List EC2 instances" #This is a python feature called doc string. It needs to be under the function. click makes use of this doc string and displays during help command
    for i in ec2.instances.all():
        print(", ".join((
            i.id,
            i.instance_type,
            i.placement["AvailabilityZone"],
            i.state["Name"],
            i.public_dns_name)))
    return

if __name__=='__main__': #Use this as the main function
    list_instances()
