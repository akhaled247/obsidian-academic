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
#_models/ppo_20260714_1540_PointLTL4MASAR1-v0_run9
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
# "_models/ppo_20260714_1623_PointLTL4MASAR1-v0_run9"
Mean reward:        1.980 +/- 0.140
Rescue rate:        49/50 (98.0%)
s0-Vis rescue %:    38/39 (97.4%)
s0-Invis rescue %:  11/11 (100.0%)
Mean ep_len:        258.300 +/- 192.859
Mean reward:        1.980 +/- 0.140
-----------------------------------------------------
# "_models/ppo_20260714_1652_PointLTL4MASAR1-v0_run9"
Mean reward:        1.560 +/- 0.753
Rescue rate:        36/50 (72.0%)
s0-Vis rescue %:    36/39 (92.3%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        433.420 +/- 373.808 
Mean reward:        1.560 +/- 0.753
=====================================================
# Note: These next two runs I was testing absolute reproducability, which is why they're identical
# "_models/ppo_20260714_2020_PointLTL4MASAR1-v0_run9"
Mean reward:        1.180 +/- 0.477
Rescue rate:        11/50 (22.0%)
s0-Vis rescue %:    11/39 (28.2%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        851.840 +/- 287.426
Mean reward:        1.180 +/- 0.477
-----------------------------------------------------
# "_models/ppo_20260714_2029_PointLTL4MASAR1-v0_run9"
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
# "_models/ppo_20260714_2103_PointLTL4MASAR1-v0"
# with visibility reward
Mean reward:        0.840 +/- 0.418
Rescue rate:        1/50 (2.0%)
s0-Vis rescue %:    1/39 (2.6%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        999.200 +/- 5.600
Mean reward:        0.840 +/- 0.418
-----------------------------------------------------
# "_models/ppo_20260714_2053_PointLTL4MASAR1-v0"
# without visibility reward
Mean reward:        0.100 +/- 0.300
Rescue rate:        5/50 (10.0%)
s0-Vis rescue %:    5/39 (12.8%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        914.140 +/- 258.424
Mean reward:        0.100 +/- 0.300
-----------------------------------------------------
# _models/ppo_20260714_2304_PointLTL4MASAR1-v0
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

saved model: _models/ppo_20260715_0729_PointLTL4MASAR1-v0.zip
----------------------------------------
Mean reward:        1.220 +/- 0.642
Rescue rate:        17/50 (34.0%)
s0-Vis rescue %:    17/39 (43.6%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        783.820 +/- 337.644 
Mean reward:        1.220 +/- 0.642

saved model: _models/ppo_20260715_0729_PointLTL4MASAR1-v0.zip
----------------------------------------
Mean reward:        1.020 +/- 0.140
Rescue rate:        1/50 (2.0%)
s0-Vis rescue %:    1/39 (2.6%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        982.460 +/- 122.780 
Mean reward:        1.020 +/- 0.140

saved model: _models/ppo_20260715_0729_PointLTL4MASAR1-v0.zip
----------------------------------------
Mean reward:        1.400 +/- 0.600
Rescue rate:        23/50 (46.0%)
s0-Vis rescue %:    18/39 (46.2%)
s0-Invis rescue %:  5/11 (45.5%)
Mean ep_len:        692.720 +/- 379.782 
Mean reward:        1.400 +/- 0.600

saved model: _models/ppo_20260715_0729_PointLTL4MASAR1-v0.zip
----------------------------------------
Mean reward:        1.040 +/- 0.564
Rescue rate:        9/50 (18.0%)
s0-Vis rescue %:    8/39 (20.5%)
s0-Invis rescue %:  1/11 (9.1%)
Mean ep_len:        845.980 +/- 330.296 
Mean reward:        1.040 +/- 0.564

saved model: _models/ppo_20260715_0832_PointLTL4MASAR1-v0.zip
----------------------------------------
Mean reward:        0.940 +/- 0.237
Rescue rate:        0/50 (0.0%)
s0-Vis rescue %:    0/39 (0.0%)
s0-Invis rescue %:  0/11 (0.0%)
Mean ep_len:        1000.000 +/- 0.000 
Mean reward:        0.940 +/- 0.237
```

# Entrapped Casualties(reward ∈ {0, 1})
```sh
# _models/ppo_20260715_1124_PointLTL5MASAR1-v0_0.zip
# Note: Trained on building in the same location, but eval had buildings in random location (bug fixed after training)
Mean reward:        1.000 +/- 0.200
Rescue rate:        49/50 (98.0%)
Mean ep_len:        262.340 +/- 133.052
# 20 obstacles
Mean reward:        0.900 +/- 0.361
Rescue rate:        44/50 (88.0%)
Mean ep_len:        424.780 +/- 250.803
```

`_models/ppo_20260715_1623_PointLTL5MASAR1-v0_0.zip
-1 reward for collision with wall
Mean reward:        0.680 +/- 0.614
Rescue rate:        41/50 (82.0%)
Mean ep_len:        370.940 +/- 297.217



--- 
#project/idea
