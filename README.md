# Simple Trip Planning Agent
A basic trip planning agent which plans your trip by allocating your budget for transport, food, and accommodation and suggests options accordingly. 

<h2>Features</h2>
<ul>
  <li>Inputs user's choice of the following from the Gradio UI
  <ol>
    <li>Source city</li>
    <li>Destination City</li>
    <li>Food preference</li>
    <li>Transport preference</li>
    <li>Budget</li>
    <li>Number of days</li>
  </ol>
  </li>
  <li>The agent chooses these inputs to
    <ol>
      <li>Allocate the budget for transport, food and stay</li>
      <li>Suggest transport options based on transport.json</li>
      <li>Suggest hotel options based on hotels.json</li>
      <li>Suggest food options based on food.josn</li>
      <li>The LLM returns a textual response</li>
    </ol>
    </li>
  <li>The response is displayed in the UI</li>
</ul>

<h2>How to run the code</h2>
<ol>
  <li>Clone this repository</li>
  <li>Install requirements using pip install requirements.txt</li>
  <li>Create and use your OpenAI API key and paste it on agent_PMT.py where LLM is created</li>
  <li>Run the code agent_ui.py</li>
  <li>You will get a link to host the UI</li>
  <li>Open the link in browser by doing ctrl+click</li>
  <li>Choose your trip details and click on "Plan Trip"</li>
  <li>The response will be generated, but it will take about 2 minutes (I want to improve that, but don't know how. Would streaming work?)</li>
</ol>

<h2>Sample Input and Output</h2>
<h4>Input</h4>
<img width="1880" height="859" alt="Screenshot 2025-12-29 190634" src="https://github.com/user-attachments/assets/a368e697-0518-43a4-bf69-46d2387a7f36" />

<h4>Output</h4>
<img width="1861" height="700" alt="Screenshot 2025-12-29 201226" src="https://github.com/user-attachments/assets/e5e7803d-d003-4008-9597-69570d6d8724" />

<img width="1870" height="688" alt="Screenshot 2025-12-29 201457" src="https://github.com/user-attachments/assets/5506a8c2-4703-42dc-ac97-68753302455f" />


