import numpy as np 


# Science 

def NusseltNumber(ReynodNumber,PrandtlNumber,L,D):
    return 1.86*(ReynodNumber*PrandtlNumber/(L/D))**1.5 

def SheerwoodNumber(ReynodNumber,ShmidtNumber):
    return 0.023*ReynodNumber**0.83*ShmidtNumber**0.33

def h_heat(length_channel,equivalent_diameter,themal_conductivity,ReynodNumber,PrandtlNumber):
    return NusseltNumber(ReynodNumber,PrandtlNumber,length_channel,equivalent_diameter)*themal_conductivity/length_channel

def h_mass(ReynodNumber,ShmidtNumber,length_channel,themal_conductivity):
    return SheerwoodNumber(ReynodNumber,ShmidtNumber)*themal_conductivity/length_channel



# Initial Condition

temp_inlet_dry = 35
absHumidity_inlet_dry = 0.024
temp_productAir = 35
temp_water = 20


# Geometrical Parameters 

height = 0.05
length = 0.5
width = 0.005

# Simulation Parameters

steps = 100
convergence = 0.001

# Looping function to simulate the value

'''
    Mass flow rate : m 
    Specific Heat Capacity : c
    Absoulte Humidity : w
    enthalpy of vaporisation : iv


    Assumptions :
    1. Temperature of water is maintained using a thermocouple implies (temperature of water remains same)
    2. 
'''


def update_temperature_product():
    return ( h_heat*dx*b*(T_productAir - T_water) + m_productAir*c_productAir*T_productAir )/ ( m_productAir*c_productAir ) 

def update_temperature_workingAir_dry():
    return ( h_heat*dx*b*(T_workingAir_dry - T_water) + m_workingAir_dry*c_productAir*T_workingAir_dry  ) / ( m_workingAir_dry*c_productAir )

def update_absoluteHumidity_workingAir_wet():
    return ( h_mass*dx*b*(w_saturated_wet - w_workingAir_wet) + m_workingAir_wet*w_workingAir_wet  ) / ( m_workingAir_wet )

def update_temperature_workingAir_wet():
    return ( h_heat*dx*b*(T_water-T_workingAir_wet) + h_mass*(dx)*b*iv*(w_saturated_wet - w_workingAir_wet) + T_workingAir_wet*m_workingAir_dry*c_productAir) / (m_workingAir_dry*c_productAir)

def update_massFlowRate_workingAir_wet():
    dT = 
    return -1. * (m_productAir*c_productAir*dT + m_workingAir_wet*iv*(w_saturated_wet - w_workingAir_wet + c_water*m_water*T_water)) / (c_water*T_water)

def waitForConvergence(convergence_factor,function,*argvs):
    values = 
    while(convergence_factor >= waitForConvergence(convergence_factor,function,))

# Simulations 

# TODO: make a matrix to solve the equation and the use the internal loop for calculating the value of the values

dx = length_channel/steps 
T_productAir_simulations = []
T_workingAir_dry_simulations = []

for n in range(steps):

    update_temperature_product()
    



