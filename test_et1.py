import pandas as pd
from et1 import transform

def test_transfrom():
    input_df = pd.DataFrame({
        "user_id":[1],
        "purchases":[10]
    })

    expected_df = pd.DataFrame({
        "user_id":[1],
        "purchases":[10],
        "projected_purchases":[20]
    })

    result_df = transform(input_df)
    
    pd.testing.assert_frame_equal(result_df, expected_df)
