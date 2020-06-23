import requests
def get_data(state, start_date=None, end_date=None, site_type=None, status='all'):
    """ The input state should be abbrevation in lower format. For example, California should be presented as: ca.
    Start/end date should be presented in yyyy-mm-dd format. Water type is presented in ST-abbrevation. For example, 
    Tidal stream should be presented in: ST-TS. Options for status is: 'all', 'active', 'inactive'."""
    if start_date:
        start_date = '&startDT={}'.format(start_date)
    if end_date:
        end_date = '&endDT={}'.format(end_date)
    if site_type:
        site_type = '&siteType={}'.format(site_type)
    if status:
        status = '&siteStatus={}'.format(status)
        
    URL = 'https://waterservices.usgs.gov/nwis/iv/?format=waterml,2.0&stateCd={}{}{}&parameterCd=00060,00065{}{}'.\
    format(state, "" if start_date is None else start_date, "" if end_date is None else end_date, 
           "" if site_type is None else site_type, "" if status is None else status)

    response = requests.get(URL)
    with open('data/%s.xml'%state, 'wb') as file:
        file.write(response.content)
        print('%s data donwloaded'%state)