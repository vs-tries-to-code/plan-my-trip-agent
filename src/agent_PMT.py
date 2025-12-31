#import necessary modules
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
import os
import json

#defining the base directory, to prevent FileNotFoundError 
BASE_DIR=os.path.dirname(os.path.abspath(__file__))

#Defining the required tools 
@tool("transport_suggestion")
def suggest_transport(destination, source , budget, mode="any"):
  """"Suggests transportation options according to the source and destination, and the allocated budget"""
  #loading data from transport.json file
  with open (os.path.join(BASE_DIR, "transport.json"), "r") as f:
    data=json.load(f)

  #finding train options under allocated budget
  options=[]
  if mode in ("train", "any"):
    for train in data["trains"]:
      if (train["source"]==source and train["destination"]==destination and train["price"]<=budget):

        options.append({
            "Mode": "train",
            "Source": train["source"],
            "Destination": train["destination"],
            "Price": train["price"],
            "Departure": train["departure"],
            "Arrival": train["arrival"],
        })

  #finding flight options under allocated budget
  if mode in ("flight", "any"):
    for flight in data["flights"]:
      if (
            flight["source"]==source and 
            flight["destination"]==destination and 
            flight["price"]<=budget):
        
        options.append({
            "mode": "flight",
            "Source": flight["source"],
            "Destination": flight["destination"],
            "Price": flight["price"],
            "Departure": flight["departure"],
            "Arrival": flight["arrival"],
        })

  return options

@tool("hotel_suggestion")
def suggest_hotel(city, budget, days):
  """
    Suggests hotels in the given city that fit within the allocated stay budget.
    """
  #loading data from hotels.json file
  with open (os.path.join(BASE_DIR,"hotels.json"), "r") as f:
    data=json.load(f)
  
  #finding hotel options under allocated budget
  options=[]
  for hotel in data["hotels"]:
    if (hotel["city"]==city and hotel["price_per_night"]*days<=budget):
      options.append(hotel)
  return options

@tool("food_suggestion")
def suggest_food(food_type, budget):
  """
    Suggests veg or mixed food plans within the allocated food budget.
    """
  #loading data from food.json file
  with open (os.path.join(BASE_DIR,"food.json"), "r") as f:
    data=json.load(f)
  
  #finding food options under allocated budget
  options=[]
  for food in data["food_plans"]:
    if (food["type"]==food_type and food["average_daily_cost"]<=budget):
      options.append(food)
  return options


@tool("Budget_allocation")
def allocate_budget(budget, travel_mode, food_pref):
  """
    Splits the total budget into transport, stay, and food based on preferences.
    """
  allocation = {}

  #base percentages
  transport_pct = 0.25
  stay_pct = 0.45
  food_pct = 0.30

  #adjustment based on choices
  if travel_mode == "flight":
      transport_pct += 0.10
      stay_pct -= 0.05
      food_pct -= 0.05

  if food_pref == "veg":
      food_pct -= 0.05
      stay_pct += 0.05

  #allocation of total budget
  total = transport_pct + stay_pct + food_pct
  allocation["transport"] = round(budget * transport_pct / total)
  allocation["stay"] = round(budget * stay_pct / total)
  allocation["food"] = round(budget * food_pct / total)

  return allocation

def plan_trip(source, destination, food, transport, budget, days):
  #if source==destination:
    #raise Exception("Source cannot be the same as destination")

  user_prompt=f"""You are a helpful, trip planning assisstant
                Plan a trip using the inputted details
                Source={source},
                Destination={destination},
                food preference= {food},
                transport preference = {transport},
                total budget={budget},
                number of days= {days} days

                
                Summarise and describe the outputs of the tools used in not more than 400 words.
                
                Explain the detailed reasoning especially if the budget or the number of days for the trip is insufficient.

                Use the tools to allocate the budget for transport, food and stay and suggest the optimal options accordingly.

                Do NOT hallucinate
                Do NOT synthesize data
                Explain with brevity
                
                """
  #invokation of the agent to provide output
  inputs = {"messages": [{"role": "user", "content": user_prompt}]}
  
  result = graph.invoke(inputs)

# pulling the very last message from the message history
  print(result["messages"][-1].content)
  return result["messages"][-1].content
  
  
#listing the tools required for the agent
tools=[suggest_transport, suggest_food, suggest_hotel, allocate_budget]

#setting the llm
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    #Add your API key here
    api_key=""
)

#creating the agent
graph=create_agent(model="gpt-4o-mini", tools=tools, system_prompt="You are a helpful trip planning agent")
