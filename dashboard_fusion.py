import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import pandas as pd
import streamlit as st
#@st.cache  # This decorator improves app performance by caching the DataFrame

#df = pd.read_excel('C:/Users/Mohamed.Yousuf/Downloads/seeded security role-RPT_userwith-role.xlsx')
import streamlit as st

# Page selection
page = st.sidebar.selectbox("Select Instance", ("PROD", "Dev26", "Dev7")) 

if page == "PROD":
    st.header("PROD")
    # Content for Page 1

elif page == "Dev26":
    st.header("Dev26")
    df = pd.read_excel('C:/Users/Mohamed.Yousuf/Downloads/seeded security role-RPT_userwith-role.xlsx') ###test
    #df = load_data()
    selected_role = st.selectbox('Select a role', df['ROLE_NAME'].unique())
    filtered_df = df[df['ROLE_NAME'] == selected_role]
    st.table(filtered_df[['USERNAME', 'ROLE_NAME']])
    #New Dashboard
    # Count the number of users for each role
    role_counts = df['ROLE_NAME'].value_counts()

    # Create a colorful bar chart using Plotly Express
    fig = px.bar(role_counts, x=role_counts.index, y=role_counts.values, color=role_counts.index)
    fig.update_layout(xaxis_title="Role", yaxis_title="Number of Users", showlegend=False)

    # Display the chart
    st.plotly_chart(fig)
    #####One more########
    sns.countplot(x='ROLE_NAME', data=df, palette='bright')

    # Customize the chart
    plt.xlabel("Role")
    plt.ylabel("Number of Users")
    plt.title("Role Distribution")

    # Display the chart
    st.pyplot(plt)

elif page == "Dev7":
    st.header("Dev7")
    # Content for Page 3





#def load_data():
    # Replace 'data.xlsx' with the path to your Excel file

    #print
 #   return df



''''
# Read the Excel file into a Pandas DataFrame
df = pd.read_excel('C:/Users/Mohamed.Yousuf/Downloads/seeded security role-RPT_userwith-role.xlsx')


#def main():
st.title('User Role Dashboard')

# Display the DataFrame as a table
st.write('## User Role Data')
st.write(df)

# Display a bar chart
st.write('## User Role Distribution (Bar Chart)')
role_counts = df['ROLE_NAME'].value_counts()
fig_bar = plt.figure()
plt.bar(role_counts.index, role_counts.values)
plt.xlabel('Role name')
plt.ylabel('Count')
st.pyplot(fig_bar)

# Display a pie chart
st.write('## User Role Distribution (Pie Chart)')
#fig_pie = px.pie(df, names='ROLE_NAME')
fig_pie = px.pie(df,names ='USERNAME')
st.plotly_chart(fig_pie)
# Display a bar chart
    st.write('## User Role Distribution (Bar Chart)')
    role_counts = df['ROLE_NAME'].value_counts()
    fig_bar = plt.figure()
    plt.bar(role_counts.index, role_counts.values)
    plt.xlabel('Role name')
    plt.ylabel('Count')
    st.pyplot(fig_bar)

    # Content for Page 2

'''
