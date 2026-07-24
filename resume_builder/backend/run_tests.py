#!/usr/bin/env python3
"""
Simple script to run authentication tests
"""
import subprocess
import sys

def run_tests():
    """Run all authentication related tests"""
    print("Running authentication tests...")
    
    # Run pytest with coverage for auth tests
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        "resume_builder/backend/app/tests/test_auth.py",
        "-v"
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ All authentication tests passed!")
        return True
    else:
        print("❌ Authentication tests failed:")
        print(result.stdout)
        print(result.stderr)
        return False

if __name__ == "__main__":
    run_tests()