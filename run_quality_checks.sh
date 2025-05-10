#!/bin/bash
export PYTHONPATH=.
pytest --maxfail=3 -v --tb=short > test_report.txt
echo "===== 테스트 결과 요약 ====="
grep -E "FAILED|ERROR|passed" test_report.txt
