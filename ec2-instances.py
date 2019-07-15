import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.command()
@click.option('--list', default=None, help='list the instances')
def list_instances(list):
    if list:
        for i in ec2.instances.all():
            response = i.instance_id
            print(response)
    else:
        return None
if __name__=='__main__':
    list_instances()
