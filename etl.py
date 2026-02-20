import pandas as pd

def extract():
    return pd.DataFrame({
        "user_id":[1,2,3],
        "purchases":[10,20,30]

    })

def transform(df):
    df['projected_purchases']=df['purchases']*2
    return df

def load(df):
    df.to_csv("staging_data.csv",index=False)
    print("Data successfully loaded ro staging_data.csv")

if __name__=="__main__":
    print("Starting ETL Job...")
    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data)
    print("ETL Job Complete.")