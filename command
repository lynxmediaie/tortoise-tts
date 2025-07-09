. /root/miniconda/etc/profile.d/conda.sh
conda activate tortoise

python do_tts.py \
  --text "再次强调，只有公民，也就是说，来自此类公民家庭的儿童。" \
  --voice "zebrak" \
  --preset "high_quality" \
  --half false \
  --output_path "/results" \
  --candidates 1


curl -X POST "http://localhost:8000/tts" -H "Content-Type: application/json" -d {  "text": "Hello, this is a test of the text-to-speech system.",  "voice": "random",  "preset": "fast",  "use_deepspeed": false,  "kv_cache": true,  "half": true,  "output_path": "results",  "model_dir": "models",  "candidates": 3,  "seed": 56343,  "produce_debug_state": true,  "cvvp_amount": 0.0}