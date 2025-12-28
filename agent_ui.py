import gradio as gr
import agent_PMT

source_cities = ["Delhi", "Kolkata", "Chennai", "Bengaluru", "Hyderabad", "Mumbai"]
destination_cities = ["Chennai", "Chandigarh", "Delhi", "Kolkata", "Pune", "Bengaluru", "Mumbai"]

with gr.Blocks() as demo:
    gr.Markdown("## Travel Planner Agent")

    source = gr.Dropdown(source_cities, label="Source city")
    destination = gr.Dropdown(destination_cities, label="Destination city")
    food = gr.Dropdown(["veg", "any"], label="Food preference")
    transport = gr.Dropdown(["train", "flight", "any"], label="Transport preference")
    budget = gr.Number(label="Budget")
    days = gr.Slider(1, 30, step=1, label="Number of days")

    output = gr.Textbox(label="Trip Plan")

    plan_button = gr.Button("Plan Trip")

    plan_button.click(
        fn=agent_PMT.plan_trip,
        inputs=[source, destination, food, transport, budget, days],
        outputs=output
    )

demo.launch(share=True)




