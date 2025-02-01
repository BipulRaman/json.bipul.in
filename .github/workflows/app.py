import os
import pandas as pd

# Process the first CSV file
df = pd.read_csv('dist/sam25.csv')
df = df.rename(columns={
    'Timestamp': 'Timestamp',
    'Email Address': 'Email',
    'Name': 'Name',
    'Gender': 'Gender',
    'Phone number': 'Phone',
    'Current Location (City, State) ': 'Location',
    'First JNV': 'FirstJnv',
    'Migration JNVs Name': 'OtherJnv',
    'Entry Year in JNV': 'EntryYear',
    'Exit Year in JNV': 'ExitYear',
    'Entry Class in JNV': 'EntryClass',
    'Current Profile': 'Profile',
    'Current Organization / Institute': 'Org',
    'Current Designation / Degree': 'Deg',
    'Which event you are planning to attend at Samagam': 'Attending',
    'Donation Amount': 'Donation'
})
df.to_json('dist/sam25.json', orient='records', lines=True)
os.remove('dist/sam25.csv')

# Process the second CSV file
df = pd.read_csv('dist/medico.csv')
df['Batch'] = df['Entry Year'] - (df['Entry Class'] - 6)
df = df.rename(columns={
    'Email': 'Email',
    'Name': 'Name',
    'Gender': 'Gender',
    'First JNV': 'FirstJnv',
    'Entry Year': 'EntryYear',
    'Entry Class': 'EntryClass',
    'Public phone number': 'Phone',
    'Current Location (City, State) ': 'Location',
    'Current Practice': 'Practice',
    'Medical Degree': 'Degree',
    'Specialization': 'Specialization',
    'University / College attended': 'College',
    'Name of Clinic / Hospital / Institute / Organization ': 'Org',
    'Designation': 'Deg'
})
df.to_json('dist/medico.json', orient='records', lines=True)
os.remove('dist/medico.csv')
