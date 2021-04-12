
# TODO: import some code

# TODO: test the code
# use his respository to fill this out
# NOT FINISHED, all code from class 



def test_summarize():
    #it should summarize and aggregate the data:
    assert summarize_data(process_data(mock_msft_response)) == {
        'latest_close': 237.71,
        'recent_high': 240.055,
        'recent_low':231.81
    }
    assert summarize_data(process_data(mock_amzn_response)) == {
        'latest_close': 3091.86,
        'latest_high': 3131.7843,
        'recent_low':; 3030.05
    }

def test_charting():
    #it should sort dates in the proper order (ascending) for charting:
    df = process_data(mock_amzn_response)
    chart_df = prepare_data_for_charting(df)
    assert chart_df['date'].tolist() == ['20']
