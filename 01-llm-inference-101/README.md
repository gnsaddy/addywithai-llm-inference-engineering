# Lecture 1 code: measure_latency.py

Learn LLM Inference Engineering, Lecture 1 (LLM Inference 101: Latency, Throughput and Cost).

* Python 3.8+, standard library only. Runs on any normal CPU: no GPU, no API key, nothing to install.
* The "model" is a stand-in server (`fake_model`) that sleeps like a real one: a prefill pause that grows with the prompt, then 20 ms per decode step.
* Part 1 measures **TTFT** (time to first token), **TPOT** (time per output token), total time and tokens/s for a short and a long prompt.
* Part 2 is a batching table: per-user speed, total throughput, **$ per 1M tokens** and whether each batch size meets a 50 ms TPOT target (SLO).
* The GPU price ($2/hour) and step times are **example numbers**. Swap in your own.

Run:
```
python measure_latency.py
```

Output on the recording machine (timings vary a little per run):
```
prompt   500: TTFT 0.15s  TPOT 20ms  total 2.14s  47 tok/s
prompt  4000: TTFT 0.85s  TPOT 20ms  total 2.85s  35 tok/s
batch  per-user   total tok/s  $ per 1M   SLO
    1     49 t/s        49     $ 11.39   ok
    8     42 t/s       333     $  1.67   ok
   32     28 t/s       889     $  0.62   ok
   64     19 t/s      1231     $  0.45   too slow
  128     12 t/s      1524     $  0.36   too slow
```

To measure a real server later in the series, replace `fake_model` with a streaming call to any OpenAI-compatible endpoint (for example a local vLLM or Ollama server) and keep `measure()` as it is.
