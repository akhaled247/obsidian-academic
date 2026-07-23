# Shell-Comment Conversion Scripts
```sh
python "C:/GitHub/obsidian-vaults/Obsidian Vault/academic-obsidian-main/scripts/train_cmd_to_comment.py" "QWERTYUIOPASDFGHJKLZXCVBNM"

python "C:\GitHub\obsidian-vaults\Obsidian Vault\academic-obsidian-main\scripts\comment_to_train_cmd.py" 'trpo_lag_envPointLTL5MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I1_DKL0.05_γ0.995_λ0.98_λc0.98_g40_h64×64_cl0_λi0_λlr1e-2_ec0.01'

python 'C:\GitHub\obsidian-vaults\Obsidian Vault\academic-obsidian-main\scripts\comment_to_train_cmd.py' "QWERTYUIOPASDFGHJKLZXCVBNM"

python ".\Obsidian Vault\academic-obsidian-main\scripts\config_to_comment.py" 'QWERTYUIOPASDFGHJKLZXCVBNM'
```

# Single-Agent Tasks
## Best-Of
### Vanilla PPO
```sh
'ppo_envPointLTL4MASAR1-v0_4M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0_ec0'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1-v0/ppo/seed-000-2026-07-22-20-24-10
After 50 episodes evaluation, the ppo in PointLTL4MASAR1-v0 reward: 0.96±0.20, cost: 0.00±0.00, ep_len: 245.76±200.70, rescue: 96.0%
============================================================
'ppo_envPointLTL4MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0_ec0'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1WC-v0/ppo/seed-000-2026-07-22-21-38-33
After 50 episodes evaluation, the ppo in PointLTL4MASAR1WC-v0 reward: 0.86±0.35, cost: 0.14±0.35, ep_len: 168.06±98.31, rescue: 86.0%
============================================================
'ppo_envPointLTL5MASAR1-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo/seed-000-2026-07-22-07-52-51
After 50 episodes evaluation, the ppo in PointLTL5MASAR1-v0 reward: 0.94±0.24, cost: 0.00±0.00, ep_len: 285.68±190.49, rescue: 94.0%
============================================================
'ppo_envPointLTL5MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo/seed-000-2026-07-22-11-47-36
After 50 episodes evaluation, the ppo in PointLTL5MASAR1WC-v0 reward: 0.68±0.47, cost: 0.32±0.47, ep_len: 227.84±87.76, rescue: 68.0%
```
### PPO Lagrangian
```sh
'ppo_lag_envPointLTL4MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0_cl0_λi0_λlr1e-2_ec0'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-20-30-23
After 50 episodes evaluation, the ppo_lag in PointLTL4MASAR1WC-v0 reward: 0.80±0.40, cost: 0.20±0.40, ep_len: 173.04±95.76, rescue: 80.0%
============================================================
'ppo_lag_envPointLTL5MASAR1WC-v0_6M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0_cl0_λi0_λlr1e-2_ec0.01'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-22-46-43
After 50 episodes evaluation, the ppo_lag in PointLTL5MASAR1WC-v0 reward: 0.68±0.47, cost: 0.30±0.46, ep_len: 224.70±132.49, rescue: 68.0%
============================================================
```
### Vanilla TRPO
```sh
'trpo_envPointLTL5MASAR1-v0_4M_T32768_N8_αa5e-5_αc1e-3_B256_I1_DKL0.02_γ0.99_λ0.95_λc0.95_g40_h64×64'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1-v0/trpo/seed-000-2026-07-22-01-10-32
After 50 episodes evaluation, the trpo in PointLTL5MASAR1-v0 reward: 0.90±0.30, cost: 0.00±0.00, ep_len: 391.90±235.26, rescue: 90.0%
============================================================
```
### TRPO Lagrangian
```sh
'N/A'
```
## PPO
```sh
'ppo_envPointLTL4MASAR1WC-v0_4M_T16384_N8_αa5e-5_αc1e-3_B256_I10_DKL0.02_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre0'
2.0%
============================================================
'ppo_envPointLTL4MASAR1WC-v0_4M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1WC-v0/ppo/seed-000-2026-07-22-00-39-41
After 50 episodes evaluation, the ppo in PointLTL4MASAR1WC-v0 reward: 0.78±0.41, cost: 0.22±0.41, ep_len: 168.48±90.63, rescue: 78.0%
============================================================
'ppo_envPointLTL5MASAR1-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo/seed-000-2026-07-22-07-52-51
After 50 episodes evaluation, the ppo in PointLTL5MASAR1-v0 reward: 0.94±0.24, cost: 0.00±0.00, ep_len: 285.68±190.49, rescue: 94.0%
============================================================
'ppo_envPointLTL5MASAR1WC-v0_5M_T65536_N8_αa7e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0'  
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo/seed-000-2026-07-22-07-52-51
After 50 episodes evaluation, the ppo in PointLTL5MASAR1WC-v0 reward: 0.00±0.00, cost: 0.92±0.27, ep_len: 300.32±251.82, rescue: 0.0%    
============================================================
'ppo_envPointLTL4MASAR1-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1-v0/ppo/seed-000-2026-07-22-09-49-51
After 50 episodes evaluation, the ppo in PointLTL4MASAR1-v0 reward: 0.04±0.20, cost: 0.00±0.00, ep_len: 965.10±171.37, rescue: 4.0%
============================================================
'ppo_envPointLTL5MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo/seed-000-2026-07-22-11-47-36
After 50 episodes evaluation, the ppo in PointLTL5MASAR1WC-v0 reward: 0.68±0.47, cost: 0.32±0.47, ep_len: 227.84±87.76, rescue: 68.0%
============================================================
'ppo_envPointLTL4MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0_ec0'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1WC-v0/ppo/seed-000-2026-07-22-21-38-33
After 50 episodes evaluation, the ppo in PointLTL4MASAR1WC-v0 reward: 0.86±0.35, cost: 0.14±0.35, ep_len: 168.06±98.31, rescue: 86.0%
============================================================
'ppo_envPointLTL4MASAR1-v0_4M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0_ec0'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1-v0/ppo/seed-000-2026-07-22-20-24-10
After 50 episodes evaluation, the ppo in PointLTL4MASAR1-v0 reward: 0.96±0.20, cost: 0.00±0.00, ep_len: 245.76±200.70, rescue: 96.0%
============================================================
'ppo_envPointLTL6MASAR1-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0'


```
## PPO Lagrangian
```sh
'ppo_lag_envPointLTL5MASAR1WC-v0_6M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0_cl0.25_λi0.25_λlr1e-3'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-10-01-27
After 50 episodes evaluation, the ppo in PointLTL5MASAR1WC-v0 reward: 0.02±0.14, cost: 0.94±0.24, ep_len: 287.12±237.36, rescue: 2.0%
============================================================
'ppo_lag_envPointLTL5MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0_cl0.25_λi0.25_λlr1e-3'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-11-29-47
After 50 episodes evaluation, the ppo_lag in PointLTL5MASAR1WC-v0 reward: 0.00±0.00, cost: 0.06±0.24, ep_len: 970.80±129.73, rescue: 0.0%
============================================================
'ppo_lag_envPointLTL4MASAR1WC-v0_4M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0_cl0.25_λi0.25_λlr1e-3'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-11-31-41
After 50 episodes evaluation, the ppo_lag in PointLTL4MASAR1WC-v0 reward: 
0.64±0.48, cost: 0.36±0.48, ep_len: 132.56±51.96, rescue: 64.0%
============================================================
'ppo_lag_envPointLTL5MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0_cl1.0_λi1.0_λlr1e-2'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-13-52-02
Early termination -- 0 mean return over 1M timesteps
============================================================
'ppo_lag_envPointLTL5MASAR1WC-v0_5M_T16384_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0_cl0.0_λi1.0_λlr5e-2_ec0.02'
Early termination -- 0 mean return over 1M timesteps
============================================================
'ppo_lag_envPointLTL5MASAR1-v0_5M_T16384_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0_cl0_λi1.0_λlr5e-2_ec0.02'
Early termination -- 0 mean return over 1M timesteps
============================================================
'ppo_lag_envPointLTL5MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0_cl0_λi0_λlr1e-2'
After 50 episodes evaluation, the ppo_lag in PointLTL5MASAR1WC-v0 reward: 0.62±0.49, cost: 0.32±0.47, ep_len: 271.80±197.35, rescue: 62.0%
============================================================
'ppo_lag_envPointLTL5MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0_cl0_λi0_λlr1e-3'After 50 episodes evaluation, the ppo_lag in PointLTL5MASAR1WC-v0 reward: 0.00±0.00, cost: 0.60±0.49, ep_len: 502.72±412.84, rescue: 0.0%
============================================================
'ppo_lag_envPointLTL4MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0_cl0_λi0_λlr1e-2_ec0'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-20-30-23
After 50 episodes evaluation, the ppo_lag in PointLTL4MASAR1WC-v0 reward: 0.80±0.40, cost: 0.20±0.40, ep_len: 173.04±95.76, rescue: 80.0%
============================================================
'ppo_lag_envPointLTL5MASAR1WC-v0_6M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0_cl0_λi0_λlr1e-2_ec0.01'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-22-46-43
After 50 episodes evaluation, the ppo_lag in PointLTL5MASAR1WC-v0 reward: 0.68±0.47, cost: 0.30±0.46, ep_len: 224.70±132.49, rescue: 68.0%
============================================================
'ppo_lag_envPointLTL5MASAR1WC-v0_6M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0_cl0_λi0_λlr1e-2_ec0.02'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-22-47-38
After 50 episodes evaluation, the ppo_lag in PointLTL5MASAR1WC-v0 reward: 0.58±0.49, cost: 0.34±0.47, ep_len: 300.06±249.98, rescue: 58.0%
============================================================
'ppo_lag_envPointLTL5MASAR1WC-v0_6M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0_cl0_λi0_λlr1e-2_ec0'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-22-48-40
After 50 episodes evaluation, the ppo_lag in PointLTL5MASAR1WC-v0 reward: 0.64±0.48, cost: 0.30±0.46, ep_len: 268.38±206.61, rescue: 64.0%
============================================================
```
## TRPO
```sh
'trpo_envPointLTL5MASAR1-v0_4M_T32768_N8_αa5e-5_αc1e-3_B256_I1_DKL0.02_γ0.99_λ0.95_λc0.95_g40_h64×64'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1-v0/trpo/seed-000-2026-07-22-01-10-32
After 50 episodes evaluation, the trpo in PointLTL5MASAR1-v0 reward: 0.90±0.30, cost: 0.00±0.00, ep_len: 391.90±235.26, rescue: 90.0%
============================================================
'trpo_envPointLTL4MASAR1-v0_4M_T32768_N8_αa5e-5_αc1e-3_B256_I1_DKL0.05_γ0.995_λ0.98_λc0.98_g40_h64×64'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1-v0/trpo/seed-000-2026-07-23-09-26-21
After 50 episodes evaluation, the trpo in PointLTL4MASAR1-v0 reward: 0.94±0.24, cost: 0.00±0.00, ep_len: 233.92±234.98, rescue: 94.0%
============================================================
'trpo_envPointLTL4MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I1_DKL0.05_γ0.995_λ0.98_λc0.98_g40_h64×64'


'trpo_envPointLTL6MASAR1-v0_4M_T32768_N8_αa5e-5_αc1e-3_B256_I1_DKL0.05_γ0.995_λ0.98_λc0.98_g40_h64×64'
```

## TRPO Lagrangian
```sh
'trpo_lag_envPointLTL4MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I1_DKL0.05_γ0.995_λ0.98_λc0.98_g40_h64×64_cl0_λi0_λlr1e-2_ec0'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1WC-v0/trpo_lag/seed-000-2026-07-23-09-38-50
After 50 episodes evaluation, the trpo_lag in PointLTL4MASAR1WC-v0 reward: 0.38±0.49, cost: 0.26±0.44, ep_len: 505.64±391.78, rescue: 38.0%

'trpo_lag_envPointLTL5MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I1_DKL0.05_γ0.995_λ0.98_λc0.98_g40_h64×64_cl0_λi0_λlr1e-2_ec0.01'

'ppo_lag_envPointLTL5MASAR1WC-v0_6M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0_cl0_λi0_λlr1e-2_ec0.01'
```

## Custom CMD Creation
```sh
python train/ppo_lag_train_env.py     --task PointLTL5MASAR1WC-v0 --seed 0     --total-steps 6000000 --num-envs 8 --steps-per-epoch 32768     --cost-limit 0     --lagrangian-multiplier-init 0 --lagrangian-multiplier-lr 1e-2     --actor-lr 5e-5 --critic-lr 1e-3     --batch-size 256 --learning-iters 10     --target-kl 0.05 --gamma 0.995 --lam 0.98 --lam-c 0.98     --clip-ratio 0.2 --max-grad-norm 40 --hidden-sizes 64 64     --device cuda --device-id 1     --write-terminal False --use-tensorboard True     --parallel True --lr_end_factor 1.0 --ent-coef 0.005
```