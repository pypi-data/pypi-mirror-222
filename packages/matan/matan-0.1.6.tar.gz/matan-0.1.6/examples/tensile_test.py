import imp
import matan as mt


force= [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
elongation = [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19]


exp= mt.sample("EXP-90pPET-10prPET")


# Initialize tensile test method to insert the tensile test forces and elongation
thickness=10
width=10
exp.define_tensile_test(thickness,width,elongation,force)

print("Engineering values")

print(f"Strain at break {exp.tensile.engineering_values.at_break.strain} {exp.tensile.strain_units}")
print(f"Stress at break {exp.tensile.engineering_values.at_break.stress} {exp.tensile.stress_units}")
print(f"Yield Stress  {exp.tensile.engineering_values.yield_strength.stress} {exp.tensile.stress_units}")
print(f"Yield strain  {exp.tensile.engineering_values.yield_strength.strain} {exp.tensile.strain_units}")
print(f"Strength stress  {exp.tensile.engineering_values.strength.value} {exp.tensile.stress_units}")
print(f"Strength strain  {exp.tensile.engineering_values.strength.strain} {exp.tensile.strain_units}")
print(f"Tensile modulus {exp.tensile.engineering_values.tensile_modulus} {exp.tensile.stress_units}")

# Plot the engineering values plot, but do not show the plot
exp.tensile.engineering_values.plot(show=False)

exp.tensile.convert2real()
print("Real values")

print(f"Strain at break {exp.tensile.real_values.at_break.strain} {exp.tensile.strain_units}")
print(f"Stress at break {exp.tensile.real_values.at_break.stress} {exp.tensile.stress_units}")
print(f"Yield Stress  {exp.tensile.real_values.yield_strength.stress} {exp.tensile.stress_units}")
print(f"Yield strain  {exp.tensile.real_values.yield_strength.strain} {exp.tensile.strain_units}")
print(f"Strength stress  {exp.tensile.real_values.strength.value} {exp.tensile.stress_units}")
print(f"Strength strain  {exp.tensile.real_values.strength.strain} {exp.tensile.strain_units}")
print(f"Tensile modulus {exp.tensile.real_values.tensile_modulus} {exp.tensile.stress_units}")
# Plot the engineering values plot, and show both of the plots
exp.tensile.real_values.plot(True)
