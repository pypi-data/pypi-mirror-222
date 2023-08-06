# tflstatuscli
tflstatuscli is a Python CLI written using the Typer CLI framework for querying the TFL Tube line statuses

## Installation
```bash
pip install tflstatuscli
```

## Usage
### Show status of all tube lines
```bash
tflcli status   
```

### Show status of particular tube line
```bash
tflcli status --line <line_name>
```
NOTE: When searching a particular tube line, validity is checked against the TFL APIs list of tube lines which at the time of writing this includes;
- Bakerloo 
- Central            
- Circle             
- District           
- Hammersmith & City 
- Jubilee            
- Metropolitan                                         
- Northern           
- Piccadilly         
- Victoria           
- Waterloo & City

### Show future disruptions of particular tube line
```bash
tflcli status --line <line_name> --startdate YYYY-MM-DD --enddate YYYY-MM-DD
```
NOTE: When searching a particular tube line, validity is checked against the TFL APIs list of tube lines which at the time of writing this includes;
- Bakerloo 
- Central            
- Circle             
- District           
- Hammersmith & City 
- Jubilee            
- Metropolitan                                         
- Northern           
- Piccadilly         
- Victoria           
- Waterloo & City


### Show all disruptions on TFL tube lines
```bash
tflcli disruptions
```

## Poetry Usage
Run these commands within project root dir with python poetry installed.

### Install package and dependancies locally
```bash
poetry install
```

### Run tests 
```bash
poetry run pytest -v
``` 

### Build wheel 
```
poetry build
```
NOTE: Wheel located under /dist in project root dir

