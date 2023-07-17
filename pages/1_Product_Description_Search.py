import streamlit as st
# import util.util as util 

# langchain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import VertexAI
from util.util import sidebar

import json
# init
def init():
    # First, let's load the language model we're going to use to control the agent.
    llm = VertexAI(temperature=0.2)

    # Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
    # tools = load_tools(["google-search", "llm-math"], llm=llm)
    tools = load_tools(["google-search"], llm=llm)
    # Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
    # agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        return_intermediate_steps=True,
        max_iterations=20,
        max_token_limit=1024
    )
    return agent


sidebar('product_description')
agent = init()
example_prompt = ''' In this task, you will be an expert content creator for products in a grocery store. You are also able to classify if some of the ingredients contains Pork, Lard, which our musilm friends may not like 
                
Your task is then to extract the information in a JSON format for it to be passed to another system, hence the formatting rules for each of the fields listed below needs to be followed very strictly. In the case of the prompt, you should be search on Google to figure these inputs. 
The required fields to be used as the JSON keys are as follows:
1. is_halal	- Yes if it doesnt contain Pork or is not halal or No based on if it contains Pork, Pig ,Lard and if not sure give Not sure.
2. is_organic - check the ingredient list to see if its organic  , if not sure give Not sure.
3. is_vegeterian - check the ingredient list to see if its contains any kind of meat or animal oils  , if not sure give Not sure. 
Create a Product description for following product here: {product}   
Only generate the json output, don't generate any fillers           
'''
st.header('Find a product description')
product_name = st.text_input('Enter a product, e.g. Heinz Baked Beans Original or Braised Yee Fu Noodles')
if len(product_name) != 0:
    # st.subheader('Enter a prompt in the text area below to get started. for e.g')
    st.write('Enter a prompt in the text area below')
    st.write('A sample prompt has been pre filled in the text box below based on the product entered')
    prompt = st.text_area(label='Enter prompt', value=example_prompt.format(product=product_name),height=460, max_chars=10000)
    print('-'+prompt+'-')
    print('-'+product_name+'-')

    if st.button('Submit') and len(prompt) != 0:
        print('submitted...')
        # st.write('Prompt Entered: \n'+prompt)
        status_placeholder = st.empty()

        status_placeholder.write('Processing.... please wait')
        st.divider()
        try:
            res = agent(prompt)
            print(type(res))
            print(res)
            print(res.keys())
            # st.write(res["intermediate_steps"])
            st.write('Output:')
            status_placeholder.write('Done.... Please refer to the output below')

        except Exception as inst:
            print('Got Exception*************')
            print(type(inst))
            print(inst.args)
            print(inst)
            status_placeholder.write('there is an error running this, please retry')
        else:   
        #st.write(type(res["output"]))
            st.write(res["output"])
        # st.write(res["intermediate_steps"])

        #st.write(res)

        print('**************************')
        #print(res["intermediate_steps"])
        #print(res["output"])

    #st.write(res)
