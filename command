. /root/miniconda/etc/profile.d/conda.sh
conda activate tortoise

python do_tts.py \
  --text "再次强调，只有公民，也就是说，来自此类公民家庭的儿童。" \
  --voice "zebrak" \
  --preset "high_quality" \
  --half false \
  --output_path "/results" \
  --candidates 1