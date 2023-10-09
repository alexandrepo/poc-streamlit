# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import streamlit as st
import pandas as pd
import numpy as np
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Projetos",
        page_icon="👋",
    )

    #    st.write("# Welcome to Streamlit! 👋")
    today = datetime.date.today()
    date = st.sidebar.write('Período')
    tomorrow = today + datetime.timedelta(days=31)
    date = st.sidebar.date_input('Início', today, format="DD/MM/YYYY")
    date = st.sidebar.date_input('Fim', tomorrow, format="DD/MM/YYYY")

    df = pd.read_csv('./data/Clockify_Time_Report_Detailed_01_01_2023-31_12_2023.csv')
    
    st.write("# Dataset 👋")
    st.write(df.head())
    st.write(df.groupby('Project')['Duration (decimal)'].sum().head(100))
    st.write(df.head())
    


if __name__ == "__main__":
    run()
