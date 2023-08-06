import imp
import matan as mt
force= [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
elongation = [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19]
exp= mt.sample("EXP-90pPET-10prPET")
comp_dict=exp.composition_from_name()
for key in comp_dict:
    print(key, comp_dict[key][0])
