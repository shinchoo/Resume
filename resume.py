import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Shin H. Choo
##### *Resume* 
''')

image = Image.open('증명사진.jpg')
st.image(image, width = 150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Data Scientist and Buyer with 4+ years of experience developing and deploying ML solutions for manufacturing, logistics, and analytics.
- Skilled in end-to-end delivery (anomaly detection, optimization, forecasting) with a proven record of implementing scalable, cost-saving analytics in production
        ''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://shinchoo.github.io/" target="_blank">Shin H. Choo</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#academic-projects">Academic Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a,b):
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)

def txt3(a,b):
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

#####################
st.markdown('''
## Education
''')

txt('**Master of Applied Data Science**, *University of Michigan - Ann Arbor*',
    '2023-2025')

txt('**Bachelors of Science** (Economics, Statistics Minor), *University of Michigan - Ann Arbor*',
    '2019-2022')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Scientist & Buyer**, General Motors',
    '2025-Present')
st.markdown('''
- Led strategic sourcing of $900M+ in annual transportation spend across intercontinental trucking and air freight, managin end-to-end RFQ, supplier evaluation, and contract negotiation across 3 bidding rounds
- Reduced Annual Procurement Value (APV) by 5% versus prior contracts while maintaining operational continuity, generating multimillion-dollar transportation cost savings through sourcing optimization and negotiation strategy
- Developed automated API-based logistics data pipelines integrating real-time provider operational data into internal databases on hourly refresh schedules, enabling scalable transportation analytics and monitoring
- Engineered interactive Streamlit decision-support application automating transportation change request analysis, route visualization, market benchmark comparison, and APV impact forecasting through contract expiration
- Developed Power BI freight spend governance dashboards to monitor invoice-level trnasportation spend, identify contract leakage, and compare realized spend against contracted APV expectations
            
''')

txt('**Data Scientist/Analytics**, KLA Corporation',
    '2022-2025')
st.markdown('''
- Developed and deployed a logistic regression model using Python and Snowflake SQL to classify over 5M misclassified product parts with 95% accuracy, increasing operational efficiency by 30% and generating $1.2M+ in annual savings
- Automated daily DHL shipping data ingestion pipeline by engineering Python scripts utilizing pysftp and snowflake-connector, transffering and loading files via SFTP into Snowlfkae data warehouse, reduced data processing time by 84%, accelerating access for 100+ business and analytics stakeholders
- Engineered data pipelines and 15+ interactive Power BI dashboards utilizing Python (pandas, matplotlib) and Power Query, optimizing data flows and visualization processes to achieve 50% increase in effiency across 10 business units
- Built ETL pipelines with Python, Spark, and SQL to unify ENOVIA, SAP, and Snowflake data, automating BOM reports and cutting Engineering Change Order cycle time by 50%
- Performed A/B testing using Python (KS-test via scipy) and SQL to compare manufacturing tool waivers, generating data-driven solutions that improved non-conformance metrics by $1.2M+ per year            
''')

txt('**Data Analyst Intern**, Quicken Loans (Rocket Mortgage)',
    '2021-2021')
st.markdown('''
- Developed a time series forecasting model using XGBoost in Python, integrating external economic indicators from U.S Bureau of Labor Statistics APIs to accurately predict loan approval rates and monthly authorization volumes
- Developed an interactive Power BI Dashboard, utilizing automated Python-SQL ETL workflows to visualize daily production KPIs and forbearance trends, supporting leadership decisions for $30M+ in daily revenue streams
- Facilitated project goal-setting and mentored intern teams in Python-based analytics and data visualization, delivering cross-functional insights to executive-level reporting
''')

txt('**Sergeant/Squad Leader**, U.S. Army (Active Duty)',
    '2015-2019')
st.markdown('''
- Managed operational budgeting and cost estimation for logistics, equipment, and personnel across 7 major training programs, leveraing quantitative planning models in Excel to optimize resource allocation and reduce excess spend
- Automated daily and monthly personnel and financial reporting across 8 units by developing custom Excel VBA scripts, streamlining report generation and integration into Word for weekly Commander briefings; decreased manual workload by 70%
- Mentored and led a team of 8 soldiers, designing and executing targeted training programs in leadership, tactical skills, and resilience; improved overall physical readiness and mission effectiveness
''')

#####################
st.markdown('''
## Academic Projects
''')

txt('**2020 COVID-19 Forecasting**',
    'Regression')
st.markdown('''
- Developed end-to-end time series forecasting pipeline in Python (statsmodels, pandas) to predict daily new COVID-19 cases across six countries, utilizing ARIMA and VAR models; delivered forecasts and cross-country trends to inform public health policy and resource planning
''')

txt('**IMDB Movie Recommender System**',
    '(Un)Supervised')
st.markdown('''
- Developed a movie sentiment classifier achieveing 69.4% accuracy and 0.67 F1 by engineering BERT plot feature and training ensemble models (XGBoost, Random Forecast, Logistic Regression) with hyperparamete optimization in Python
- Clustered movies by themes, raising sillhouette score to 0.46 by applying TF-IDF, KMeans, and UMAP - revealing genre-driven structures within the dataset
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Model deployment', '`streamlit`')
txt3('Methods','`Linear/Logistic Regression`,`Random Forest`,`SVM`,`KNN`,`Gradient Boosting Machine`,`Time-Series Forecasting`,`K-Means Clustering`,`Principal Component Analysis`,`t-SNE`,`Large Language Models`,`Natural Language Proessing`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn','https://www.linkedin.com/in/shin-choo-3b87b41ab/')
txt2('GitHub','https://shinchoo.github.io/')
