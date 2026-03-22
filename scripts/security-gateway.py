#!/usr/bin/env python3
"""Security Gateway для DevSecOps Pipeline"""

import json
import sys
from pathlib import Path

def main():
    print("=" * 60)
    print("  🔒 SECURITY GATEWAY")
    print("=" * 60)
    
    reports_dir = Path('reports')
    bandit_report = reports_dir / 'bandit-report.json'
    
    if bandit_report.exists():
        with open(bandit_report, 'r') as f:
            data = json.load(f)
        issues = data.get('issues', [])
        print(f"\n📊 Bandit: {len(issues)} уязвимостей найдено")
        
        high = sum(1 for i in issues if i.get('issue_severity', '').upper() == 'HIGH')
        critical = sum(1 for i in issues if i.get('issue_severity', '').upper() == 'CRITICAL')
        
        print(f"  • CRITICAL: {critical}")
        print(f"  • HIGH: {high}")
        
        if critical > 0:
            print(f"\n{'=' * 60}")
            print("  🚫 RELEASE BLOCKED")
            print(f"{'=' * 60}")
            sys.exit(1)
        else:
            print(f"\n{'=' * 60}")
            print("  ✅ RELEASE APPROVED")
            print(f"{'=' * 60}")
            sys.exit(0)
    else:
        print("\n⚠️ Отчёт не найден, пропускаем проверку")
        sys.exit(0)

if __name__ == '__main__':
    main()
