#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path
print(Path.cwd())


# In[2]:


import pandas as pd

df = pd.read_csv("/home/david/thesis/data/processed/cr/ams02_proton_daily.csv")
df.head()


# In[3]:


print(df.columns.tolist())


# In[4]:


print(df.shape)


# In[5]:


df.info()


# In[6]:


df = pd.read_csv("/home/david/thesis/data/cr/core/ams02_proton_daily.csv")
df.head()


# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

df = pd.read_csv("/home/david/thesis/data/processed/cr/ams02_proton_daily.csv")
df["date"] = pd.to_datetime(df["date"])

df["rigidity_mid_GV"] = 0.5 * (df["rigidity_min_GV"] + df["rigidity_max_GV"])
df["sigma_tot"] = np.sqrt(df["err_stat"]**2 + df["err_time"]**2 + df["err_sys"]**2)

df.head()


# In[8]:


summary = (
    df.groupby(["rigidity_min_GV", "rigidity_max_GV", "rigidity_mid_GV"])
      .agg(
          N=("flux", "size"),
          mean_flux=("flux", "mean"),
          min_flux=("flux", "min"),
          max_flux=("flux", "max"),
          std_flux=("flux", "std"),
          mean_sigma_tot=("sigma_tot", "mean")
      )
      .reset_index()
      .sort_values("rigidity_mid_GV")
)

summary["A"] = (summary["max_flux"] - summary["min_flux"]) / summary["mean_flux"]
summary["A_p"] = (
    df.groupby(["rigidity_min_GV", "rigidity_max_GV", "rigidity_mid_GV"])["flux"]
      .apply(lambda x: (np.percentile(x, 95) - np.percentile(x, 5)) / x.mean())
      .values
)
summary["A_rms"] = (
    df.groupby(["rigidity_min_GV", "rigidity_max_GV", "rigidity_mid_GV"])["flux"]
      .apply(lambda x: x.std(ddof=1) / x.mean())
      .values
)

summary.head(10)


# In[9]:


rho_A, p_A = spearmanr(summary["rigidity_mid_GV"], summary["A"])
rho_Ap, p_Ap = spearmanr(summary["rigidity_mid_GV"], summary["A_p"])
rho_Arms, p_Arms = spearmanr(summary["rigidity_mid_GV"], summary["A_rms"])

print("Spearman rho for A     =", rho_A, " p =", p_A)
print("Spearman rho for A_p   =", rho_Ap, " p =", p_Ap)
print("Spearman rho for A_rms =", rho_Arms, " p =", p_Arms)


# In[10]:


plt.figure(figsize=(8, 5))
plt.plot(summary["rigidity_mid_GV"], summary["A"], marker="o", label="A = (Jmax - Jmin) / <J>")
plt.plot(summary["rigidity_mid_GV"], summary["A_p"], marker="s", label="A_p = (P95 - P5) / <J>")
plt.plot(summary["rigidity_mid_GV"], summary["A_rms"], marker="^", label="A_rms = sigma(J) / <J>")

plt.xscale("log")
plt.xlabel("Rigidity (GV)")
plt.ylabel("Amplitude")
plt.title("Rigidity dependence of AMS-02 proton time variability")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()


# In[11]:


summary.to_csv("/home/david/thesis/outputs/tables/ams02_rigidity_dependence_summary.csv", index=False)

plt.figure(figsize=(8, 5))
plt.plot(summary["rigidity_mid_GV"], summary["A"], marker="o", label="A")
plt.plot(summary["rigidity_mid_GV"], summary["A_p"], marker="s", label="A_p")
plt.plot(summary["rigidity_mid_GV"], summary["A_rms"], marker="^", label="A_rms")
plt.xscale("log")
plt.xlabel("Rigidity (GV)")
plt.ylabel("Amplitude")
plt.title("Rigidity dependence of AMS-02 proton time variability")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("/home/david/thesis/figures/ams02_rigidity_dependence_A.png", dpi=300, bbox_inches="tight")
plt.show()


# In[12]:


paper_table = summary[[
    "rigidity_min_GV", "rigidity_max_GV", "rigidity_mid_GV",
    "N", "A", "A_p", "A_rms"
]].copy()

paper_table.head(15)


# In[ ]:




