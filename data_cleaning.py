import pandas as pd
import re
import logging

# List of valid U.S. states
valid_states = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI',
    'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN',
    'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH',
    'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA',
    'WV', 'WI', 'WY'
]

def get_cleaned_state(location):
    """Extract and clean the state from the location string."""
    match = re.search(r',\s*([A-Z]{2})$', location)
    if match:
        state = match.group(1)
        if state in valid_states:
            return state
    return None

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """Clean the dataset."""
    data['applies'].fillna(0, inplace=True)
    data['state'] = data['location'].apply(get_cleaned_state)
    return data
