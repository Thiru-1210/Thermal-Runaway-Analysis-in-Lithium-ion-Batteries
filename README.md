# Thermal-Runaway-Analysis-in-Lithium-ion-Batteries


I am excited to share the results of my recent project on thermal runaway analysis in lithium-ion batteries. Using the Python Battery Mathematical Modelling software (PyBaMM), I simulated various conditions that can lead to thermal runaway, a critical safety concern in lithium-ion batteries. I used the LG INR21700 M50 lithium-ion battery and the Single Particle Model (SPM) for the simulations.

Project Overview:
High Discharge Rate:
I simulated a high discharge rate scenario, a common condition that can lead to thermal runaway. The results showed how the battery’s voltage and temperature responded to this high load condition.

High Ambient Temperature:
I also simulated a high ambient temperature scenario. High temperatures can accelerate the electrochemical reactions in a battery, leading to increased heat generation and potentially thermal runaway.

Heat Generation Rate:
To understand the heat dynamics within the battery, I plotted the heat generation rate over time. This plot revealed how much heat was being generated within the battery at different times, which is a key factor in thermal runaway.

Key Results:
Voltage Response:
The first image shows the voltage response of the battery under different discharge rates. It highlights how discharge rates higher than 2C can cause the battery to exceed its safety limits.

Temperature Rise:
The second image illustrates the temperature rise when the ambient temperature is set at 25°C. It demonstrates that a 6C discharge rate can cause the battery temperature to reach 65°C if the ambient temperature is not properly maintained.

Heat Generation Rate:
The third image depicts the heat generation rate, showing a high spike at the beginning due to the high load current, followed by stabilization.

Conclusion:
By analyzing these simulations, I gained valuable insights into the conditions that can lead to thermal runaway. This understanding can help in developing strategies to prevent thermal runaway and improve the safety of lithium-ion batteries.

Future Work:
It is very exciting and engaging to work with batteries, and I look forward to applying these insights to real-world problems and contributing to the development of safer and more reliable battery technologies.

Installation:
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/thermal-runaway-analysis.git
cd thermal-runaway-analysis
Set up the virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the simulation:

bash
Copy code
python thermal_runaway_analysis.py
View the results:

The simulation will generate plots showing voltage, temperature, and heat generation rate over time for different discharge rates and ambient temperatures.

Contributions
Contributions are welcome! Please submit a pull request or open an issue to discuss potential improvements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Special thanks to the PyBaMM development team for providing a powerful and flexible tool for battery modeling.
