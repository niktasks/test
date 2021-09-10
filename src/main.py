# Databricks notebook source
# MAGIC %run ./module_1

# COMMAND ----------

#%% IMPORTS
try:
    from module_1 import iwas
except ModuleNotFoundError:
    try:
        get_ipython()
    except NameError:
        print("Module import failed")

#%% PROGRAM
x = numpy.ones((5,))
print(x)

y = []
for i in range(5):
    y.append(iwas(i))

print(y)

# COMMAND ----------

# Just something to commit