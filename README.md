# solar-viability-calculator
A simple analytical tool to evaluate solar energy economic viability
# Solar Viability Calculator

This project provides a simple and general computational tool to evaluate the economic viability of residential photovoltaic systems. The model is based on a physical–economic formulation and allows users to estimate both individual and collective financial returns from solar energy adoption.

---

## 📌 Features

* Analytical computation of payback time
* Financial return for a user-defined time horizon
* Collective impact based on adoption rate
* Fully parameterized and adaptable to any region

---

## ⚙️ Inputs

The model requires the following inputs:

* System power (kW)
* Monthly solar irradiation (kWh/kW/month)
* System efficiency (0–1)
* Electricity tariff ($/kWh)
* Installation cost ($)
* Annual maintenance cost ($)
* Number of households
* Adoption rate (0–1)
* Time horizon (years)

---

## 📊 Outputs

The program computes:

* Payback time
* Individual financial return at a chosen time
* Total city-level financial return

All monetary values are expressed in generic currency units ($), allowing application in any country.

---

## ▶️ How to Use
Run the script:

main.py

And enter the requested parameters when prompted.

---

## 🧠 Model

The accumulated financial return is given by:

R(t) = 12t · S_m − C − t · C_m

where:

S_m = P · G_m · η · T

The payback time is obtained analytically as:

t_payback = C / (12S_m − C_m)

---

## 🌍 Applicability

This model is designed to be general and can be applied to any city by adjusting local parameters such as solar irradiation and electricity prices.

---

## 📄 Related Work

This code was developed as part of a research project on solar energy viability and its economic impact in small municipalities.

---

## 📜 License

This project is open-source and free to use for educational and research purposes.
