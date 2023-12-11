import requests 
import streamlit as st
from streamlit_lottie import st_lottie

# Find more imojis here: https://www.webfx.com/tools/emoji-cheat-sheet/ 
st.set_page_config(page_title="Mine Only", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
   r = requests.get(url)
   if r.status_code != 200:\
        return None
   return r.json()
# ---- LOAD ASSETS ----
lottie_coding =  load_lottieurl("https://lottie.host/b3c4efbf-3c67-42b2-ba03-e6e5da2afac5/jXNg2IN9E7.json")
lottie_coding2 = load_lottieurl("https://lottie.host/bc0f39f3-1b10-4569-994f-f867a93306b6/CtcvNKuyXj.json")

# ----HEADER SECTION----
with st.container():  
    st.subheader("Hi, I am Algen Marc a BSCPE student :wave:")
    st.title("SIARGAO")
    st.write("I am here to show you the beauty of SIARGAO.")

# ---- WHAT TO KNOW ----
with st.container():
   st.write("---")
   left_column, right_column = st.columns(2)
   with left_column:
      st.header("What To Know")
      st.write("##")
      st.write(
         """ 
         ABOUT;\n
         - CULTURE & FOOD
         - TOP EVENTS & FESTIVALS
         THINGS YOU CAN DO IN SIARGAO;\n
         - SURFING
         - SUNRISE AND SUNSETS
         - ISLAND HOPPING
         - SUGBA LAGOON
         - CLIFF JUMPING
         - TAYANGBAN CAVE POOLS
         - TAKTAK WATERFALL
         - BUCAS GRANDE’S LAGOON
         - PACIFICO BEACH
         - LOCAL COMMUNITY MARKET 
         """
      )
   with right_column:
      st_lottie(lottie_coding, height=300, key="coding")
      st_lottie(lottie_coding2, height=500, key="coding2")




# ---- ABOUT ----
with st.container():
   st.write("---")
   st.header("ABOUT")
   st.write("Culture & Food")
   st.write("- Attracting adventurous travellers from around the world many on a tight budget – Siargao has an eclectic dining scene embracing international cooking, vegan and other healthy cuisine, and local recipes with or without a modern twist. Filipino favourites not to miss include the seafood boodle fight at Daku Island and the unique surfboard-shaped bread, Pan de Surf.  Siargao has a lively nightlife scene focused on different bars on different nights of the week, so chatting to locals is the best way to find out where to head. Regular venues include Bravo, RumBar, Viento and the Jungle Shack.Another way to get to know locals is through their love of karaoke, both in their own homes and in dedicated bars.")
   st.write("##")
   st.write("Top Events & Festivals")
   st.write(
            """
            - Siargao International Game Fishing Tournament – April.
            - Siargao International Marathon – July.
            - Siargao International Surfing Cup – September.
            - Part of General Luna’s yearly fiesta – the island’s biggest, with two weeks of parades, parties, live bands and discos.
            - Other fiestas include Dapa in January, San Benito in March, San Isidro in May, Socorro in June, Del Carmen and Burgus in July, Santa Monica in August, Pilar in October.
            """
   )

# ---- THINGS YOU CAN DO IN SIARGAO ----
with st.container():
   st.write("---")
   st.header("THINGS YOU CAN DO IN SIARGAO")
   st.write("SURFING")
   st.write("- Grab a board. For beginners, there’s Jacking Horse with its many surf schools; for pros, the thick, hollow ‘barrels’ at Cloud 9 have earnt it a place among the world’s top 10 waves.")
   st.write("SUNRISE AND SUNSETS")
   st.write("- Alternatively, admire the action – and watch the sun rise or set, or stargaze – from Cloud 9 boardwalk with its viewing area")
   st.write("ISLAND HOPPING")
   st.write("- Go island-hopping to Guyam, Daku and Naked Island.")
   st.write("SUGBA LAGOON")   
   st.write("- Head for mountain-rimmed Sugba Lagoon, where you’ll find a floating hut with a diving board plus SUP paddleboard and wooden raft hire.")
   st.write("CLIFF JUMPING")
   st.write("- Go cliff jumping and explore the caves and coves of Magpupungko Rock Pools, or try the Tarzan Jump on the Maasin River. Stop by the Maasin viewpoint to see the incredible sight of the island’s coconut plantation.")
   st.write("TAYANGBAN CAVE POOLS")
   st.write("- Go caving at Tayangban Cave Pools, swimming and floating by torchlight while bats flit around you.")
   st.write("TAKTAK WATERFALL")
   st.write("- Journey to Taktak Waterfall, for more cliff jumping, tree jumping and exploring, and to see the sun set from Santa Monica Pier or bask in the sun at the Alegria whitesand beach.")
   st.write("BUCAS GRANDE’S LAGOON")
   st.write("- Explore Bucas Grande’s lagoon with non-sting jellyfish, and do sea kayaking or cliff diving. Enjoy the water bungalow resorts in the island.")
   st.write("PACIFICO BEACH")
   st.write("- Get off the beaten track at pristine Pacifico Beach with its small surf-town feel and a sprinkling of resorts and homestays. On Sundays, join in with beach clean-ups in aid of disadvantaged children.")
   st.write("LOCAL COMMUNITY MARKET")
   st.write("- Shop at LOKAL Tabo, a community market where local farmers and artisans sell their produce and crafts.")




