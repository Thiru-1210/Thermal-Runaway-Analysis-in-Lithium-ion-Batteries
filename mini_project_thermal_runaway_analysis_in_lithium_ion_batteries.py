# -*- coding: utf-8 -*-
"""Mini project - Thermal Runaway Analysis in Lithium-Ion batteries

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v3uw2U45F9IcoE6AdXos-10fQE0lg7BA
"""

!pip install pybamm

# High Discharge
import pybamm
import numpy as np
import matplotlib.pyplot as plt

options = {"thermal": "lumped"}
model = pybamm.lithium_ion.SPM(options=options)
parameter_values = pybamm.ParameterValues("Chen2020")

I = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
fig, ax = plt.subplots(2, 1, figsize=(6, 12))

for current in I:
        experiment = pybamm.Experiment(
            [
                f"Discharge at {current}C until 2.5V",
                "Rest for 1 hour",
                "Charge at 1C until 4.2V",
                "Hold at 4.2V until C/50"
            ],
            period="10 seconds"
        )
        sim = pybamm.Simulation(model, experiment=experiment, parameter_values=parameter_values)
        solution = sim.solve()

        ax[0].plot(solution["Time [s]"].entries, solution["Terminal voltage [V]"].entries, label=f'{current}C')
        ax[1].plot(solution["Time [s]"].entries, solution["X-averaged cell temperature [K]"].entries - 273.15, label=f'{current}C')

ax[0].set_xlabel('Time [s]')
ax[0].set_ylabel('Voltage [V]')
ax[0].legend()

ax[1].set_xlabel('Time [s]')
ax[1].set_ylabel('Cell Temperature [C]')
ax[1].legend()

plt.tight_layout()
plt.show()

#High Ambient temperature
import pybamm
import numpy as np
import matplotlib.pyplot as plt

options = {"thermal": "lumped"}
model = pybamm.lithium_ion.SPM(options=options)
parameter_values = pybamm.ParameterValues("Chen2020")

# Set the initial temperature to 50°C
parameter_values.update({"Initial temperature [K]": 313.15})

I = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]

fig, ax = plt.subplots(2, 1, figsize=(6, 12))

for current in I:
    experiment = pybamm.Experiment(
        [f"Discharge at {current}C until 2.5V",
         "Rest for 1 hour",
         "Charge at 1C until 4.2V",
         "Hold at 4.2V until C/50"],
        period="10 seconds"
    )

    sim = pybamm.Simulation(model, experiment=experiment, parameter_values=parameter_values)
    solution = sim.solve()

    ax[0].plot(solution["Time [s]"].entries, solution["Terminal voltage [V]"].entries, label=f'{current}C')
    ax[1].plot(solution["Time [s]"].entries, solution["X-averaged cell temperature [K]"].entries - 273.15, label=f'{current}C')

ax[0].set_xlabel('Time [s]')
ax[0].set_ylabel('Voltage [V]')
ax[0].legend()

ax[1].set_xlabel('Time [s]')
ax[1].set_ylabel('Cell Temperature [C]')
ax[1].legend()

plt.tight_layout()
plt.show()

# Heat generation rate
import pybamm
import numpy as np
import matplotlib.pyplot as plt

options = {"thermal": "lumped"}
model = pybamm.lithium_ion.SPM(options=options)
parameter_values = pybamm.ParameterValues("Chen2020")

I = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]

fig, ax = plt.subplots(2, 1, figsize=(6, 12))

for current in I:
    experiment = pybamm.Experiment(
        [
            f"Discharge at {current}C until 2.5V",
            "Rest for 1 hour",
            "Charge at 1C until 4.2V",
            "Hold at 4.2V until C/50"
        ],
        period="10 seconds"
    )

    sim = pybamm.Simulation(model, experiment=experiment, parameter_values=parameter_values)
    solution = sim.solve()

    ax[0].plot(solution["Time [s]"].entries, solution["X-averaged cell temperature [K]"].entries - 273.15, label=f'{current}C')
    ax[1].plot(solution["Time [s]"].entries, solution["Volume-averaged total heating [W.m-3]"].entries, label=f'{current}C')

ax[0].set_xlabel('Time [s]')
ax[0].set_ylabel('Cell Temperature [C]')
ax[0].legend()

ax[1].set_xlabel('Time [s]')
ax[1].set_ylabel('Heat Generation Rate [W/m³]')
ax[1].legend()

plt.tight_layout()
plt.show()