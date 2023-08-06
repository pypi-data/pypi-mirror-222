from EDAeasy import dataframe_summary
import pandas as pd 

def test_dataframe_summary():
    # Test Case 1: Basic test case with different data types
    data = {
        'age': ['[40-50)', '[60-70)', '[70-80)'],
        'time_in_hospital': [8, 3, 5],
        'n_lab_procedures': [72, 34, 45],
        'weight': [65.5, 70.2, None],
        'is_diabetic': [True, False, True],
    }
    dataframe = pd.DataFrame(data)
    result, (rows, columns) = dataframe_summary(dataframe)
    assert rows == 3
    assert columns == 5
    assert result.loc['age', 'Type'] == 'object'
    assert result.loc['time_in_hospital', 'Type'] == 'int64'
    assert result.loc['n_lab_procedures', 'Type'] == 'int64'
    assert result.loc['weight', 'Type'] == 'float64'
    assert result.loc['is_diabetic', 'Type'] == 'bool'
    assert result.loc['age', 'Min'] == '[40-50)'
    assert result.loc['age', 'Max'] == '[70-80)'
    assert result.loc['time_in_hospital', 'Min'] == 3
    assert result.loc['time_in_hospital', 'Max'] == 8
    assert result.loc['n_lab_procedures', 'Min'] == 34
    assert result.loc['n_lab_procedures', 'Max'] == 72
    assert result.loc['weight', 'Min'] == 65.5
    assert result.loc['weight', 'Max'] == 70.2
    assert result.loc['is_diabetic', 'Min'] == False
    assert result.loc['is_diabetic', 'Max'] == True
    assert result.loc['age', 'Nan %'] == 0.0
    assert result.loc['time_in_hospital', 'Nan %'] == 0.0
    assert result.loc['n_lab_procedures', 'Nan %'] == 0.0
    assert result.loc['weight', 'Nan %'] == 33.33333333333333
    assert result.loc['is_diabetic', 'Nan %'] == 0.0
    assert result.loc['age', '# Unique Values'] == 3
    assert result.loc['time_in_hospital', '# Unique Values'] == 3
    assert result.loc['n_lab_procedures', '# Unique Values'] == 3
    assert result.loc['weight', '# Unique Values'] == 3
    assert result.loc['is_diabetic', '# Unique Values'] == 2
    assert result.loc['age', 'Unique values'] == ['[40-50)', '[60-70)', '[70-80)']
    assert result.loc['time_in_hospital', 'Unique values'] == ['3','5','8']
    assert result.loc['n_lab_procedures', 'Unique values'] == ['34', '45', '72']
    assert result.loc['weight', 'Unique values'] == ['65.5', '70.2', 'nan']
    assert result.loc['is_diabetic', 'Unique values'] == ['False', 'True']

    # Test Case 2: Test with an empty DataFrame
    data = {
        'A': [],
        'B': [],
        'C': [],
    }
    dataframe = pd.DataFrame(data)
    result, (rows, columns) = dataframe_summary(dataframe)
    assert rows == 0
    assert columns == 3
    assert not result.empty

    # Test Case 3: Test with all NaN values in a column
    data = {
        'X': [None, None, None],
        'Y': [1, 2, 3],
    }
    dataframe = pd.DataFrame(data)
    result, (rows, columns) = dataframe_summary(dataframe)
    assert rows == 3
    assert columns == 2
    assert result.loc['X', 'Nan %'] == 100.0
    assert result.loc['Y', 'Nan %'] == 0.0

    # Add more test cases as needed

    print("All test cases passed!")

# Run the test function
test_dataframe_summary()