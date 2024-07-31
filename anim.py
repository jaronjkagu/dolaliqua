from transformers import Trainer

trainer = Trainer(model=model, args=training_args, compute_metrics=compute_metrics, timesteps=custom_timesteps)
