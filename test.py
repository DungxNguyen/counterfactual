import torch
from dp_optimizer import DPOptimizer

optimizer = torch.optim.SGD(None, lr=0.1)
dp_optimizer = DPOptimizer(
        optimizer=optimizer,
        noise_multiplier=1.0,
        max_grad_norm=1.0,
        expected_batch_size=4,
        )