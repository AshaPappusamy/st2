import sqlalchemy as sa
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
engine = sa.create_engine("mysql+mysqlconnector://3qKZvyc8Bw7Ckf1.root:ixPIapSBo4owm2Qf@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/Asteroids")

st.write("🔗 SQLAlchemy engine successfully created 👌")

query = """SELECT neo_reference_id, COUNT(*) AS approach_count
           FROM close_approach
           GROUP BY neo_reference_id
           ORDER BY approach_count DESC;"""

with engine.connect() as conn:
    df = pd.read_sql(text(query), conn)

st.write(df)
