import mlflow
import sklearn
import torch
import transformers

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("Transformers version:", transformers.__version__)
print("scikit-learn version:", sklearn.__version__)
print("MLflow version:", mlflow.__version__)
