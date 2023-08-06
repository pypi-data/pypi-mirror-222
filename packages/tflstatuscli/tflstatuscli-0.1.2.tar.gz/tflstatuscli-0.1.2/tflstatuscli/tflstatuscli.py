import requests
import typer
from rich import print
from rich.table import Table

app = typer.Typer()

valid_line_ids = [line['id'] for line in requests.get('https://api.tfl.gov.uk/Line/Mode/tube').json()]


def validate_line(line):
    '''
    Grab all lines for Mode tube from the TFL API and add the line id
    to a list. If line passed in as --line option is not in this list
    raise a ValueError
    '''
    if line not in valid_line_ids and line != 'all':
        raise ValueError(f'Invalid line ID please select from {valid_line_ids} or select  "all"')


@app.command()
def status(
        line: str = 'all'
):
    '''
    Get the name, status and any disruptions (planned and unplanned) 
    of all tube lines or a given tube line if specified with --line. 
    prints output in a table format
    '''
    validate_line(line)

    table = Table(title='Tube Line Status')
    table.add_column("Line")
    table.add_column("Status")
    table.add_column("Disruption")

    if line != 'all':
        r = requests.get('https://api.tfl.gov.uk/Line/' + line + '/Status')
        data = r.json()
        #print(data)
        line_name = data[0]['name']
        line_status = data[0]['lineStatuses'][0]['statusSeverityDescription']
        if 'disruption' in data[0]['lineStatuses'][0].keys():
            line_disruption = data[0]['lineStatuses'][0]['disruption']['description']
        else:
            line_disruption = 'None'

        table.add_row(line_name, line_status, line_disruption)
    else:
        for line in valid_line_ids:
            r = requests.get('https://api.tfl.gov.uk/Line/' + line + '/Status')
            data = r.json()
            line_name = data[0]['name']
            line_status = data[0]['lineStatuses'][0]['statusSeverityDescription']
            if 'disruption' in data[0]['lineStatuses'][0].keys():
                line_disruption = data[0]['lineStatuses'][0]['disruption']['description']
            else:
                line_disruption = 'None'
            table.add_row(line_name, line_status, line_disruption)

    print(table)


@app.command()
def disruptions():
    '''
    Show all unplanned disruptions on tube services
    '''
    r = requests.get('https://api.tfl.gov.uk/Line/Mode/tube/Disruption')
    data = r.json()
    for i in data:
        print(i['description'])


if __name__ == '__main__':
   app()
   