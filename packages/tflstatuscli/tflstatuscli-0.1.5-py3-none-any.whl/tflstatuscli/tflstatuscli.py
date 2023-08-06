'''
tflstatuscli - CLI to interact with TFL API to query tube line statuses
'''
from datetime import datetime
import requests
import typer
from rich import print # pylint: disable=redefined-builtin
from rich.table import Table

app = typer.Typer()

valid_line_ids = [line['id'] for line in
                  requests.get('https://api.tfl.gov.uk/Line/Mode/tube', timeout=10).json()]

def validate_line(line):
    '''
    Grab all lines for Mode tube from the TFL API and add the line id
    to a list. If line passed in as --line option is not in this list
    raise a ValueError
    '''
    if line not in valid_line_ids and line != 'all':
        raise ValueError(f'Invalid line ID please select from {valid_line_ids} or select  "all"')


@app.command()
def status( # pylint: disable=too-many-branches
        line: str = 'all',
        startdate: datetime = None,
        enddate: datetime  = None

):
    '''
    Get the name, status and any disruptions (planned and unplanned) 
    of all tube lines or a given tube line if specified with --line. 
    prints output in a table format
    '''
    # Check the line argument is valid
    validate_line(line)

    # Check both a start and end date are supplied if doing a date range
    if startdate is None:
        if enddate is not None:
            raise ValueError("startdate requires an enddate!")
    if enddate is None:
        if startdate is not None:
            raise ValueError("enddate requires an startdate!")

    # Create a table for some output
    table = Table(title='Tube Line Status')
    table.add_column("Line")
    table.add_column("Status")
    table.add_column("Disruption")

    # Output a specific line status
    if line != 'all':
        if enddate is None and startdate is None:
            req = requests.get('https://api.tfl.gov.uk/Line/' + line + '/Status', timeout=10)
            data = req.json()
            line_name = data[0]['name']
            line_current_status = data[0]['lineStatuses'][0]['statusSeverityDescription']
            if 'disruption' in data[0]['lineStatuses'][0].keys():
                line_disruption = data[0]['lineStatuses'][0]['disruption']['description']
            else:
                line_disruption = 'None'
            table.add_row(line_name, line_current_status, line_disruption)
            print(table)
        else:
            req = requests.get('https://api.tfl.gov.uk/Line/' +
                               line + '/Status/' +
                               startdate.strftime("%Y-%m-%d") + '/to/'
                               + enddate.strftime("%Y-%m-%d"), timeout=10)
            data = req.json()
            line_name = data[0]['name']
            line_current_status = data[0]['lineStatuses'][0]['statusSeverityDescription']
            for linestatus in data[0]['lineStatuses']:
                if linestatus['statusSeverityDescription'] != 'Good Service':
                    print(linestatus['reason'])
    # Output all line statuses by looping through and adding each line to table
    else:
        for valid_line in valid_line_ids:
            req = requests.get('https://api.tfl.gov.uk/Line/' + valid_line + '/Status', timeout=10)
            data = req.json()
            line_name = data[0]['name']
            line_current_status = data[0]['lineStatuses'][0]['statusSeverityDescription']
            if 'disruption' in data[0]['lineStatuses'][0].keys():
                line_disruption = data[0]['lineStatuses'][0]['disruption']['description']
            else:
                line_disruption = 'None'
            table.add_row(line_name, line_current_status, line_disruption)
            print(table)


@app.command()
def disruptions():
    '''
    Show all unplanned disruptions on tube services
    '''
    req = requests.get('https://api.tfl.gov.uk/Line/Mode/tube/Disruption', timeout=10)
    data = req.json()
    for i in data:
        print(i['description'])


if __name__ == '__main__':
    app()
   