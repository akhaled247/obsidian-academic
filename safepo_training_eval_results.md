# Shell-Comment Conversion Scripts
```sh
python "C:/GitHub/obsidian-vaults/Obsidian Vault/academic-obsidian-main/scripts/train_cmd_to_comment.py" "qwertyuiopasdfghjklzxcvbnm"

	python 'C:\GitHub\obsidian-vaults\Obsidian Vault\academic-obsidian-main\scripts\comment_to_train_cmd.py' "qwertyuiopasdfghjklzxcvbnm"
```

# Single-Agent Tasks
## PPO
```sh
'ppo_envPointLTL4MASAR1WC-v0_4M_T16384_N8_αa5e-5_αc1e-3_B256_I10_DKL0.02_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre0'
2.0%

'ppo_envPointLTL4MASAR1WC-v0_4M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1WC-v0/ppo/seed-000-2026-07-22-00-39-41
After 50 episodes evaluation, the ppo in PointLTL4MASAR1WC-v0 reward: 0.78±0.41, cost: 0.22±0.41, ep_len: 168.48±90.63, rescue: 78.0%

'ppo_envPointLTL5MASAR1-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo/seed-000-2026-07-22-07-52-51
After 50 episodes evaluation, the ppo in PointLTL5MASAR1-v0 reward: 0.94±0.24, cost: 0.00±0.00, ep_len: 285.68±190.49, rescue: 94.0%
    
'ppo_envPointLTL5MASAR1WC-v0_5M_T65536_N8_αa7e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0'  
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo/seed-000-2026-07-22-07-52-51
After 50 episodes evaluation, the ppo in PointLTL5MASAR1WC-v0 reward: 0.00±0.00, cost: 0.92±0.27, ep_len: 300.32±251.82, rescue: 0.0%    

'ppo_envPointLTL4MASAR1-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1-v0/ppo/seed-000-2026-07-22-09-49-51
After 50 episodes evaluation, the ppo in PointLTL4MASAR1-v0 reward: 0.04±0.20, cost: 0.00±0.00, ep_len: 965.10±171.37, rescue: 4.0%

'ppo_envPointLTL5MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo/seed-000-2026-07-22-11-47-36
After 50 episodes evaluation, the ppo in PointLTL5MASAR1WC-v0 reward: 0.68±0.47, cost: 0.32±0.47, ep_len: 227.84±87.76, rescue: 68.0%
```
## PPO-Lagrangian
```sh
'ppo_lag_envPointLTL5MASAR1WC-v0_6M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0_cl0.25_λi0.25_λlr1e-3'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-10-01-27
After 50 episodes evaluation, the ppo in PointLTL5MASAR1WC-v0 reward: 0.02±0.14, cost: 0.94±0.24, ep_len: 287.12±237.36, rescue: 2.0%

'ppo_lag_envPointLTL5MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0_cl0.25_λi0.25_λlr1e-3'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-11-29-47
After 50 episodes evaluation, the ppo_lag in PointLTL5MASAR1WC-v0 reward: 0.00±0.00, cost: 0.06±0.24, ep_len: 970.80±129.73, rescue: 0.0%

'ppo_lag_envPointLTL4MASAR1WC-v0_4M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0_cl0.25_λi0.25_λlr1e-3'
# SpecRLBench/_training_logs/safepo/PointLTL4MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-11-31-41
After 50 episodes evaluation, the ppo_lag in PointLTL4MASAR1WC-v0 reward: 
0.64±0.48, cost: 0.36±0.48, ep_len: 132.56±51.96, rescue: 64.0%

'ppo_lag_envPointLTL5MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0_cl1.0_λi1.0_λlr1e-2'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/ppo_lag/seed-000-2026-07-22-13-52-02
Early termination

'ppo_lag_envPointLTL5MASAR1WC-v0_5M_T16384_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0_cl0.0_λi1.0_λlr5e-2_ec0.02'
Early termination -- 0 mean return over 1M timesteps

'ppo_lag_envPointLTL5MASAR1-v0_5M_T16384_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0_cl0_λi1.0_λlr5e-2_ec0.02'
```
## TRPO
```sh
'trpo_envPointLTL5MASAR1WC-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I1_DKL0.02_γ0.99_λ0.95_λc0.95_g40_h64×64'
# SpecRLBench/_training_logs/safepo/PointLTL5MASAR1WC-v0/trpo/seed-000-2026-07-22-13-54-45
```