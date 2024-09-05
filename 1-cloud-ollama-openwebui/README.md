# ollama-cloudformation
CloudFormation templates that simplify launching AWS resources for running:

- [Ollama LLM Management Service](https://ollama.com/)
- [Open-WebUI LLM Web Interface](https://openwebui.com/)

| Template | Description |
| --- | --- |
| [0-amazon-linux2-nvidia-tesla-gpu.yml](./0-amazon-linux2-nvidia-tesla-gpu.yml) | Launches an Amazon Linux 2 instance with an NVIDIA Tesla GPU. |
| [1-amazon-linux2-nvidia-tesla-gpu-efs.yml](./1-amazon-linux2-nvidia-tesla-gpu-efs.yml) | Launches an Amazon Linux 2 instance with an NVIDIA Tesla GPU and an EFS volume to persist Open Web UI data |
| [2-amazon-linux2-nvidia-tesla-gpu-efs-alb.yml](./2-amazon-linux2-nvidia-tesla-gpu-efs-alb.yml) | Same as `1` but with custom domain and SSL certificate |
| [3-amazon-linux2-nvidia-tesla-gpu-multiple-ollama.yml](./3-amazon-linux2-nvidia-tesla-gpu-multiple-ollama.yml) | Single server running Open WebUI, multiple Ollama servers |
