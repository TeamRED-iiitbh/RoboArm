# Stepper Motor Calculator

This program calculates various parameters for different stepper motors based on their specifications. The program uses formulas derived from stepper motor theory to compute average power, maximum power, speed, and minimum delay. The motor specifications and results are then printed in a formatted string for easy readability.

## Formulas

1. **Power:**
   - $P_{\text{avg}} = \frac{2}{3} \times I_{\text{rated}} V_{\text{rated}}$
   - $V_{\text{max}} = \sqrt{L} \times 32$
   - $P_{\text{max}} = 1.2 \times I_{\text{rated}} V_{\text{max}}$

2. **Speed:**
   - $\text{Speed (rpm)} = \frac{V_{\text{rated}} \times 60}{2 \times L \times I_{\text{rated}} \times \text{spr}}$

3. **Minimum Delay:**
   - $\text{Delay (s)} = \frac{2 \times L \times I_{\text{rated}}}{V_{\text{rated}}}$

## Circuit Diagram

![Circuit Diagram](path/to/your/circuit_diagram.png)

## Motor Specifications

| # | Motor Model   | Qty. | 🛒                                                                                                    | 📄                                                                                  | 📏                                                                                                                |
|---|---------------|------|------------------------------------------------------------------------------------------------------  |-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| 1 | NEMA23_31_D   | 1    | [🛒](https://robu.in/product/neema-23-jk57hs112-4204-3-1n-m-d-type/)                                  | [📄](https://www.steppermotorcanada.ca/57hs112-4204-03.pdf)                         | -                                                                                                                 |
| 2 | NEMA23_18.9_D | 2    | [🛒](https://www.robu.in/product/57hs76-2804-05-nema23-18-9-kg-cm-hybrid-stepper-motor-d-type-shaft/) | [📄](https://ecksteinimg.de/Datasheet/Schrittmotor/JK57HS76-2804/JK57HS76-2804.pdf) | [📏](https://robu.in/wp-content/uploads/2015/12/NEMA-23-18.9-kg-cm-Hybrid-Stepper-Motor-ROBU.IN_.gif)             |
| 3 | NEMA17_7.2_R  | 2    | [🛒](https://robu.in/product/neema-17-jk42hs60-1704-0-72n-m-round-type/)                              | [📄](https://robu.in/wp-content/uploads/2023/07/1551713.pdf)                        | -                                                                                                                 |
| 4 | NEMA17_6.5_D  | 2    | [🛒](https://robu.in/product/neema-17-jk42hs60-1206-0-65n-m-d-type/)                                  | [📄](https://robu.in/wp-content/uploads/2022/03/datasheet.pdf)                      | -                                                                                                                 |
| 5 | NEMA17_4.8_D  | 2    | [🛒](https://robu.in/product/nema17-4-8-kg-cm-stepper-motor-with-detachable-72-cm-cable/)             | [📄](https://robu.in/wp-content/uploads/2023/04/JK42HS48-2504AF-01.pdf)             | [📏](https://robu.in/wp-content/uploads/2018/08/NEMA-17-Stepper-Motor-4.8-kg-cm-Dimensional-Drawing-ROBU.IN_.jpg) |

## References

* [GeckoDrive - Power Supply Basics](https://www.geckodrive.com/support/power-supply-basics/)
* [All About Circuits - Stepper Motor Calculator](https://www.allaboutcircuits.com/tools/stepper-motor-calculator/)
