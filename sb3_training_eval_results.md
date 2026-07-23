---
with:
hasTopic:
  - "[[SpecRLBench]]"
  - "[[PPO]]"
  - "[[Environment]]"
  - "[[RL]]"
  - "[[Simulation]]"
score:
Created:
  - "[[02-07-2026]]"
---
```bash
# Hyperparams
TOTAL_TIMESTEPS = 5_000_000
seed = 0
n_envs = 8
ent_coef = 0.01
n_steps = 4096  #512 Level0, 2048 Level4
batch_size = 256
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
_models/ppo_20260714_1540_PointLTL4MASAR1-v0_run9
=====================================================
Mean reward:        0.550 +/- 0.497
Rescue rate:        11/20 (55.0%)
s0-Vis rescue %:    11/18 (61.1%)
s0-Invis rescue %:  0/2 (0.0%)
Mean ep_len:        579.500 +/- 402.491
Mean reward:        0.550 +/- 0.497
=====================================================
# Hyperparams
# Note: Included addt'l sparse reward based on whether the casualty was seen or not (reward ∈ {0, 1, 2})
TOTAL_TIMESTEPS = 1_000_000
seed = 0
n_envs = 8
ent_coef = 0.02
learning_rate = 5e-5
n_steps = 2048  # 512 Level0, 2048 Level4
batch_size = 256
n_epochs = 10
clip_range = 0.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Mean reward:        1.560 +/- 0.779
Rescue rate:        37/50 (74.0%)
s0-Vis rescue %:    37/40 (92.5%)
s0-Invis rescue %:  0/10 (0.0%)
Mean ep_len:        499.520 +/- 353.966
Mean reward:        1.560 +/- 0.779
=====================================================
# Hyperparameters
# Note: Included addt'l sparse reward based on whether the casualty was seen or not (reward ∈ {0, 1, 2})
TOTAL_TIMESTEPS = 1_000_000
seed = 0
n_envs = 8
ent_coef = 0.02
learning_rate = 5e-5
n_steps = 2048  # 512 Level0, 2048 Level4
batch_size = 256
n_epochs = 10
clip_range = 0.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
_models/ppo_20260714_1623_PointLTL4MASAR1-v0_run9
Mean reward:        1.980 +/- 0.140
Rescue rate:        49/50 (98.0%)
s0-Vis rescue %:    38/39 (97.4%)
s0-Invis rescue %:  11/11 (100.0%)
Mean ep_len:        258.300 +/- 192.859
Mean reward:        1.980 +/- 0.140
-----------------------------------------------------
_models/ppo_20260714_1652_PointLTL4MASAR1-v0_run9
Mean reward:        1.560 +/- 0.753
Rescue rate:        36/50 (72.0%)
s0-Vis rescue %:    36/39 (92.3%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        433.420 +/- 373.808 
Mean reward:        1.560 +/- 0.753
=====================================================
# Note: These next two runs I was testing absolute reproducability, which is why they're identical
_models/ppo_20260714_2020_PointLTL4MASAR1-v0_run9
Mean reward:        1.180 +/- 0.477
Rescue rate:        11/50 (22.0%)
s0-Vis rescue %:    11/39 (28.2%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        851.840 +/- 287.426
Mean reward:        1.180 +/- 0.477
-----------------------------------------------------
_models/ppo_20260714_2029_PointLTL4MASAR1-v0_run9
Mean reward:        1.180 +/- 0.477
Rescue rate:        11/50 (22.0%)
s0-Vis rescue %:    11/39 (28.2%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        851.840 +/- 287.426
Mean reward:        1.180 +/- 0.477
=====================================================
# Hyperparams
TOTAL_TIMESTEPS = 1_000_000
seed = 0
n_envs = 8
ent_coef = 0.02
learning_rate = 5e-5
n_steps = 1024  # 512 Level0, 2048 Level4
batch_size = 128
n_epochs = 10
clip_range = 0.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
_models/ppo_20260714_2103_PointLTL4MASAR1-v0
# with visibility reward
Mean reward:        0.840 +/- 0.418
Rescue rate:        1/50 (2.0%)
s0-Vis rescue %:    1/39 (2.6%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        999.200 +/- 5.600
Mean reward:        0.840 +/- 0.418
-----------------------------------------------------
_models/ppo_20260714_2053_PointLTL4MASAR1-v0
# without visibility reward
Mean reward:        0.100 +/- 0.300
Rescue rate:        5/50 (10.0%)
s0-Vis rescue %:    5/39 (12.8%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        914.140 +/- 258.424
Mean reward:        0.100 +/- 0.300
-----------------------------------------------------
_models/ppo_20260714_2304_PointLTL4MASAR1-v0
# dense distance based reward shaping
Mean reward:        1.181 +/- 2.503
Rescue rate:        32/50 (64.0%)
s0-Vis rescue %:    27/39 (69.2%)
s0-Invis rescue %:  5/11 (45.5%)
Mean ep_len:        487.600 +/- 402.264
Mean reward:        1.181 +/- 2.503
```

# Seedhunting (reward ∈ {0, 1, 2})
```sh
# Seedhunting

_models/ppo_20260715_0729_PointLTL4MASAR1-v0 # Seed 0
----------------------------------------
Mean reward:        1.220 +/- 0.642
Rescue rate:        17/50 (34.0%)
s0-Vis rescue %:    17/39 (43.6%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        783.820 +/- 337.644 
Mean reward:        1.220 +/- 0.642

_models/ppo_20260715_0729_PointLTL4MASAR1-v0 # Seed 1
----------------------------------------
Mean reward:        1.020 +/- 0.140
Rescue rate:        1/50 (2.0%)
s0-Vis rescue %:    1/39 (2.6%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        982.460 +/- 122.780 
Mean reward:        1.020 +/- 0.140

_models/ppo_20260715_0729_PointLTL4MASAR1-v0 # Seed 2
----------------------------------------
Mean reward:        1.400 +/- 0.600
Rescue rate:        23/50 (46.0%)
s0-Vis rescue %:    18/39 (46.2%)
s0-Invis rescue %:  5/11 (45.5%)
Mean ep_len:        692.720 +/- 379.782 
Mean reward:        1.400 +/- 0.600

_models/ppo_20260715_0729_PointLTL4MASAR1-v0 # Seed 3
----------------------------------------
Mean reward:        1.040 +/- 0.564
Rescue rate:        9/50 (18.0%)
s0-Vis rescue %:    8/39 (20.5%)
s0-Invis rescue %:  1/11 (9.1%)
Mean ep_len:        845.980 +/- 330.296 
Mean reward:        1.040 +/- 0.564

_models/ppo_20260715_0832_PointLTL4MASAR1-v0 # Seed 4
----------------------------------------
Mean reward:        0.940 +/- 0.237
Rescue rate:        0/50 (0.0%)
s0-Vis rescue %:    0/39 (0.0%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        1000.000 +/- 0.000 
Mean reward:        0.940 +/- 0.237
```

# Entrapped Casualties (reward ∈ {0, 1})
```sh
# Note: Trained on building in the same location, but eval had buildings in random location (bug fixed after training)
_models/ppo_20260715_1124_PointLTL5MASAR1-v0_0
========================================
Mean reward:        1.000 +/- 0.200
Rescue rate:        49/50 (98.0%)
Mean ep_len:        262.340 +/- 133.052
# 20 obstacles
Mean reward:        0.900 +/- 0.361
Rescue rate:        44/50 (88.0%)
Mean ep_len:        424.780 +/- 250.803

_models/ppo_20260717_1419_PointLTL4MASAR1-v0_0
========================================
Mean reward:        0.960 +/- 0.196
Rescue rate:        48/50 (96.0%)
Mean ep_len:        209.420 +/- 194.717
```

# Multiple Buildings
```sh
# Disregard building lidar after it's been entered
_models/ppo_20260716_2118_PointLTL6MASAR1-v0_0
========================================
Mean reward:        1.630 +/- 0.508
Rescue rate:        46/50 (92.0%)
Mean ep_len:        664.380 +/- 656.094
```
# Wall Collision Tests
```sh
_models/ppo_20260715_1623_PointLTL5MASAR1-v0_0
# -1 reward for collision with wall
Mean reward:        0.680 +/- 0.614
Rescue rate:        41/50 (82.0%)
Mean ep_len:        370.940 +/- 297.217

_models/ppo_20260716_1342_PointLTL5MASAR1-v0_0
# Termination when hitting wall
========================================
Mean reward:        0.260 +/- 0.450
Rescue rate:        12/50 (24.0%)
Mean ep_len:        2003.820 +/- 896.217
--------------------------------
# Observation-based wall collisions
_models/ppo_20260716_2350_PointLTL5MASAR1-v0_0
========================================
Mean reward:        1.760 +/- 0.650
Rescue rate:        44/50 (88.0%)
Mean ep_len:        219.400 +/- 52.605
--------------------------------
_models/ppo_20260716_2350_PointLTL6MASAR1-v0_0
========================================
Mean reward:        0.780 +/- 0.708
Rescue rate:        18/50 (36.0%)
Mean ep_len:        892.300 +/- 979.976
```
## Gremlin-Based Collision Detection
```sh
_models/ppo_20260717_1312_PointLTL4MASAR1WC-v0_0
========================================
Mean reward:        0.920 +/- 0.271
Rescue rate:        46/50 (92.0%)
Mean ep_len:        201.540 +/- 181.446
--------------------------------
_models/ppo_20260717_0905_PointLTL5MASAR1-v0_0
========================================
Mean reward:        0.620 +/- 0.485
Rescue rate:        31/50 (62.0%)
Mean ep_len:        182.480 +/- 52.410

_models/rnd_ppo_L5_S2_20260717_1109_PointLTL5MASAR1WC-v0_0
========================================
Mean reward:        0.660 +/- 0.474
Rescue rate:        33/50 (66.0%)
Mean ep_len:        191.980 +/- 60.951
--------------------------------
_models/rnd_ppo_L6_S2_20260717_0906_PointLTL6MASAR1-v0_0
========================================
Mean reward:        0.440 +/- 0.496
Rescue rate:        22/50 (44.0%)
Mean ep_len:        290.480 +/- 302.739

_models/ppo_20260717_0906_PointLTL6MASAR1-v0_0
========================================
Mean reward:        0.000 +/- 0.000
Rescue rate:        0/50 (0.0%)
Mean ep_len:        2487.240 +/- 89.320
```
# RND
```sh
# First test using RND on surface casualty env
_models/rnd_ppo_L4_S2_20260716_1511_PointLTL4MASAR1-v0_0
Mean reward:        0.960 +/- 0.196
Rescue rate:        48/50 (96.0%)
Mean ep_len:        249.760 +/- 238.361
----------------------------------------
# RND on entrapped building environment (no disregard)
_models/rnd_ppo_L5_S2_20260716_1639_PointLTL5MASAR1-v0_0
========================================
Mean reward:        0.600 +/- 0.529
Rescue rate:        29/50 (58.0%)
Mean ep_len:        1286.540 +/- 1066.874
-----------------------------------------
# Observation-based wall collisions
_models/rnd_ppo_L6_S2_20260716_2349_PointLTL6MASAR1-v0_0
========================================
Mean reward:        1.400 +/- 0.648
Rescue rate:        40/50 (80.0%)
Mean ep_len:        411.760 +/- 383.412

_models/rnd_ppo_L6_S2_20260719_1936_PointLTL6MASAR1-v0_0
========================================
Mean reward:        0.900 +/- 0.300
Rescue rate:        45/50 (90.0%)
Mean ep_len:        728.240 +/- 779.803

```

# PPO
```sh
_models/ppo_20260720_1838_PointLTL0MASAR1-v0_0
========================================
Rescue rate: 50/50 (100.0%)
Mean ep_len: 198.420 +/- 83.106

_models/ppo_20260720_1838_PointLTL4MASAR1-v0_1
========================================
Rescue rate: 49/50 (98.0%)
Mean ep_len: 194.300 +/- 159.937

_models/ppo_20260721_0811_PointLTL4MASAR1WC-v0_0
========================================
Mean reward: 0.860 +/- 0.347
Rescue rate: 43/50 (86.0%)
Mean ep_len: 181.660 +/- 141.758

_models/ppo_20260720_1838_PointLTL5MASAR1-v0_3
========================================
Rescue rate: 49/50 (98.0%)
Mean ep_len: 258.240 +/- 129.260

_models/ppo_20260721_1233_PointLTL5MASAR1WC-v0_0
# PPO_t20260721_1233_st4096_bs256_tt4.0M_ec0.02_lr5e-05_ep10_cr0.2_kl0.05_γ0.99_λ0.95_s0
========================================
Mean reward: 0.680 +/- 0.466
Rescue rate: 34/50 (68.0%)
Mean ep_len: 194.780 +/- 49.972
_models/ppo_20260720_1838_PointLTL6MASAR1-v0_4
========================================
Mean reward: 0.900 +/- 0.300
Rescue rate: 45/50 (90.0%)
Mean ep_len: 650.800 +/- 705.477
------------------------------------------------------

_models/ppo_20260720_1644_PointLTL6MASAR1-v0_0
# gamma=0.995, gae_lambda=0.98
========================================
Mean reward: 0.940 +/- 0.237
Rescue rate: 47/50 (94.0%)
Mean ep_len: 637.820 +/- 572.917
```
# PPO Lagrangian
```shell
_models/ppo_lag_20260721_0809_PointLTL4MASAR1WC-v0_0
========================================
Mean reward: 0.800 +/- 0.400
Rescue rate: 40/50 (80.0%)
Mean ep_len: 193.800 +/- 184.005

-----------------------------------------
_models/ppo_lag_L4_S0_20260717_2248_PointLTL4MASAR1WC-v0_0
========================================
Mean reward:        0.940 +/- 0.237
Rescue rate:        47/50 (94.0%)
Mean ep_len:        184.220 +/- 100.788
-----------------------------------------

_models/ppo_lag_L5_S0_20260717_2332_PointLTL5MASAR1WC-v0_0
========================================
Mean reward:        0.500 +/- 0.500
Rescue rate:        25/50 (50.0%)
Mean ep_len:        206.280 +/- 92.236

# After switching to sb3-style updates (~640 vs 20)

_models/ppo_lag_L5_S1_20260719_1341_PointLTL5MASAR1WC-v0_0
# S0
========================================
Mean reward:        0.720 +/- 0.449
Rescue rate:        36/50 (72.0%)
Mean ep_len:        216.100 +/- 89.889

_models/ppo_lag_L5_S0_20260719_1939_PointLTL5MASAR1WC-v0_0
# S0
========================================
Mean reward:        0.740 +/- 0.439
Rescue rate:        37/50 (74.0%)
Mean ep_len:        208.300 +/- 66.244

_models/ppo_lag_L5_S1_20260719_2112_PointLTL5MASAR1WC-v0_0
# S1
========================================
Mean reward:        0.720 +/- 0.449
Rescue rate:        36/50 (72.0%)
Mean ep_len:        369.820 +/- 292.297

_models/ppo_lag_20260720_1602_PointLTL6MASAR1WC-v0_0
========================================
Mean reward: 0.120 +/- 0.325
Rescue rate: 6/50 (12.0%)
Mean ep_len: 778.560 +/- 311.987
```
# TRPO
```sh
_models/trpo_20260720_1256_PointLTL0MASAR1-v0_0
========================================
Mean reward: 1.000 +/- 0.000
Rescue rate: 50/50 (100.0%)
Mean ep_len: 189.040 +/- 77.015

_models/trpo_20260720_1328_PointLTL4MASAR1-v0_0
========================================
Mean reward: 0.960 +/- 0.196
Rescue rate: 48/50 (96.0%)
Mean ep_len: 215.840 +/- 198.322

_models/trpo_20260721_0810_PointLTL4MASAR1WC-v0_0
========================================
Mean reward: 0.880 +/- 0.325
Rescue rate: 44/50 (88.0%)
Mean ep_len: 202.800 +/- 163.613

_models/trpo_20260720_1328_PointLTL5MASAR1-v0_2
========================================
Mean reward: 0.980 +/- 0.140
Rescue rate: 49/50 (98.0%)
Mean ep_len: 256.300 +/- 120.162

_models/trpo_20260721_0810_PointLTL5MASAR1WC-v0_0
========================================
Mean reward: 0.780 +/- 0.414
Rescue rate: 39/50 (78.0%)
Mean ep_len: 228.660 +/- 57.095

_models/trpo_20260720_1328_PointLTL6MASAR1-v0_3
========================================
Mean reward: 0.920 +/- 0.271
Rescue rate: 46/50 (92.0%)
Mean ep_len: 556.540 +/- 608.140

_models/trpo_20260721_0810_PointLTL6MASAR1WC-v0_0
========================================
Mean reward: 0.520 +/- 0.500
Rescue rate: 26/50 (52.0%)
Mean ep_len: 467.320 +/- 653.646
```

# TRPO Lagrangian
```sh
_models/trpo_lag_20260721_0811_PointLTL4MASAR1WC-v0_0
========================================
Mean reward: 0.840 +/- 0.367
Rescue rate: 42/50 (84.0%)
Mean ep_len: 238.120 +/- 225.010

_models/trpo_lag_20260721_0811_PointLTL5MASAR1WC-v0_0
========================================
Mean reward: 0.540 +/- 0.498
Rescue rate: 27/50 (54.0%)
Mean ep_len: 338.180 +/- 259.823

_models/trpo_lag_20260720_2100_PointLTL6MASAR1WC-v0_2
========================================
Mean reward: 0.180 +/- 0.384
Rescue rate: 9/50 (18.0%)
Mean ep_len: 1817.900 +/- 975.505
```
# SAC
```sh
_models/sac_20260720_1414_PointLTL0MASAR1-v0_0
# 4 envs, 8/8
========================================
Mean reward: 0.980 +/- 0.140
Rescue rate: 49/50 (98.0%)
Mean ep_len: 196.040 +/- 137.233

_models/sac_20260720_2253_PointLTL4MASAR1-v0_0
# 8 envs, 1/1
========================================
Mean reward: 0.740 +/- 0.439
Rescue rate: 37/50 (74.0%)
Mean ep_len: 362.900 +/- 381.330
```
---

--- 
#project/idea
