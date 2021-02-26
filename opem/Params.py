# -*- coding: utf-8 -*-
"""OPEM parameters."""
Version = 1.2
Website = "http://www.ecsim.ir/opem"
UpdateUrl = "http://www.ecsim.ir/opem/update"
Overview = '''
Modeling and simulation of proton-exchange membrane fuel cells (PEMFC) may work as a
powerful tool in the research & development of renewable energy sources. The Open-Source
PEMFC Simulation Tool (OPEM) is a modeling tool for evaluating the performance of proton
exchange membrane fuel cells. This package is a combination of models (static/dynamic)
that predict the optimum operating parameters of PEMFC. OPEM contained generic models that
will accept as input, not only values of the operating variables such as anode and cathode
feed gas, pressure and compositions, cell temperature and current density, but also cell
parameters including the active area and membrane thickness. In addition, some of the different
models of PEMFC that have been proposed in the OPEM, just focus on one particular FC stack,
and some others take into account a part or all auxiliaries such as reformers. OPEM is
a platform for collaborative development of PEMFC models.'''

Links = '''
Website : http://www.ecsim.ir/opem
Repository : https://github.com/ECSIM/opem
Document : http://www.ecsim.ir/opem/doc/
Paper : https://doi.org/10.21105/joss.00676
* If you use OPEM in your research, please cite our paper
* OPEM GUI is available here : https://github.com/ECSIM/gopem
'''
Warning_Message_1 = "Warning : The value of I(>{}) leads to minus amount of V, please check your inputs"
Warning_Message_2 = "Warning : There are errors in the simulations in some of I amounts; please refer to the .opem file" \
    " for review. If you are confident about this parameters, ignore this warning."
Report_Message = "Report is generating ..."
HHV = 1.482
uF = 0.95
n = 8 * (10 ** -3)
m = 3 * (10 ** -5)
xi1 = -0.948
xi3 = 7.6 * (10 ** -5)
xi4 = -1.93 * (10 ** -4)
# F=96500
# R1=8.314
R = 8314.47
F = 96484600
Eth = 1.23
Amphlett_InputParams = {
    "T": "Cell operation temperature [K]",
    "PH2": "Partial pressure [atm]",
    "PO2": "Partial pressure [atm]",
    "i-start": "Cell operating current start point [A]",
    "i-step": "Cell operating current step",
    "i-stop": "Cell operating current end point [A]",
    "A": "Active area [cm^2]",
    "l": "Membrane thickness [cm]",
    "lambda": "An adjustable parameter with a min value of 14 and max value of 23",
    "N": "Number of single cells",
    "R": "R-Electronic [ohm] (*Optional)",
    "JMax": "Maximum current density [A/(cm^2)]"}
Amphlett_OutputParams = {
    "Enernst": "V",
    "Eta Activation": "V",
    "Eta Ohmic": "V",
    "Eta Concentration": "V",
    "Loss": "V",
    "Vcell": "V",
    "PEM Efficiency": "",
    "Power": "W",
    "VStack": "V",
    "Power-Stack": "W",
    "Power-Thermal": "W"}

Amphlett_Params_Default = {"R": 0}

Amphlett_Description = '''
Amphlett static model is a parametric model that predicting the performance of a solid polymer electrolyte,
proton exchange membrane (PEM) fuel cell. Main concepts in the Amphlett model includes Nernst voltage, PEMFC losses
(activation polarization loss, ohmic polarization loss and concentration polarization loss), power and efficiency
of fuel cell. This parametric model of PEMFC using a combination of mechanistic and empirical approach. The ideal
standard potential (Nernst potential) of an H2/O2 FC is 1.229 V with liquid water product. The actual cell potential
is decreased from its reference potential because of irreversible losses.
'''

Amphlett_Standard_Vector = {
    "T": 343.15,
    "PH2": 1,
    "PO2": 1,
    "i-start": 0,
    "i-stop": 75,
    "i-step": 0.1,
    "A": 50.6,
    "l": 0.0178,
    "lambda": 23,
    "N": 1,
    "R": 0,
    "JMax": 1.5,
    "Name": "Amphlett_Test"}
Larminiee_InputParams = {
    "T": "Cell operation temperature [K]",
    "E0": "Fuel cell reversible no loss voltage [V]",
    "i-start": "Cell operating current start point [A]",
    "i-step": "Cell operating current step",
    "i-stop": "Cell operating current end point [A]",
    "RM": "The membrane and contact resistances [ohm]",
    "i_n": "Internal current [A]",
    "i_0": "Exchange current at which the overvoltage begins to move from zero [A]",
    "i_L": "Limiting current [A]",
    "A": "The slope of the Tafel line [V]",
    "N": "Number of single cells"}
Larminiee_OutputParams = {
    "Vcell": "V",
    "PEM Efficiency": "",
    "Power": "W",
    "VStack": "V",
    "Power-Stack": "W",
    "Power-Thermal": "W"}

Larminiee_Description = '''
Larminie-Dicks model is obtained for large variation of the load parameters. In this model, the fuel cell is represented
by means of its voltage-current characteristic obtained in static operating mode. In fact, Larminie-Dicks static model
presents the fuel cell voltage as a function of the current magnitude. The obtained polarization curve is composed of
three main regions corresponding to the predominance of electrochemical activation phenomena (region I), a linear
part (region II) where the voltage drop is mainly due to electronic and ionic internal resistances and the last
region where the diffusion kinetics of gases through the electrodes becomes the limiting factor (region III). This
last zone is characterized by a rapid voltage fall.
'''

Larminiee_Standard_Vector = {
    "A": 0.06,
    "E0": 1.178,
    "T": 328.15,
    "RM": 0.0018,
    "i_0": 0.00654,
    "i_L": 100.0,
    "i_n": 0.23,
    "N": 23,
    "i-start": 0.1,
    "i-stop": 98,
    "i-step": 0.1,
    "Name": "Larminiee_Test"}
Chamberline_InputParams = {
    "E0": "Open circuit voltage [V]",
    "b": "Tafel's parameter for the oxygen reduction [V]",
    "R": "Resistance [ohm.cm^2]",
    "m": "Diffusion's parameters [V] (*Optional)",
    "n": "Diffusion's parameters [(A^-1)(cm^2)] (*Optional)",
    "i-start": "Cell operating current start point [A]",
    "i-step": "Cell operating current step",
    "i-stop": "Cell operating current end point [A]",
    "A": "Active area [cm^2]",
    "N": "Number of single cells"}
Chamberline_OutputParams = {
    "Vcell": "V",
    "PEM Efficiency": "",
    "Power": "W",
    "VStack": "V",
    "Power-Stack": "W",
    "Power-Thermal": "W"}

Chamberline_Params_Default = {"m": 3 * (10 ** -8),"n":8}

Chamberline_Description = '''
Chamberlin-Kim static model is an empirical equation which was developed to fit the experimental cell potential (E) vs.
current density (J) data for proton exchange membrane fuel cells (PEMFCs), at several temperatures, pressures, and
oxygen compositions in the cathode gas mixture. The exponential term compensates for the mass-transport regions of the
V vs. i plot; i.e., the increase in slope of the pseudolinear region and the subsequent rapid fall-off of the cell
potential with increasing current density. The terms E0 and b yield the electrode kinetic parameters for oxygen
reduction in the PEMFC and R represents the resistance, predominantly ohmic and, to a small extent, the charge
transfer resistance of the electro-oxidation of hydrogen. The exponential term characterizes the mass-transport
region of the V vs. i plot. The parameter n has more pronounced effects than the parameter m in this region. In
Chamberline Kim's model, the values of the parameters(five parameters: E0, b, R, m, n) vary depending on many
variables, including the composition of the Membrane Electrode Assemblies(MEA), the fuel and oxidant used, besides
the local temperature, pressure, and humidity of the MEA. They also depend on the stack itself, so that it can not
be transposed to another fuel cell without new parameter identification.
'''
Chamberline_Standard_Vector = {
    "A": 50.0,
    "E0": 0.982,
    "b": 0.0689,
    "R": 0.328,
    "m": 0.000125,
    "n": 9.45,
    "N": 1,
    "i-start": 1,
    "i-stop": 42.5,
    "i-step": 0.1,
    "Name": "Chamberline_Test"}

Padulles_InputParams = {
    "N0": "Number of cells",
    "E0": "No load voltage [V]",
    "T": "Fuel cell temperature [K]",
    "KH2": "Hydrogen valve constant [kmol.s^(-1).atm^(-1)]",
    "KO2": "Oxygen valve constant [kmol.s^(-1).atm^(-1)]",
    "tH2": "Hydrogen time constant [s]",
    "tO2": "Oxygen time constant [s]",
    "qH2": "Molar flow of hydrogen [kmol.s^(-1)]",
    "rho": "Hydrogen-Oxygen flow rate",
    "Rint": "Fuel cell internal resistance [ohm]",
    "B": "Activation voltage constant [V]",
    "C": "Activation constant parameter [A^(-1)]",
    "i-start": "Cell operating current start point [A]",
    "i-step": "Cell operating current step",
    "i-stop": "Cell operating current end point [A]"}

Padulles_Outparams = {
    "FC Voltage": "V",
    "FC Power": "W",
    "FC Efficiency": "",
    "PO2": "atm",
    "PH2": "atm",
    "E": "V",
    "Power-Thermal": "W"}


Padulles_Description = '''
In this model, Nernst and fuel cell potential were modeled as a function of oxygen and hydrogen gases partial pressure
that can be calculated from independent variables or constants. The partial pressure of gases is proportional to
the molar flow of each gas.
'''

Padulles_Standard_Vector = {
    "T": 343,
    "E0": 0.6,
    "N0": 88,
    "KO2": 0.0000211,
    "KH2": 0.0000422,
    "tH2": 3.37,
    "tO2": 6.74,
    "B": 0.04777,
    "C": 0.0136,
    "Rint": 0.00303,
    "rho": 1.168,
    "qH2": 0.0004,
    "i-start": 0,
    "i-stop": 100,
    "i-step": 0.1,
    "Name": "PadullesI_Test"}
Padulles2_InputParams = {
    "N0": "Number of cells",
    "E0": "No load voltage [V]",
    "T": "Fuel cell temperature [K]",
    "KH2": "Hydrogen valve constant [kmol.s^(-1).atm^(-1)]",
    "KO2": "Oxygen valve constant [kmol.s^(-1).atm^(-1)]",
    "tH2": "Hydrogen time constant [s]",
    "tO2": "Oxygen time constant [s]",
    "qH2": "Molar flow of hydrogen [kmol.s^(-1)]",
    "rho": "Hydrogen-Oxygen flow rate",
    "Rint": "Fuel cell internal resistance [ohm]",
    "B": "Activation voltage constant [V]",
    "C": "Activation constant parameter [A^(-1)]",
    "i-start": "Cell operating current start point [A]",
    "i-step": "Cell operating current step",
    "i-stop": "Cell operating current end point [A]",
    "KH2O": "Water Valve Constant [kmol.s^(-1).atm^(-1)]",
    "tH2O": "Water time constant [s]"}
Padulles2_Outparams = {
    "FC Voltage": "V",
    "FC Power": "W",
    "FC Efficiency": "",
    "PO2": "atm",
    "PH2": "atm",
    "PH2O": "atm",
    "E": "V",
    "Power-Thermal": "W"}

Padulles2_Description = '''
In this model, Nernst and fuel cell potential were modeled as a function of water, oxygen and hydrogen gases partial
pressure that can be calculated from independent variables or constants. The partial pressure of gases is proportional
to the molar flow of each gas.
'''
Padulles2_Standard_Vector = {
    "T": 343,
    "E0": 0.6,
    "N0": 5,
    "KO2": 0.0000211,
    "KH2": 0.0000422,
    "KH2O": 0.000007716,
    "tH2": 3.37,
    "tO2": 6.74,
    "tH2O": 18.418,
    "B": 0.04777,
    "C": 0.0136,
    "Rint": 0.00303,
    "rho": 1.168,
    "qH2": 0.0004,
    "i-start": 0.1,
    "i-stop": 100,
    "i-step": 0.1,
    "Name": "Padulles2_Test"}
Padulles_Hauer_InputParams = {
    "N0": "Number of cells",
    "E0": "No load voltage [V]",
    "T": "Fuel cell temperature [K]",
    "KH2": "Hydrogen valve constant [kmol.s^(-1).atm^(-1)]",
    "KO2": "Oxygen valve constant [kmol.s^(-1).atm^(-1)]",
    "tH2": "Hydrogen time constant [s]",
    "tO2": "Oxygen time constant [s]",
    "t1": "Reformer time constant [s]",
    "t2": "Reformer time constant [s]",
    "rho": "Hydrogen-Oxygen flow rate",
    "Rint": "Fuel cell internal resistance [ohm]",
    "B": "Activation voltage constant [V]",
    "C": "Activation constant parameter [A^(-1)]",
    "i-start": "Cell operating current start point [A]",
    "i-step": "Cell operating current step",
    "i-stop": "Cell operating current end point [A]",
    "KH2O": "Water valve constant [kmol.s^(-1).atm^(-1)]",
    "tH2O": "Water time constant [s]",
    "qMethanol": "Molar flow of methanol [kmol.s^(-1)]",
    "CV": "Conversion factor"}
Padulles_Hauer_Outparams = {
    "FC Voltage": "V",
    "FC Power": "W",
    "FC Efficiency": "",
    "PO2": "atm",
    "PH2": "atm",
    "PH2O": "atm",
    "E": "V",
    "Power-Thermal": "W"}

Padulles_Hauer_Description = '''
Padulles-Hauer Dynamic Model is a dynamic electrochemical simulation model of a grid independent proton exchange
membrane (PEM) fuel cell. This model includes a methanol reformer to generate hydrogen from methanol and the PEM stack.
The model is used to predict the output voltage and power of a PEMFC. It has to be noted that the reformer model is a
second order transfer function.
'''
Padulles_Hauer_Standard_Vector = {
    "T": 343,
    "E0": 0.6,
    "N0": 5,
    "KO2": 0.0000211,
    "KH2": 0.0000422,
    "KH2O": 0.000007716,
    "tH2": 3.37,
    "tO2": 6.74,
    "t1": 2,
    "t2": 2,
    "tH2O": 18.418,
    "B": 0.04777,
    "C": 0.0136,
    "Rint": 0.00303,
    "rho": 1.168,
    "qMethanol": 0.0002,
    "CV": 2,
    "i-start": 0.1,
    "i-stop": 100,
    "i-step": 0.1,
    "Name": "Padulles_Hauer_Test"}
Padulles_Amphlett_Params_Default = {"R": 0, "E0": 1.229}

Padulles_Amphlett_InputParams = {
    "N0": "Number of cells",
    "E0": "No load voltage [V], Default Value:" + str(
        Padulles_Amphlett_Params_Default["E0"]),
    "T": "Fuel cell temperature [K]",
    "KH2": "Hydrogen valve constant [kmol.s^(-1).atm^(-1)]",
    "KO2": "Oxygen valve constant [kmol.s^(-1).atm^(-1)]",
    "tH2": "Hydrogen time constant [s]",
    "tO2": "Oxygen time constant [s]",
    "t1": "Reformer time constant [s]",
    "t2": "Reformer time constant [s]",
    "rho": "Hydrogen-Oxygen flow rate",
    "R": "R-Electronic [ohm] (*Optional)",
    "i-start": "Cell operating current start point [A]",
    "i-step": "Cell operating current step",
    "i-stop": "Cell operating current end point [A]",
    "KH2O": "Water valve constant [kmol.s^(-1).atm^(-1)]",
    "tH2O": "Water time constant [s]",
    "qMethanol": "Molar flow of methanol [kmol.s^(-1)]",
    "CV": "Conversion factor",
    "A": "Active area [cm^2]",
    "l": "Membrane thickness [cm]",
    "lambda": "An adjustable parameter with a min value of 14 and max value of 23",
    "JMax": "Maximum current density [A/(cm^2)]"}

Padulles_Amphlett_Outparams = {
    "FC Voltage": "V",
    "FC Power": "W",
    "FC Efficiency": "",
    "PO2": "atm",
    "PH2": "atm",
    "PH2O": "atm",
    "E": "V",
    "Eta Activation": "V",
    "Eta Ohmic": "V",
    "Eta Concentration": "V",
    "Loss": "V",
    "Power-Thermal": "W"}

Padulles_Amphlett_Description = '''
This model is an integration of Padulles-Hauer dynamic model with Amphlett static model. The advantage of this dynamic
model is using Amphlett equation for simulating the polarization values. Amphlett model as the most complicated and
preferable static model, but the most precise. Based on this model, the obtained polarization voltage is identical to
the experimental results.
'''
Padulles_Amphlett_Standard_Vector = {
    "A": 50.6,
    "l": 0.0178,
    "lambda": 23,
    "JMax": 1.5,
    "T": 343,
    "N0": 5,
    "KO2": 0.0000211,
    "KH2": 0.0000422,
    "KH2O": 0.000007716,
    "tH2": 3.37,
    "tO2": 6.74,
    "t1": 2,
    "t2": 2,
    "tH2O": 18.418,
    "rho": 1.168,
    "qMethanol": 0.0002,
    "CV": 2,
    "i-start": 0.1,
    "i-stop": 75,
    "i-step": 0.1,
    "Name": "Padulles_Amphlett_Test"}

Chakraborty_Params_Default = {"R": 0, "E0": 0.6}

Chakraborty_InputParams = {
    "N0": "Number of cells",
    "u": "Fuel utilization  ratio",
    "E0": "No load voltage [V], Default Value:" + str(
        Chakraborty_Params_Default["E0"]),
    "T": "Fuel cell temperature [K]",
    "KH2": "Hydrogen valve constant [kmol.s^(-1).atm^(-1)]",
    "KO2": "Oxygen valve constant [kmol.s^(-1).atm^(-1)]",
    "rho": "Hydrogen-Oxygen flow rate",
    "PO2": "Oxygen partial pressure [atm]",
    "PH2": "Hydrogen partial pressure [atm]",
    "PH2O": "Water partial pressure [atm]",
    "R": "Internal  ohmic  resistance [ohm] (*Optional)",
    "i-start": "Cell operating current start point [A]",
    "i-step": "Cell operating current step",
    "i-stop": "Cell operating current end point [A]",
    "KH2O": "Water valve constant [kmol.s^(-1).atm^(-1)]"}

Chakraborty_Outparams = {
    "FC Voltage": "V",
    "FC Power": "W",
    "FC Efficiency": "",
    "PO2": "atm",
    "PH2": "atm",
    "PH2O": "atm",
    "E": "V",
    "Power-Thermal": "W"}

Chakraborty_Description = '''
The new dynamic model is presented based on constant fuel utilization control (constant stoichiometry condition).
The model solves the long-standing problem of mixing reversible and irreversible potentials (equilibrium and non-equilibrium states)
in the Nernst voltage expression. Specifically, a Nernstian gain term is introduced for the constant fuel utilization condition, and
it is shown that the Nernstian gain is an irreversibility in the computation of the output voltage of the fuel cell.
'''

Chakraborty_Standard_Vector = {
    "T": 1273,
    "E0": 0.6,
    "u":0.8,
    "N0": 2,
    "R": 3.28125 * 10**(-4),
    "KH2O": 0.000281,
    "KH2": 0.000843,
    "KO2": 0.00252,
    "rho": 1.145,
    "i-start": 0.1,
    "i-stop": 50,
    "i-step": 0.1,
    "Name": "Chakraborty_Test"}

General_Padulles_Description = '''
The Padulles dynamic model can predict the transient response of cell voltage, temperature of the cell, hydrogen/oxygen
out flow rates and cathode and anode channel temperatures/pressures under sudden change in load current. Hence, a
dynamic fuel cell simulation is developed in this model, which incorporates the dynamics of flow and pressure in the
anode and cathode channels and mass/ heat transfer transient features in the fuel cell body. This model based on some
assumption such; the gases are ideal, the stack is fed with hydrogen and air, temperature is stable at all times, the
ratio of pressures between the interior and exterior of the channel is large, The channels that transport gases along
the electrodes have a fixed volume, only source of losses is ohmic and Nernst equation can be applied too.
'''

Description_Menu = {
    "Amphlett_Analysis (Static)": Amphlett_Description,
    "Larminiee_Analysis (Static)": Larminiee_Description,
    "Chamberline_Kim_Analysis (Static)": Chamberline_Description,
    "Padulles_Analysis I (Dynamic)": Padulles_Description,
    "Padulles_Analysis II (Dynamic)": Padulles2_Description,
    "Padulles_Hauer Analysis (Dynamic)": Padulles_Hauer_Description,
    "Padulles_Amphlett Analysis (Dynamic)": Padulles_Amphlett_Description,
    "Chakraborty_Analysis (Dynamic)": Chakraborty_Description,
    "General Padulles": General_Padulles_Description,
    "Overview": Overview,
    "Links": Links}

Mode_Menu = "\n\n[M]: More information\n\n[T]: Run standard test vector\n\n[P]: Enter your parameters (*default)\n\nPlease select a mode : "

Description_Links = {
    "Amphlett_Analysis (Static)": "http://www.ecsim.ir/opem/doc/Static/Amphlett.html",
    "Larminiee_Analysis (Static)": "http://www.ecsim.ir/opem/doc/Static/Larminie_Dicks.html",
    "Chamberline_Kim_Analysis (Static)": "http://www.ecsim.ir/opem/doc/Static/Chamberline_Kim.html",
    "Padulles_Analysis I (Dynamic)": "http://www.ecsim.ir/opem/doc/Dynamic/Padulles1.html",
    "Padulles_Analysis II (Dynamic)": "http://www.ecsim.ir/opem/doc/Dynamic/Padulles2.html",
    "Padulles_Hauer Analysis (Dynamic)": "http://www.ecsim.ir/opem/doc/Dynamic/Padulles_Hauer.html",
    "Padulles_Amphlett Analysis (Dynamic)": "http://www.ecsim.ir/opem/doc/Dynamic/Padulles_Amphlett.html",
    "Chakraborty_Analysis (Dynamic)": "http://www.ecsim.ir/opem/doc/Dynamic/Chakraborty.html"}
Vectors = {
    "Amphlett_Analysis (Static)": Amphlett_Standard_Vector,
    "Larminiee_Analysis (Static)": Larminiee_Standard_Vector,
    "Chamberline_Kim_Analysis (Static)": Chamberline_Standard_Vector,
    "Padulles_Analysis I (Dynamic)": Padulles_Standard_Vector,
    "Padulles_Analysis II (Dynamic)": Padulles2_Standard_Vector,
    "Padulles_Hauer Analysis (Dynamic)": Padulles_Hauer_Standard_Vector,
    "Padulles_Amphlett Analysis (Dynamic)": Padulles_Amphlett_Standard_Vector,
    "Chakraborty_Analysis (Dynamic)": Chakraborty_Standard_Vector}

Overall_Params_Max_Description = {
    "Pmax": "Maximum power [W]",
    "VFC|Pmax": "Cell voltage at maximum power [V]",
    "Efficiency|Pmax": "Cell efficiency at maximum power",
    "Ptotal(Elec)": "Total electrical power [W]",
    "Ptotal(Thermal)": "Total thermal power [W]"}
Overall_Params_Linear_Description = {
    "V0": "Intercept of the curve obtained by linear approximation [V]",
    "K": "Slope of the curve obtained by linear approximation [A^(-1)]",
    "Pmax(L-Approx)": "Maximum power obtained by linear approximation [W]",
    "VFC|Pmax(L-Approx)": "Cell voltage at maximum power obtained by linear approximation [V]",
}


Test_List = ['test_Amphlett.py', 'test_Chamberline_Kim.py', 'test_Functions.py', 'test_Larminie_Dicks.py', 'test_Padulles1.py', 'test_Padulles2.py', 'test_Padulles_Amphlett.py', 'test_Padulles_Hauer.py']
