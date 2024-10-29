import streamlit as st
import plotly.express as px

def create_visualizations(data):
    """Create visualizations for the dashboard."""
    # 1. Median Salary by Job Title
    st.subheader("Median Salary by Job Title")
    title_med_salary = data.groupby("title").agg({'normalized_salary': 'median'}).reset_index().sort_values(by='normalized_salary', ascending=False)
    title_med_salary_fig = px.bar(title_med_salary, x='title', y='normalized_salary', title='Median Salary by Job Title')
    st.plotly_chart(title_med_salary_fig)

    # 2. Median Salary by State
    st.subheader("Median Salary by State")
    state_med_salary = data.groupby("state").agg({'normalized_salary': 'median'}).reset_index().sort_values(by='normalized_salary', ascending=False)
    state_med_salary_fig = px.bar(state_med_salary, x='state', y='normalized_salary', title='Median Salary by State')
    st.plotly_chart(state_med_salary_fig)

    # 3. Top Companies by Number of Job Postings
    st.subheader("Top Companies by Number of Job Postings")
    top_companies = data['company_name'].value_counts().head(20)
    top_companies_fig = px.bar(top_companies, x=top_companies.index, y=top_companies.values, title='Top Companies by Job Postings')
    st.plotly_chart(top_companies_fig)

    # 4. Salary Comparison Across Job Types
    st.subheader("Salary Comparison Across Job Types")
    job_type_salary_fig = px.box(data, x='work_type', y='normalized_salary', title='Salary Comparison by Job Type')
    st.plotly_chart(job_type_salary_fig)

    # 5. Job Title vs. Applications
    st.subheader("Job Title vs. Applications")
    views_fig = px.scatter(data, x='title', y='applies', title='Job Title vs. Applications', size='applies', hover_name='title')
    st.plotly_chart(views_fig)

    # 6. Salary by Location (Heatmap)
    st.subheader("Geographical Salary Heatmap")
    location_salary_fig = px.choropleth(
        data_frame=state_med_salary,
        locations='state',
        locationmode='USA-states',
        color='normalized_salary',
        title='Median Salary by Location',
        scope='usa',  # Set scope to 'usa' to focus on the U.S.
        hover_name='state',  # Show state names on hover
        hover_data={
            'normalized_salary': True,  # Show average salary on hover
            'state': False  # Optionally hide the state name since it's already displayed
        }
    )

    # Update the layout to add annotations for the salaries
    location_salary_fig.update_traces(
        text=state_med_salary['normalized_salary'],  # Display average salary
    )

    st.plotly_chart(location_salary_fig)
    
    # 7. Experience Level Analysis
    st.subheader("Job Postings by Experience Level")
    exp_level_count = data['formatted_experience_level'].value_counts().reset_index()
    exp_level_count.columns = ['Experience Level', 'Number of Postings']
    exp_level_count_fig = px.bar(exp_level_count, x='Experience Level', y='Number of Postings', title='Number of Job Postings by Experience Level')
    st.plotly_chart(exp_level_count_fig)

    # Salary bands by experience level
    exp_level_salary = data.groupby('formatted_experience_level').agg({'normalized_salary': 'median'}).reset_index().sort_values(by="normalized_salary", ascending=False)
    exp_level_salary.columns = ['Experience Level', 'Median Salary']
    exp_level_salary_fig = px.bar(exp_level_salary, x='Experience Level', y='Median Salary', title='Median Salary by Experience Level')
    st.plotly_chart(exp_level_salary_fig)
