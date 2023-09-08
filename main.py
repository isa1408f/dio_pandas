import pandas as pd
import matplotlib.pyplot as plt

tab = pd.read_excel("Salvador.xlsx")

tab["Total"] = tab["Vendas"].mul(tab["Qtde"])

print(tab)
print("----------------------------")
print("Total Vendas: %.2f" % (tab["Total"].sum()))
print("Media Vendas: %.2f" % (tab["Total"].mean()))
print("Desvio Padrão Vendas: %.2f" % (tab["Total"].std()))
print("----------------------------")
plt.plot(tab['Data'], tab['Total'])