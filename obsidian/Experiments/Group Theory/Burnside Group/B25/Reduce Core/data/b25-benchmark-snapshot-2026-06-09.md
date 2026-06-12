---
title: B(2,5) Benchmark Reduction — Run b25-reduce-core-benchmark-0001 (complete)
domain: group-theory
project: b25
experiment_type: reduce-core
author: maumayma
snapshot_date: 2026-06-09
updated: 2026-06-10
provenance: overnight 4-pass Rust beam, b25-reduce-core-benchmark-0001
source_logs: [overnight_4pass.log, remaining_4pass.log, retry_failed.log]
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/proof-search, project/b25, status/inconclusive, data]
---

# B(2,5) Benchmark — Run b25-reduce-core-benchmark-0001 (complete, 119 rows)

**Run**: `experiments/b25_reduce_core/runs/b25-reduce-core-benchmark-0001/`
**Provenance**: overnight 4-pass Rust beam search, binary `braid_reduce`, rules = `mega_ab_rules.live` (~25.7M rules), beam-width 16384, beam-secs 300 per pass.
**Source logs** (all under `runs/b25-reduce-core-benchmark-0001/logs/`):
- `overnight_4pass.log` — primary run, 84 targets (sorted smallest-first, up to 4 iterative passes)
- `remaining_4pass.log` — continuation for targets not yet complete, 19 targets (single `--num-passes 4` invocation)
- `retry_failed.log` — final retry pass for 16 remaining targets (single `--num-passes 4`)

**Cross-check**: all 119 `best_len` values confirmed against `data/overnight_results/*_best.txt` word lengths. Log and .txt agree exactly on all 119. No absent targets.

**Prior-snapshot gap status**: this run covers all 119 targets with fully identified provenance (overnight/remaining/retry logs). However, for 42 of 119 targets the `ui/benchmarks_data.json` best_len is strictly better than this run's result — meaning a different, still-unidentified run produced those JSON records. The 31 previously-untraceable rows are all in that 42. **The JSON provenance gap is NOT closed.** See section below.

---

## Log format

`overnight_4pass.log`: `[comm_X_Y] original=N (word i/119)` → `  pass k: M (Δ=d)` × (up to 4) → `  BEST: M (pct%) [done=N/119 improved=K]`

`remaining_4pass.log` / `retry_failed.log`: `[comm_X_Y] original=N (... word i/N)` → `<word text>` → `BEST: M (pct%) [improved=K]` — single `--num-passes 4` invocation; per-pass lines not logged; pass_count = n/a.

> **original_len** note: the log reads input length with `wc -c` which includes the file's trailing newline, so `original_len` here is exactly 1 greater than the word length (= `raw_len` + 1 vs. `ui/benchmarks_data.json`). Numbers are verbatim from logs.

---

## Key

- `passes` — number of improvement passes logged (1–4 for overnight; `n/a` for remaining/retry where format logs final only)
- `source` — which log file
- `‡ json=N` — `ui/benchmarks_data.json` shows a better (smaller) all-time best `N` from a prior/different run; this run did not match it

---

## Complete 119-row results table

| target     | original_len |            best_len |  delta |     pct% | passes | source            |
| ---------- | -----------: | ------------------: | -----: | -------: | :----: | ----------------- |
| comm_13_10 |        2,501 |   2,496 ‡ json=2494 |      5 |      0.2 |   1    | overnight_4pass   |
| comm_26_1  |        3,577 |               3,567 |     10 |      0.3 |   1    | overnight_4pass   |
| comm_11_1  |        3,757 |               3,744 |     13 |      0.3 |   1    | overnight_4pass   |
| comm_11_7  |        3,793 |               3,777 |     16 |      0.4 |   1    | overnight_4pass   |
| comm_22_3  |        4,163 |               4,156 |      7 |      0.2 |   1    | overnight_4pass   |
| comm_14_9  |        4,967 |               4,957 |     10 |      0.2 |   1    | overnight_4pass   |
| comm_12_10 |        4,973 |               4,964 |      9 |      0.2 |   1    | overnight_4pass   |
| comm_16_5  |        5,073 |               5,054 |     19 |      0.4 |   1    | overnight_4pass   |
| comm_21_5  |        5,371 |               5,359 |     12 |      0.2 |   1    | overnight_4pass   |
| comm_13_8  |        6,145 |               6,134 |     11 |      0.2 |   1    | overnight_4pass   |
| comm_18_4  |        7,453 |   7,440 ‡ json=7438 |     13 |      0.2 |   1    | overnight_4pass   |
| comm_26_2  |        8,341 |               4,761 |  3,580 |     42.9 |   1    | overnight_4pass   |
| comm_26_3  |        8,341 |               8,323 |     18 |      0.2 |   1    | overnight_4pass   |
| comm_12_7  |        8,457 |               3,698 |  4,759 |     56.3 |   1    | overnight_4pass   |
| comm_15_4  |        8,821 |   7,551 ‡ json=7550 |  1,270 |     14.4 |   1    | overnight_4pass   |
| comm_10_9  |        9,661 |   9,644 ‡ json=9634 |     17 |      0.2 |   1    | overnight_4pass   |
| comm_14_6  |        9,667 |               9,618 |     49 |      0.5 |   4    | overnight_4pass   |
| comm_15_7  |        9,803 |               9,767 |     36 |      0.4 |   3    | overnight_4pass   |
| comm_16_1  |        9,829 |   9,811 ‡ json=9808 |     18 |      0.2 |   1    | overnight_4pass   |
| comm_16_7  |        9,841 |               9,803 |     38 |      0.4 |   3    | overnight_4pass   |
| comm_15_10 |        9,873 |   9,856 ‡ json=9854 |     17 |      0.2 |   1    | overnight_4pass   |
| comm_18_9  |        9,877 |   9,859 ‡ json=9858 |     18 |      0.2 |   1    | overnight_4pass   |
| comm_17_9  |        9,897 |               9,880 |     17 |      0.2 |   1    | overnight_4pass   |
| comm_16_10 |        9,909 |   9,890 ‡ json=9887 |     19 |      0.2 |   1    | overnight_4pass   |
| comm_22_4  |       10,127 |              10,110 |     17 |      0.2 |   1    | overnight_4pass   |
| comm_27_3  |       10,711 |              10,686 |     25 |      0.2 |   2    | overnight_4pass   |
| comm_19_2  |       10,713 |              10,074 |    639 |      6.0 |   4    | overnight_4pass   |
| comm_20_2  |       10,717 |              10,673 |     44 |      0.4 |   4    | overnight_4pass   |
| comm_21_3  |       11,295 |              11,259 |     36 |      0.3 |   3    | overnight_4pass   |
| comm_13_9  |       12,105 |              12,073 |     32 |      0.3 |   2    | overnight_4pass   |
| comm_14_4  |       12,651 |              12,623 |     28 |      0.2 |   2    | overnight_4pass   |
| comm_17_5  |       13,425 | 13,401 ‡ json=13399 |     24 |      0.2 |   2    | overnight_4pass   |
| comm_19_3  |       13,683 | 11,275 ‡ json=11271 |  2,408 |     17.6 |   3    | overnight_4pass   |
| comm_10_5  |       14,063 |               8,991 |  5,072 |     36.1 |   3    | overnight_4pass   |
| comm_25_2  |       14,237 |               7,098 |  7,139 |     50.1 |   3    | overnight_4pass   |
| comm_32_2  |       14,271 |              14,225 |     46 |      0.3 |   4    | overnight_4pass   |
| comm_30_2  |       14,279 |              14,239 |     40 |      0.3 |   3    | overnight_4pass   |
| comm_24_2  |       14,303 |               7,171 |  7,132 |     49.9 |   2    | overnight_4pass   |
| comm_12_5  |       14,417 |               9,623 |  4,794 |     33.3 |   4    | overnight_4pass   |
| comm_17_4  |       14,593 | 14,558 ‡ json=14549 |     35 |      0.2 |   3    | overnight_4pass   |
| comm_19_5  |       14,827 |              14,781 |     46 |      0.3 |   4    | overnight_4pass   |
| comm_27_2  |       15,469 |              10,682 |  4,787 |     30.9 |   2    | overnight_4pass   |
| comm_27_4  |       15,481 |              10,690 |  4,791 |     30.9 |   2    | overnight_4pass   |
| comm_25_5  |       15,489 |              10,704 |  4,785 |     30.9 |   2    | overnight_4pass   |
| comm_11_8  |       15,617 |               8,435 |  7,182 |     46.0 |   3    | overnight_4pass   |
| comm_11_5  |       15,767 |              15,141 |    626 |      4.0 |   3    | overnight_4pass   |
| comm_20_3  |       16,075 |               8,886 |  7,189 |     44.7 |   3    | overnight_4pass   |
| comm_6_4   |       16,409 |              11,878 |  4,531 |     27.6 |   4    | overnight_4pass   |
| comm_29_2  |       16,759 |               9,627 |  7,132 |     42.6 |   2    | overnight_4pass   |
| comm_14_7  |       16,831 | 13,238 ‡ json=13236 |  3,593 |     21.3 |   2    | overnight_4pass   |
| comm_12_8  |       16,835 |              13,242 |  3,593 |     21.3 |   2    | overnight_4pass   |
| comm_13_7  |       16,837 |              16,798 |     39 |      0.2 |   3    | overnight_4pass   |
| comm_18_6  |       16,955 |              14,537 |  2,418 |     14.3 |   4    | overnight_4pass   |
| comm_17_6  |       16,967 |              14,548 |  2,419 |     14.3 |   4    | overnight_4pass   |
| comm_15_8  |       16,971 |   9,812 ‡ json=9808 |  7,159 |     42.2 |   1    | overnight_4pass   |
| comm_18_7  |       16,985 |   9,825 ‡ json=9822 |  7,160 |     42.2 |   1    | overnight_4pass   |
| comm_17_7  |       17,005 |               9,846 |  7,159 |     42.1 |   1    | overnight_4pass   |
| comm_16_8  |       17,013 |   9,852 ‡ json=9851 |  7,161 |     42.1 |   1    | overnight_4pass   |
| comm_16_3  |       17,051 |               8,618 |  8,433 |     49.5 |   4    | overnight_4pass   |
| comm_10_4  |       17,157 |              15,586 |  1,571 |      9.2 |   4    | overnight_4pass   |
| comm_17_3  |       17,539 |   8,610 ‡ json=8609 |  8,929 |     50.9 |   3    | overnight_4pass   |
| comm_10_8  |       17,923 |              13,738 |  4,185 |     23.3 |   3    | overnight_4pass   |
| comm_7_5   |       17,933 |               9,544 |  8,389 |     46.8 |   3    | overnight_4pass   |
| comm_7_6   |       18,229 | 16,379 ‡ json=16377 |  1,850 |     10.1 |   3    | overnight_4pass   |
| comm_9_4   |       18,575 | 13,075 ‡ json=13072 |  5,500 |     29.6 |   4    | overnight_4pass   |
| comm_9_5   |       18,819 |              11,678 |  7,141 |     37.9 |   4    | overnight_4pass   |
| comm_10_6  |       18,835 |              11,520 |  7,315 |     38.8 |   4    | overnight_4pass   |
| comm_14_2  |       18,857 |              16,432 |  2,425 |     12.9 |   4    | overnight_4pass   |
| comm_14_5  |       19,197 | 10,258 ‡ json=10256 |  8,939 |     46.6 |   2    | overnight_4pass   |
| comm_13_5  |       19,205 |              13,802 |  5,403 |     28.1 |   4    | overnight_4pass   |
| comm_11_4  |       19,267 | 13,807 ‡ json=13803 |  5,460 |     28.3 |   3    | overnight_4pass   |
| comm_12_3  |       19,561 | 15,036 ‡ json=15027 |  4,525 |     23.1 |   4    | overnight_4pass   |
| comm_20_5  |       19,681 |   5,390 ‡ json=5389 | 14,291 |     72.6 |   1    | overnight_4pass   |
| comm_25_3  |       20,193 |              13,050 |  7,143 |     35.4 |   3    | overnight_4pass   |
| comm_26_4  |       20,249 |               5,947 | 14,302 |     70.6 |   1    | overnight_4pass   |
| comm_12_6  |       20,415 |              13,270 |  7,145 |     35.0 |   2    | overnight_4pass   |
| comm_15_5  |       20,491 | 20,442 ‡ json=20432 |     49 |      0.2 |   4    | overnight_4pass   |
| comm_8_2   |       20,797 |              12,258 |  8,539 |     41.1 |   4    | overnight_4pass   |
| comm_11_3  |       20,841 |              11,717 |  9,124 |     43.8 |   4    | overnight_4pass   |
| comm_11_10 |       21,621 |               7,314 | 14,307 |     66.2 |   2    | overnight_4pass   |
| comm_16_4  |       21,971 |              15,790 |  6,181 |     28.1 |   4    | overnight_4pass   |
| comm_12_4  |       22,303 |              10,910 | 11,393 |     51.1 |   4    | overnight_4pass   |
| comm_8_4   |       22,675 |              16,257 |  6,418 |     28.3 |   4    | overnight_4pass   |
| comm_4_2   |       23,299 | 16,901 ‡ json=16897 |  6,398 |     27.5 |  n/a   | remaining_4pass   |
| comm_8_3   |       23,421 | 17,678 ‡ json=17677 |  5,743 |     24.5 |  n/a   | remaining_4pass   |
| comm_5_3   |       23,521 | 20,307 ‡ json=20304 |  3,214 |     13.7 |  n/a   | remaining_4pass   |
| comm_9_7   |       24,053 |              17,406 |  6,647 |     27.6 |  n/a   | remaining_4pass   |
| comm_13_6  |       24,247 |   6,191 ‡ json=6188 | 18,056 |     74.5 |  n/a   | remaining_4pass   |
| comm_21_4  |       24,385 |              10,058 | 14,327 |     58.8 |  n/a   | remaining_4pass   |
| comm_10_7  |       24,443 |              13,727 | 10,716 |     43.8 |  n/a   | remaining_4pass   |
| comm_8_5   |       24,975 | 21,083 ‡ json=21069 |  3,892 |     15.6 |  n/a   | remaining_4pass   |
| comm_15_3  |       25,445 |              14,610 | 10,835 |     42.6 |  n/a   | remaining_4pass   |
| comm_9_3   |       25,799 |              20,524 |  5,275 |     20.4 |  n/a   | remaining_4pass   |
| comm_6_2   |       26,853 | 17,798 ‡ json=17797 |  9,055 |     33.7 |  n/a   | remaining_4pass   |
| comm_6_3   |       26,963 | 16,853 ‡ json=16836 | 10,110 |     37.5 |  n/a   | remaining_4pass   |
| comm_6_1   |       27,205 | 21,031 ‡ json=21019 |  6,174 |     22.7 |  n/a   | remaining_4pass   |
| comm_9_6   |       27,335 |              11,358 | 15,977 |     58.4 |  n/a   | remaining_4pass   |
| comm_8_7   |       27,391 |              13,063 | 14,328 |     52.3 |  n/a   | remaining_4pass   |
| comm_4_3   |       27,797 |              13,016 | 14,781 |     53.2 |  n/a   | remaining_4pass   |
| comm_14_3  |       28,059 | 22,386 ‡ json=22373 |  5,673 |     20.2 |  n/a   | remaining_4pass   |
| comm_18_3  |       28,225 |              18,086 | 10,139 |     35.9 |  n/a   | remaining_4pass   |
| comm_9_8   |       28,615 | 20,261 ‡ json=20246 |  8,354 |     29.2 |  n/a   | remaining_4pass   |
| comm_12_9  |       28,653 |           **7,245** | 21,408 | **74.7** |  n/a   | remaining_4pass † |
| comm_7_3   |       28,751 | 17,726 ‡ json=17725 | 11,025 |     38.3 |  n/a   | retry_failed      |
| comm_20_4  |       29,157 |               7,743 | 21,414 |     73.4 |  n/a   | retry_failed      |
| comm_5_4   |       29,391 |              15,135 | 14,256 |     48.5 |  n/a   | retry_failed      |
| comm_13_4  |       29,509 |              19,309 | 10,200 |     34.6 |  n/a   | retry_failed      |
| comm_11_2  |       29,579 |              16,408 | 13,171 |     44.5 |  n/a   | retry_failed      |
| comm_10_3  |       31,547 |              24,636 |  6,911 |     21.9 |  n/a   | retry_failed      |
| comm_8_6   |       32,201 | 20,156 ‡ json=20143 | 12,045 |     37.4 |  n/a   | retry_failed      |
| comm_12_2  |       32,251 | 26,644 ‡ json=26643 |  5,607 |     17.4 |  n/a   | retry_failed      |
| comm_23_2  |       32,287 | 11,830 ‡ json=11827 | 20,457 |     63.4 |  n/a   | retry_failed      |
| comm_15_2  |       32,721 | 22,150 ‡ json=22137 | 10,571 |     32.3 |  n/a   | retry_failed      |
| comm_13_3  |       33,329 |              27,340 |  5,989 |     18.0 |  n/a   | retry_failed      |
| comm_17_2  |       34,771 | 20,174 ‡ json=20167 | 14,597 |     42.0 |  n/a   | retry_failed      |
| comm_7_2   |       37,071 | 23,001 ‡ json=23000 | 14,070 |     38.0 |  n/a   | retry_failed      |
| comm_6_5   |       39,411 | 23,711 ‡ json=23705 | 15,700 |     39.8 |  n/a   | retry_failed      |
| comm_7_4   |       41,229 |              20,930 | 20,299 |     49.2 |  n/a   | retry_failed      |
| comm_16_2  |       41,887 | 22,421 ‡ json=22397 | 19,466 |     46.5 |  n/a   | retry_failed      |

> † comm_12_9: log value 7,245 independently confirmed by `corrected/README.md` (chain: 28652 → 7245, abelianization (0,0) at all stages; see `corrected/final_beam.txt`).

> ‡ `json=N` entries: `ui/benchmarks_data.json` records a better all-time best `N` for that target. The JSON tracks cumulative bests across all runs; this run's result was not the best known. The source methodology for all 42 is now identified from the JSON `comment` field — see the "Provenance gap" section below.

---

## Targets absent from all three logs

None. All 119 targets present in `ui/benchmarks_data.json` appear in at least one log.

---

## Provenance gap NOT closed for 42 rows

For 42 of 119 targets, `ui/benchmarks_data.json` records a strictly better `best_len` than this run produced. All 31 previously-untraceable rows from the prior snapshot fall within this 42.

**Source methodology identified from JSON `comment` field** (not from logs — git history chase confirmed dead end: 1 commit, no history; runs were local):

| Category | Count | JSON comment | Source |
|---|---:|---|---|
| A | 8 | `Power + braid + greedy rules` | Earlier Python-only pipeline (power + braid + greedy rule application, no Rust beam). Reproducible with `reduce_coreless.py` (corrected). |
| B | 30 | `Rust beam + 7M historical rules` | Pre-benchmark-0001 run with a 7M rule bank. Run directory gone; outputs collected by `collect_best.sh`, then deleted from `benchmark_run/overnight_results/`. Rule bank not on disk. |
| C | 3 | `Lift→coreless→beam (new pipeline)` | `reduce_benchmark_v2.py` (lift-first strategy, `burnside_bidirectional` binary). Likely run on benchmark-0001 outputs as starting words — gets 9–10 chars better for these 3 targets. |
| D | 1 | `Multi-pass Rust beam + 25M biased rules (new record)` | Biased KB run for comm_16_2 only; specific run directory unlocated. |

**Disk search result (2026-06-10)**: Searched `benchmark_run/overnight_results/`, `benchmark_run/best_words/`, all per-target logs, `full_logged_progress.log` (73-word run using older `burnside/burnside_bidirectional` binary), `run_v2.log`, `analysis_output.log`, and `b25_bias_bidir/runs/*/run.log` files. `benchmark_run/overnight_results/` is empty — files were written there by earlier runs and subsequently deleted. Category B source confirmed absent from disk.

| target | this_run_best | json_best | Δ | this_run_source | cat |
|---|---:|---:|---:|---|:---:|
| comm_13_10 | 2,496 | 2,494 | 2 | overnight_4pass | A |
| comm_18_4 | 7,440 | 7,438 | 2 | overnight_4pass | A |
| comm_10_9 | 9,644 | 9,634 | 10 | overnight_4pass | A |
| comm_16_1 | 9,811 | 9,808 | 3 | overnight_4pass | A |
| comm_15_10 | 9,856 | 9,854 | 2 | overnight_4pass | A |
| comm_18_9 | 9,859 | 9,858 | 1 | overnight_4pass | A |
| comm_16_10 | 9,890 | 9,887 | 3 | overnight_4pass | A |
| comm_17_5 | 13,401 | 13,399 | 2 | overnight_4pass | A |
| comm_15_4 | 7,551 | 7,550 | 1 | overnight_4pass | B |
| comm_19_3 | 11,275 | 11,271 | 4 | overnight_4pass | B |
| comm_14_7 | 13,238 | 13,236 | 2 | overnight_4pass | B |
| comm_15_8 | 9,812 | 9,808 | 4 | overnight_4pass | B |
| comm_18_7 | 9,825 | 9,822 | 3 | overnight_4pass | B |
| comm_16_8 | 9,852 | 9,851 | 1 | overnight_4pass | B |
| comm_17_3 | 8,610 | 8,609 | 1 | overnight_4pass | B |
| comm_7_6 | 16,379 | 16,377 | 2 | overnight_4pass | B |
| comm_9_4 | 13,075 | 13,072 | 3 | overnight_4pass | B |
| comm_14_5 | 10,258 | 10,256 | 2 | overnight_4pass | B |
| comm_11_4 | 13,807 | 13,803 | 4 | overnight_4pass | B |
| comm_20_5 | 5,390 | 5,389 | 1 | overnight_4pass | B |
| comm_4_2 | 16,901 | 16,897 | 4 | remaining_4pass | B |
| comm_8_3 | 17,678 | 17,677 | 1 | remaining_4pass | B |
| comm_5_3 | 20,307 | 20,304 | 3 | remaining_4pass | B |
| comm_13_6 | 6,191 | 6,188 | 3 | remaining_4pass | B |
| comm_8_5 | 21,083 | 21,069 | 14 | remaining_4pass | B |
| comm_6_2 | 17,798 | 17,797 | 1 | remaining_4pass | B |
| comm_6_3 | 16,853 | 16,836 | 17 | remaining_4pass | B |
| comm_6_1 | 21,031 | 21,019 | 12 | remaining_4pass | B |
| comm_14_3 | 22,386 | 22,373 | 13 | remaining_4pass | B |
| comm_9_8 | 20,261 | 20,246 | 15 | remaining_4pass | B |
| comm_7_3 | 17,726 | 17,725 | 1 | retry_failed | B |
| comm_8_6 | 20,156 | 20,143 | 13 | retry_failed | B |
| comm_12_2 | 26,644 | 26,643 | 1 | retry_failed | B |
| comm_23_2 | 11,830 | 11,827 | 3 | retry_failed | B |
| comm_15_2 | 22,150 | 22,137 | 13 | retry_failed | B |
| comm_17_2 | 20,174 | 20,167 | 7 | retry_failed | B |
| comm_7_2 | 23,001 | 23,000 | 1 | retry_failed | B |
| comm_6_5 | 23,711 | 23,705 | 6 | retry_failed | B |
| comm_12_3 | 15,036 | 15,027 | 9 | overnight_4pass | C |
| comm_15_5 | 20,442 | 20,432 | 10 | overnight_4pass | C |
| comm_17_4 | 14,558 | 14,549 | 9 | overnight_4pass | C |
| comm_16_2 | 22,421 | 22,397 | 24 | retry_failed | D |

---

## Snapshot stats

| Metric | Value |
|---|---|
| Total rows | 119 |
| From overnight_4pass.log | 84 |
| From remaining_4pass.log | 19 |
| From retry_failed.log | 16 |
| Log/txt agreement | 119/119 (perfect) |
| JSON-identical (log = json best) | 77/119 |
| JSON-better (prior run holds record) | 42/119 |
| ↳ Cat A: Power+braid+greedy (Python-only, no beam) | 8/42 |
| ↳ Cat B: Rust beam + 7M historical rules (run gone) | 30/42 |
| ↳ Cat C: Lift→coreless→beam v2 pipeline | 3/42 |
| ↳ Cat D: 25M biased rules (comm_16_2 only) | 1/42 |
| Best reduction this run | comm_12_9: 74.7% (28,653→7,245) |
| Targets absent from all logs | 0 |
| JSON provenance gap | Methodology identified for all 42 (JSON comment field); Cat B run directory gone from disk |

---

## Related material

- [[reduce-core-data]] — sibling data note: rule banks, scripts, X-core constant
- [[reduce-core-results]] — comm_12_9 pipeline results; version history; main findings
- [[_progress|B(2,5) Progress Note]] — standing progress note
- [[reduce-core-pipeline-b25-2026-05-22]] — methodology note; corrected pipeline
