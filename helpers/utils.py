def uniques(df):
    uniques_ = {}
    cols = df.columns
    for i in cols:
        uniques_[i] = df[i].unique()
    return uniques_ 