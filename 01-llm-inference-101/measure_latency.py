# LLM Inference 101: measure TTFT, TPOT and tokens/s, then turn throughput into cost.
# Runs on any CPU (stdlib only). The "model" is a stand-in that sleeps like a real server.
import time

def fake_model(prompt_tokens, max_tokens):
    """Stand-in LLM server: prefill the prompt, then decode one token at a time."""
    time.sleep(0.05 + prompt_tokens * 0.0002)    # prefill: whole prompt at once
    for i in range(max_tokens):
        if i:
            time.sleep(0.02)                      # decode: one step per token
        yield f"tok{i}"

def measure(prompt_tokens, max_tokens):
    start = time.perf_counter()
    first, n = None, 0
    for _ in fake_model(prompt_tokens, max_tokens):
        if first is None:
            first = time.perf_counter() - start  # time to first token
        n += 1
    total = time.perf_counter() - start
    tpot = (total - first) / (n - 1)              # time per output token
    return first, tpot, total, n / total

for p in (500, 4000):
    ttft, tpot, total, tps = measure(p, 100)
    print(f"prompt {p:>5}: TTFT {ttft:.2f}s  TPOT {tpot * 1000:.0f}ms  "
          f"total {total:.2f}s  {tps:.0f} tok/s")

# Batching: one decode step serves the whole batch, but each step gets slower.
GPU_PER_HOUR = 2.00          # $ per GPU hour (example price)
SLO_TPOT = 0.050             # our target: at most 50 ms per token

print("batch  per-user   total tok/s  $ per 1M   SLO")
for batch in (1, 8, 32, 64, 128):
    step = 0.020 + 0.0005 * batch               # seconds per decode step (example)
    per_user = 1 / step
    total = batch * per_user
    cost = GPU_PER_HOUR / (total * 3600) * 1e6
    ok = "ok" if step <= SLO_TPOT else "too slow"
    print(f"{batch:>5}  {per_user:>5.0f} t/s  {total:>8.0f}     ${cost:>6.2f}   {ok}")
