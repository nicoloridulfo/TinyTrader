from TinyTrader import initdb
from os import listdir
import pandas as pd
import datetime

"""
This test suit will test the following:
    - Downloading of the initial data
    - Overriding of the initial data when main is called twice
"""
def test_init():
    initdb.main()

def test_data_is_pickled():
    """
    This test tests that the data is pickled and that it is readable.
    """
    assert(all(".p" in file for file in listdir("data")))
    for file in listdir("data"):
        df = pd.read_pickle(f"data/{file}")
        assert(len(df)>0)
        assert(all(column in df.columns for column in ["Open", "High", "Low", "Close"]))

def test_override():
    for symbol in listdir("data"):
        df = pd.read_pickle(f"data/{symbol}")
        df = df[0:0].to_pickle(f"data/{symbol}")
    for file in listdir("data"):
        df = pd.read_pickle(f"data/{file}")
        assert(len(df)==0)
    initdb.main()
    for file in listdir("data"):
        df = pd.read_pickle(f"data/{file}")
        assert(len(df)>0)

def test_uptodate():
    for i, symbol in enumerate(listdir("data")):
        df = pd.read_pickle(f"data/{symbol}")
        if i==0:
            latest = df.index[-1]
        else:
            assert(latest in df.index)

    latest = latest.to_pydatetime()
    latestallowed = datetime.datetime.today()
    if latestallowed.weekday()>4:
        latestallowed -= datetime.timedelta(days=latestallowed.weekday()-4)
    assert(latestallowed.date()==latest.date())
        
