import pandas as pd

# %% New ipython cell ================

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')

print(staff_df.head())
print(student_df.head())

# %% New ipython cell ================

pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)

# %% New ipython cell ================

pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)

# %% New ipython cell ================

pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)

# %% New ipython cell ================

pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)

# %% New ipython cell ================

staff_df = staff_df.reset_index()
student_df = student_df.reset_index()

pd.merge(staff_df, student_df, how='right', on='Name')

# %% New ipython cell ================

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR',
                          'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion',
                          'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader',
                          'Location': 'Washington Avenue'}])

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business',
                            'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law',
                            'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering',
                            'Location': '512 Wilson Crescent'}])

pd.merge(staff_df, student_df, how='left', on='Name')

# %% New ipython cell ================

staff_df = pd.DataFrame([{'Name': 'Kelly',
                          'Last Name': 'Desjardins',
                          'Role': 'Director of HR',
                          'Location': 'State Street'},
                         {'Name': 'Sally',
                          'Last Name': 'Brooks',
                          'Role': 'Course liasion',
                          'Location': 'Washington Avenue'},
                         {'Name': 'James',
                          'Last Name': 'Wilde',
                          'Role': 'Grader',
                          'Location': 'Washington Avenue'}])

student_df = pd.DataFrame([{'Name': 'James',
                            'Last Name': 'Hammond',
                            'School': 'Business',
                            'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike',
                            'Last Name': 'Smith',
                            'School': 'Law',
                            'Location': 'Fraternity House #22'},
                           {'Name': 'Sally',
                            'Last Name': 'Brooks',
                            'School': 'Engineering',
                            'Location': '512 Wilson Crescent'}])

pd.merge(staff_df, student_df, how='inner', on=['Name', 'Last Name'])

