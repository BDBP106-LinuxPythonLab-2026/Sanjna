#Write a function protein_energy_temp() with an inner function
#calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H − T ∆S. Use
#random or user-input ∆H, ∆S and return stability (”stable’ if ∆G < 0).

def protein_energy_temp(h, t, s):
    def calculate_free_energy(h, s):
        return h-(t*s)
    gibbs_energy = calculate_free_energy(h, s)
    if gibbs_energy<0: print(f"Gibbs free energy is {gibbs_energy} joules and thus it is stable.")
    else: print(f"Gibbs free energy is {gibbs_energy} joules and thus it is unstable.")

protein_energy_temp(int(input("Enter change in enthalpy: ")), int(input("Enter temperature in Kelvin: ")), int(input("Enter change in entropy: ")))