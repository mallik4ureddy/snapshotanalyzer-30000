import boto3 #boto3 is the python SDK to handle and communicate with AWS resources
import click #We are importing click to use the click commands

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.group()
def instances():
    """Commands for instances"""

@instances.command('list') #This will give our scirpt a nice help option and also takes control of the list_instances function beneath
@click.option('--project', default=None, help="Only instances for project (tag Project:<name>)")
def list_instances(project):
    "List EC2 instances" #This is a python feature called doc string. It needs to be under the function. click makes use of this doc string and displays during help command
    instances = []
    if project:
        filters = [{'Name':'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
       instances = ec2.instances.all()

    for i in instances:
        tags = { t['Key']: t['Value'] for t in i.tags or [] }
        print(", ".join((
            i.id,
            i.instance_type,
            i.placement["AvailabilityZone"],
            i.state["Name"],
            i.public_dns_name,
            tags.get('Project', '<no project>')
            )))
    return

@instances.command('stop')
@click.option('--project', default=None, help='Only instances for projects')
def stop_instances(project):
    "Stop EC2 instances"
    instances = []
    if project:
        filters = [{'Name':'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
       instances = ec2.instances.all()

    for i in instances():
        print("Stopping {0}...".format(i.id))
        i.stop()

    return

if __name__=='__main__': #Use this as the main function
    instances()
