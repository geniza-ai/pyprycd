# PyPRYCD
This module provides a simple wrapper for working with the PRYCD APIs for real estate analysis.

## Getting Started
To install, simply execute the following command in the command line:

```shell
pip install pyprycd
```
Once you have installed the module, you can 


## Methods
* `set_pricing_api_key(<api_key>)`: Sets or resets the pricing API key. 
* `set_comp_api_key(<api_key>)`  Sets or resets the comp API key. 


## Usage
```python
from pyprycd import PyPrycd

PRICING_API_KEY = '1234'
COMPS_API_KEY = '5678'
pyrcd = PyPrycd(pricing_api_key=PRICING_API_KEY, comp_api_key=COMPS_API_KEY)

# Get pricing data about a property
pricing_data = pyrcd.get_pricing()

```
