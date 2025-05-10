@echo off
set PYTHONPATH=.
pytest --maxfail=3 -v --tb=short > test_report.txt
echo ===== 테스트 결과 요약 =====
type test_report.txt | findstr "FAILED ERROR passed"
