# Databricks notebook source
# MAGIC %run ./module_2

# COMMAND ----------

try:
    from module_2 import func
except ModuleNotFoundError:
    try:
        get_ipython()
    except NameError:
        print("Module import failed")

def iwas(x):
    return x + func(x)