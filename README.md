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
2020-06-23 15:32:47
Live Analysis Rejected Flows > 0 for Live Analysis Application Secure X Global Web Servers
application_id: 5eab2e2d755f020c304bd929
constituent_flows:
- consumer_address: 172.31.37.92
  consumer_port: 49850
  protocol: TCP
  provider_address: 146.112.63.6
  provider_port: 443
- consumer_address: 172.31.32.159
  consumer_port: 64779
  protocol: TCP
  provider_address: 146.112.63.13
  provider_port: 443
consumer_scope_ids:
- 5e56fc6f755f0229d4a64acf
- 5eab2dcd755f020c304bd922
consumer_scope_names:
- SBGSECUREXPOV
- SBGSECUREXPOV:SecureX Test Machines
internal_trigger:
  datasource: live_analysis_compliance
  label: Alert Trigger
  rules:
    field: rejected_count
    type: gt
    value: 0
policy_category:
- REJECTED
policy_type: LIVE_POLICY
protocol: TCP
provider_port: 443
provider_scope_ids:
- 5e56fc6f755f0229d4a64acf
- 5eab2dfd755f020c304bd926
provider_scope_names:
- SBGSECUREXPOV
- SBGSECUREXPOV:Internet 🌎
rejected_count: 2
time_range:
- 1592951220000
- 1592951279999
 ```

## In Action
[![asciicast](https://asciinema.org/a/cpUyurUKHasjCKLXWQZwQHSDX.svg)](https://asciinema.org/a/cpUyurUKHasjCKLXWQZwQHSDX)

## License
This code is provided as-is with an Apache 2.0 license