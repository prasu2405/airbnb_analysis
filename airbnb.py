import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns',None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


# Streamlit part

st.set_page_config(layout= "wide")
st.title("AIRBNB DATA ANALYSIS")
st.write("")


def datafr():
    air=pd.read_csv("D:/capstone project guvi/airbnb/airbnb.csv") 
    return air

air= datafr()

with st.sidebar:
    select= option_menu("Main Menu", ["Home", "Data Exploration", "About"])

if select == "Home":
        
    image1= Image.open("D:/capstone project guvi/airbnb/airbnb images.png")
    st.image(image1)

    st.header("About Airbnb")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    st.write("")
    st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***''')
    
    st.header("Background of Airbnb")
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')
    

if select == "Data Exploration":
        tab1, tab2, tab3, tab4, tab5= st.tabs(["***PRICE ANALYSIS***","***AVAILABILITY ANALYSIS***","***LOCATION BASED***", "***GEOSPATIAL VISUALIZATION***", "***TOP CHARTS***"])
        with tab1:
            st.title("**PRICE DIFFERENCE**")
            col1,col2= st.columns(2)

            with col1:
                        
                country= st.selectbox("Select the Country",air["country"].unique())

                air1= air[air["country"] == country]
                air1.reset_index(drop= True, inplace= True)  

                room_type= st.selectbox("Select the Room Type",air1["room_type"].unique())
                
                air2=air1[air1["room_type"] == room_type]
                air2.reset_index(drop= True, inplace= True)

                air_bar= pd.DataFrame(air2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
                air_bar.reset_index(inplace= True)

                fig_bar= px.bar(air_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY_TYPES",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
                st.plotly_chart(fig_bar)

            with col2:
            
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
        
                proper_type= st.selectbox("Select the Property_type",air2["property_type"].unique())

                air4= air2[air2["property_type"] == proper_type]
                air4.reset_index(drop= True, inplace= True)

                air_pie= pd.DataFrame(air4.groupby("host_response_time")[["price","bedrooms"]].sum())
                air_pie.reset_index(inplace= True)

                fig_pi= px.pie(air_pie, values="price", names= "host_response_time",
                                hover_data=["bedrooms"],
                                color_discrete_sequence=px.colors.sequential.BuPu_r,
                                title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                                width= 600, height= 500)
                st.plotly_chart(fig_pi)

            col1,col2= st.columns(2)

            with col1:

            
                hostresponsetime= st.selectbox("Select the host_response_time",air4["host_response_time"].unique())

                df5= air4[air4["host_response_time"] == hostresponsetime]

                df_do_bar= pd.DataFrame(df5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
                df_do_bar.reset_index(inplace= True)

                fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
                title='MINIMUM NIGHTS AND MAXIMUM NIGHTS',hover_data="price",
                barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow, width=600, height=500)
                

                st.plotly_chart(fig_do_bar)

            with col2:

                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")

                df_do_bar_2= pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
                df_do_bar_2.reset_index(inplace= True)

                fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
                title='BEDROOMS AND BEDS ACCOMMODATES',hover_data="price",
                barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r, width= 600, height= 500)
            
                st.plotly_chart(fig_do_bar_2)

        with tab2:

            def datafr():
                air_a= pd.read_csv("D:/capstone project guvi/airbnb/airbnb.csv")
                return air_a

            air_a= datafr()

            st.title("**AVAILABILITY ANALYSIS**")
            col1,col2= st.columns(2)

            with col1:
            
            
                country_a= st.selectbox("Select the Country_a",air_a["country"].unique())

                air1_a= air[air["country"] == country_a]
                air1_a.reset_index(drop= True, inplace= True)

                property_type_a= st.selectbox("Select the Property Type",air1_a["property_type"].unique())
                
                air2_a= air1_a[air1_a["property_type"] == property_type_a]
                air2_a.reset_index(drop= True, inplace= True)

                air_a_sunb_30= px.sunburst(air2_a, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=600,height=500,title="Availability_30",color_discrete_sequence=px.colors.sequential.Peach_r)
                st.plotly_chart(air_a_sunb_30)
            
            with col2:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                

                air_a_sunb_60= px.sunburst(air2_a, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=600,height=500,title="Availability_60",color_discrete_sequence=px.colors.sequential.Blues_r)
                st.plotly_chart(air_a_sunb_60)

            col1,col2= st.columns(2)

            with col1:
            
                air_a_sunb_90= px.sunburst(air2_a, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=600,height=500,title="Availability_90",color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
                st.plotly_chart(air_a_sunb_90)

            with col2:

                air_a_sunb_365= px.sunburst(air2_a, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=600,height=500,title="Availability_365",color_discrete_sequence=px.colors.sequential.Greens_r)
                st.plotly_chart(air_a_sunb_365)
        
            roomtype_a= st.selectbox("Select the Room Type_a", air2_a["room_type"].unique())

            df3_a= air2_a[air2_a["room_type"] == roomtype_a]

            df_mul_bar_a= pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
            df_mul_bar_a.reset_index(inplace= True)

            fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
            title='AVAILABILITY BASED ON HOST RESPONSE TIME',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)

            st.plotly_chart(fig_df_mul_bar_a)


        with tab3:

            st.title("LOCATION ANALYSIS")
            st.write("")

            def datafr():
                air= pd.read_csv("D:/capstone project guvi/airbnb/airbnb.csv")
                return air

            airl= datafr()

            country_l= st.selectbox("Select the Country_l",airl["country"].unique())

            air1_l= airl[airl["country"] == country_l]
            air1_l.reset_index(drop= True, inplace= True)

            proper_type_l= st.selectbox("Select the Property_type_l",air1_l["property_type"].unique())

            air2_l= air1_l[air1_l["property_type"] == proper_type_l]
            air2_l.reset_index(drop= True, inplace= True)

            st.write("")

            def select_the_air(sel_val):
                if sel_val == str(air2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + air2_l['price'].min())+' '+str("(30% of the Value)"):

                    air_val_30= air2_l[air2_l["price"] <= differ_max_min*0.30 + air2_l['price'].min()]
                    air_val_30.reset_index(drop= True, inplace= True)
                    return air_val_30

                elif sel_val == str(differ_max_min*0.30 + air2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + air2_l['price'].min())+' '+str("(30% to 60% of the Value)"):
                
                    air_val_60= air2_l[air2_l["price"] >= differ_max_min*0.30 + air2_l['price'].min()]
                    air_val_60_1= air_val_60[air_val_60["price"] <= differ_max_min*0.60 + air2_l['price'].min()]
                    air_val_60_1.reset_index(drop= True, inplace= True)
                    return air_val_60_1
                
                elif sel_val == str(differ_max_min*0.60 + air2_l['price'].min())+' '+str('to')+' '+str(air2_l['price'].max())+' '+str("(60% to 100% of the Value)"):

                    air_val_100= air2_l[air2_l["price"] >= differ_max_min*0.60 + air2_l['price'].min()]
                    air_val_100.reset_index(drop= True, inplace= True)
                    return air_val_100
                
            differ_max_min= air2_l['price'].max()-air2_l['price'].min()

            val_sel= st.radio("Select the Price Range",[str(air2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + air2_l['price'].min())+' '+str("(30% of the Value)"),
                                                        
                                                        str(differ_max_min*0.30 + air2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + air2_l['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                        str(differ_max_min*0.60 + air2_l['price'].min())+' '+str('to')+' '+str(air2_l['price'].max())+' '+str("(60% to 100% of the Value)")])
                                            
            air_val_sel= select_the_air(val_sel)

            st.dataframe(air_val_sel)



        # checking the correlation 

            air_val_sel_corr= air_val_sel.drop(columns=["listing_url","name", "property_type",                 
                                            "room_type", "bed_type","cancellation_policy",
                                            "images","host_url","host_name", "host_location",                   
                                            "host_response_time", "host_thumbnail_url",            
                                            "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                            "host_picture_url","host_neighbourhood",
                                            "host_identity_verified","host_verifications",
                                            "street", "suburb", "government_area", "market",                        
                                            "country", "country_code","location_type","is_location_exact",
                                            "amenities"]).corr()

            st.dataframe(air_val_sel_corr)

            air_val_sel_gr= pd.DataFrame(air_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
            air_val_sel_gr.reset_index(inplace= True)

            fig_1= px.bar(air_val_sel_gr, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], title="ACCOMMODATES",
                        hover_data= "extra_people", barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
            st.plotly_chart(fig_1)
            
            
            room_ty_l= st.selectbox("Select the Room_Type_l", air_val_sel["room_type"].unique())

            air_val_sel_rt= air_val_sel[air_val_sel["room_type"] == room_ty_l]

            fig_2= px.bar(air_val_sel_rt, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
                        hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
            st.plotly_chart(fig_2)

            fig_3= px.bar(air_val_sel_rt, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
                        hover_data= ["guests_included","location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
            st.plotly_chart(fig_3)


        with tab4:

            st.title("GEOSPATIAL VISUALIZATION")
            st.write("")

            fig_4 = px.scatter_mapbox(air, lat='latitude', lon='longitude', color='price', size='accommodates',
                            color_continuous_scale= "rainbow",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                            zoom=1)
            fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
            st.plotly_chart(fig_4)   


        with tab5:

                country_t= st.selectbox("Select the Country_t",air["country"].unique())

                air1_t= air[air["country"] == country_t]

                property_ty_t= st.selectbox("Select the Property_type_t",air1_t["property_type"].unique())

                air2_t= air1_t[air1_t["property_type"] == property_ty_t]
                air2_t.reset_index(drop= True, inplace= True)

                air2_t_sorted= air2_t.sort_values(by="price")
                air2_t_sorted.reset_index(drop= True, inplace= True)


                air_price= pd.DataFrame(air2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
                air_price.reset_index(inplace= True)
                air_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
                
                col1, col2= st.columns(2)
                
                with col1:
            
                    fig_price= px.bar(air_price, x= "Total_price", y= "host_neighbourhood", orientation='h',
                                    title= "PRICE BASED ON HOST_NEIGHBOURHOOD", width= 600, height= 800)
                    st.plotly_chart(fig_price)

                with col2:

                    fig_price_2= px.bar(air_price, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                                        title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",width= 600, height= 800)
                    st.plotly_chart(fig_price_2)

        col1, col2= st.columns(2)

        with col1:

            air_price_1= pd.DataFrame(air2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
            air_price_1.reset_index(inplace= True)
            air_price_1.columns= ["host_location", "Total_price", "Avarage_price"]
            
            fig_price_3= px.bar(air_price_1, x= "Total_price", y= "host_location", orientation='h',
                                width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_3)

        with col2:

            fig_price_4= px.bar(air_price_1, x= "Avarage_price", y= "host_location", orientation='h',
                                width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "AVERAGE PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_4)


        room_type_t= st.selectbox("Select the Room_Type_t",air2_t_sorted["room_type"].unique())

        air3_t= air2_t_sorted[air2_t_sorted["room_type"] == room_type_t]

        air3_t_sorted_price= air3_t.sort_values(by= "price")

        air3_t_sorted_price.reset_index(drop= True, inplace = True)

        air3_top_50_price= air3_t_sorted_price.head(100)

        fig_top_50_price_1= px.bar(air3_top_50_price, x= "name",  y= "price" ,color= "price",
                                 color_continuous_scale= "rainbow",
                                range_color=(0,air3_top_50_price["price"].max()),
                                title= "MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES",
                                width=1200, height= 800,
                                hover_data= ["minimum_nights","maximum_nights","accommodates"])
        
        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2= px.bar(air3_top_50_price, x= "name",  y= "price",color= "price",
                                 color_continuous_scale= "greens",
                                 title= "BEDROOMS, BEDS, ACCOMMODATES AND BED_TYPE",
                                range_color=(0,air3_top_50_price["price"].max()),
                                width=1200, height= 800,
                                hover_data= ["accommodates","bedrooms","beds","bed_type"])

        st.plotly_chart(fig_top_50_price_2)

if select == "About":

        st.header("ABOUT THIS PROJECT")

        st.subheader(":orange[1. Data Collection:]")

        st.write('''***Gather data from Airbnb's public API or other available sources.
            Collect information on listings, hosts, reviews, pricing, and location data.***''')
        
        st.subheader(":orange[2. Data Cleaning and Preprocessing:]")

        st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
            Convert data types, handle duplicates, and standardize formats.***''')
        
        st.subheader(":orange[3. Exploratory Data Analysis (EDA):]")

        st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data.
            Explore relationships between variables and identify potential insights.***''')
        
        st.subheader(":orange[4. Visualization:]")

        st.write('''***Create visualizations to represent key metrics and trends.
            Use charts, graphs, and maps to convey information effectively.
            Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''')
        
        st.subheader(":orange[5. Geospatial Analysis:]")

        st.write('''***Utilize geospatial analysis to understand the geographical distribution of listings.
            Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.***''')






        


        








