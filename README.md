# Tetration Alert Client (Python)

This is an example Tetration alerts client written in Python

To connect and print incoming alerts
```bash
# clone this repository
git clone https://github.com/tetration-exchange/alert-client-python.git && cd alert-client-python

# install dependencies
pip install -r requirements.txt

# copy your alerts data tap credentials (download in "certificate" format)
cp /path/to/downloaded/Alerts-${tenant-name}.cert.tar.gz ./credentials.tar.gz

# make the credentials directory and unzip keys and certificates
mkdir credentials
tar -xzvf credentials.tar.gz -C credentials

# run the client - python 3 required!
python alerts.py
```

#### Example alert
```
Live Analysis Annotated Flows contains escaped for Live Analysis Application Secure X Global Web Servers
{'application_id': '5eab2e2d755f020c304bd929',
 'consumer_scope_ids': ['5e56fc6f755f0229d4a64acf', '5eab2dfd755f020c304bd926'],
 'consumer_scope_names': ['SBGSECUREXPOV', 'SBGSECUREXPOV:Internet 🌎'],
 'escaped_count': 1,
 'internal_trigger': {'datasource': 'live_analysis_compliance',
                      'label': 'Alert Trigger',
                      'rules': {'field': 'policy_violations',
                                'type': 'contains',
                                'value': 'escaped'}},
 'policy_category': ['ESCAPED'],
 'policy_type': 'LIVE_POLICY',
 'protocol': 'TCP',
 'provider_port': 445,
 'provider_scope_ids': ['5e56fc6f755f0229d4a64acf', '5eab2dcd755f020c304bd922'],
 'provider_scope_names': ['SBGSECUREXPOV',
                          'SBGSECUREXPOV:SecureX Test Machines'],
 'time_range': [1588376340000, 1588376399999]}
 ```


## License
This code is provided as-is with an Apache 2.0 license