# Databricks notebook source
print("Hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello World from SQL"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Demo

# COMMAND ----------

# MAGIC %run ./include/setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

me = full_name
