#!/usr/bin/python
#import sys
import boto3
import logging
import os.path
logging.basicConfig(
    filename="log1.log",
    level=10,
    format="%(asctime)s:%(levelno)s:%(message)s"

)


client = boto3.client('cloudformation')

def main():
    cf_validation("/home/prasanth/Documents/Workspace/cfsample1.json")
    cf_stack_creation('cfsample3', "/home/prasanth/Documents/Workspace/cfsample1.json")
    cf_stack_description('cfsample3')


def cf_validation(url):
    with open(url, 'r+') as f:
        valuation = client.validate_template(TemplateBody = f.read())
        logging.debug("Validation log: ", valuation)


def cf_stack_creation(sname,url):
    with open(url, 'r+') as f:
        response = client.create_stack(
            StackName = sname,
            TemplateBody= f.read(),
            TimeoutInMinutes = 2,
            OnFailure='ROLLBACK',)
        logging.debug("Stack creation Output:", response)


def cf_stack_description(sname):
    description = client.describe_stacks(StackName=sname)
    logging.debug("stack description:", description)


if __name__ == '__main__':
    main()
