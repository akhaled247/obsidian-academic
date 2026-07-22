```sh
python "C:/GitHub/obsidian-vaults/Obsidian Vault/academic-obsidian-main/scripts/train_cmd_to_comment.py" "qwertyuiopasdfghjklzxcvbnm"

	python 'C:\GitHub\obsidian-vaults\Obsidian Vault\academic-obsidian-main\scripts\comment_to_train_cmd.py' "qwertyuiopasdfghjklzxcvbnm"
```

# PPO
```sh
# ppo_envPointLTL4MASAR1WC-v0_4M_T16384_N8_αa5e-5_αc1e-3_B256_I10_DKL0.02_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre0
python train/ppo_train_env.py \
    --task PointLTL4MASAR1WC-v0 --seed 0 \
    --total-steps 4000000 --num-envs 8 --steps-per-epoch 16384 \
    --actor-lr 5e-5 --critic-lr 1e-3 \
    --batch-size 256 --learning-iters 10 \
    --target-kl 0.02 --gamma 0.99 --lam 0.95 --lam-c 0.95 \
    --clip-ratio 0.2 --max-grad-norm 40 \
    --hidden-sizes 64 64 \
    --device cuda --device-id 1 \
    --write-terminal False --use-tensorboard True \
    --parallel True
2.0%

# ppo_envPointLTL4MASAR1WC-v0_4M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.99_λ0.95_λc0.95_ε0.2_g40_h64×64_lre1.0
python train/ppo_train_env.py \
    --task PointLTL4MASAR1WC-v0 --seed 0 \
    --total-steps 4000000 --num-envs 8 --steps-per-epoch 32768 \
    --actor-lr 5e-5 --critic-lr 1e-3 \
    --batch-size 256 --learning-iters 10 \
    --target-kl 0.05 --gamma 0.99 --lam 0.95 --lam-c 0.95 \
    --clip-ratio 0.2 --max-grad-norm 40 --hidden-sizes 64 64 \
    --device cuda --device-id 1 \
    --write-terminal False --use-tensorboard True \
    --parallel True --lr_end_factor 1.0
After 50 episodes evaluation, the ppo in PointLTL4MASAR1WC-v0 reward: 0.78±0.41, cost: 0.22±0.41, ep_len: 168.48±90.63, rescue: 78.0%

# ppo_envPointLTL5MASAR1-v0_5M_T32768_N8_αa5e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0
python train/ppo_train_env.py \
    --task PointLTL5MASAR1-v0 --seed 0 \
    --total-steps 5000000 --num-envs 8 --steps-per-epoch 32768 \
    --actor-lr 5e-5 --critic-lr 1e-3 \
    --batch-size 256 --learning-iters 10 \
    --target-kl 0.05 --gamma 0.995 --lam 0.98 --lam-c 0.98 \
    --clip-ratio 0.2 --max-grad-norm 40 --hidden-sizes 64 64 \
    --device cuda --device-id 1 \
    --write-terminal False --use-tensorboard True \
    --parallel True --lr_end_factor 1.0
    
# ppo_envPointLTL5MASAR1WC-v0_5M_T65536_N8_αa7e-5_αc1e-3_B256_I10_DKL0.05_γ0.995_λ0.98_λc0.98_ε0.2_g40_h64×64_lre1.0
python train/ppo_train_env.py \
    --task PointLTL5MASAR1WC-v0 --seed 0 \
    --total-steps 5000000 --num-envs 8 --steps-per-epoch 65536 \
    --actor-lr 7e-5 --critic-lr 1e-3 \
    --batch-size 256 --learning-iters 10 \
    --target-kl 0.05 --gamma 0.995 --lam 0.98 --lam-c 0.98 \
    --clip-ratio 0.2 --max-grad-norm 40 --hidden-sizes 64 64 \
    --device cuda --device-id 1 \
    --write-terminal False --use-tensorboard True \
    --parallel True --lr_end_factor 1.0
    
    
  
```