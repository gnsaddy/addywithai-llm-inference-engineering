# Learn LLM Inference Engineering: code for every lecture

Python code for the **Learn LLM Inference Engineering** series by **@addywithai**. Each folder matches one lecture and has its own `README.md`.

## How to run any lecture

```bash
cd <folder>
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt   # if the folder has one
cp .env.example .env              # only if the folder has one, then paste your own key
```

Then follow the run steps in that folder's `README.md`. Never commit your `.env` file; it is already in `.gitignore`.

Python 3.10 or newer.

## Lectures

| # | Lecture | Code |
|---|---|---|
| 1 | LLM Inference 101: Latency, Throughput and Cost | [01-llm-inference-101](01-llm-inference-101) |
| 2 | GPU, TPU and the Memory Wall | Coming soon |
| 3 | Prefill vs Decode | Coming soon |
| 4 | Sampling and Decoding Strategies | Coming soon |
| 5 | Token Streaming | Coming soon |
| 6 | KV Cache | Coming soon |
| 7 | Grouped Query Attention | Coming soon |
| 8 | Flash Attention | Coming soon |
| 9 | PagedAttention | Coming soon |
| 10 | Prompt Caching | Coming soon |
| 11 | Long-Context Inference | Coming soon |
| 12 | Continuous Batching | Coming soon |
| 13 | Quantization | Coming soon |
| 14 | Speculative Decoding | Coming soon |
| 15 | Kernels and Compilers | Coming soon |
| 16 | Model Parallelism | Coming soon |
| 17 | Mixture of Experts | Coming soon |
| 18 | Disaggregated Serving: Splitting Prefill and Decode | Coming soon |
| 19 | How does vLLM work? | Coming soon |
| 20 | How does SGLang work? | Coming soon |
| 21 | Other Inference Engines: TensorRT-LLM, TGI, llama.cpp, Ollama | Coming soon |
| 22 | On-Device and Edge Inference | Coming soon |
| 23 | Serving Fine-Tuned Models: Multi-LoRA | Coming soon |
| 24 | LLM Routing | Coming soon |
| 25 | Deployment and Autoscaling | Coming soon |
| 26 | Observability for LLM Inference | Coming soon |
| 27 | Benchmarking and Inference Cost | Coming soon |
| 28 | Capstone: Build and Tune a Mini LLM Server | Coming soon |
