# brain-preflight-checks (free lite)

**Stop wasting WorldQuant BRAIN simulations on preventable failures.**

Most simulations beginners burn don't die on bad ideas. They die on
process:

- a field name from a tutorial that **does not exist on your account**
  (availability = region × delay × universe × subscription — even one
  underscore off, like `cash_flow_op` vs the real name, fails);
- a **VECTOR** field used without `vec_avg(...)`;
- an alpha that reaches `/check` and fails at **0.7+ self-correlation**
  against something you submitted months ago;
- a `trade_when` exit argument that quietly zeroes the whole alpha.

This free lite repo gives you a runnable taste of **Gate 1** of the
three-gate workflow I now run before every submission.

## Run the demo (30 seconds)

```bash
python3 demo_check.py
```

```
OK_EXAMPLE: PASS problems=[]
TYPO_EXAMPLE: FAIL problems=['NOT_IN_CATALOG:cash_flow_op']
VECTOR_EXAMPLE: FAIL problems=['VECTOR_WITHOUT_VEC_AVG:actual_earnings_per_share_2']
VECTOR_FIXED: PASS problems=[]
```

It checks candidate expressions against a tiny **sample** field list
(10 illustrative rows in `sample_fields.csv`). Same idea, toy data.

## The three gates (full workflow)

1. **Field gate** — pull the real field catalog from *your own* account
   and validate every expression against it before simulating.
2. **Submission discipline** — simulate sequentially, respect
   `Retry-After`, recover "lost" simulations by ID before resubmitting.
3. **Self-correlation gate** — mirror your own submitted (OS) pool
   locally and estimate correlation *before* spending an official
   `/check`; treat ≥ 0.6 as a stop sign (official limit 0.7).
   In my own rounds the local estimate matched the official check
   closely — 0.871 exact once, and 0.558 local vs 0.5582 official on
   the alpha that eventually passed every check.

## Full toolkit

The paid toolkit (Basic $19 / Pro $39) contains:

- the **Pre-Submission Playbook**: the three gates in full, plus six
  expensive mistakes (the real cause of most CONCENTRATED_WEIGHT
  failures, why backfill helps slow signals and hurts fast ones, the
  news-signal turnover trap, and more);
- `fetch_my_catalog.py` — builds the field catalog of **your** account;
- `check_fields.py` — Gate 1 against your real catalog;
- Pro: `fetch_my_os_pool.py` + `local_selfcorr.py` — Gate 3 locally.

Tools and method only — **no alphas for sale, no simulation or
submission service, ever.** Your credentials stay on your machine
(environment variables), and all data comes from your own account.

👉 Get it here:
- Basic ($19): https://3569099975461.gumroad.com/l/brain-pre-submission-toolkit-basic
- Pro ($39): https://3569099975461.gumroad.com/l/brain-pre-submission-toolkit-pro

Questions or a bug in the demo? Open an issue — I answer demo issues
here; toolkit support is by message after purchase (text only).

## License

The demo script in this repo is MIT licensed. The paid toolkit and
playbook are commercial products and are not part of this repository.
