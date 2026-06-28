# We test the functions from your transform.py
import sys
sys.path.insert(0, '.')

from transform import validate_schema

def test_validate_schema_passes_when_columns_exist():
    """Schema validation should pass when all expected columns are present."""
    class MockDF:
        columns = ["patient_id", "diagnosis", "date"]
    
    # Should not raise any error
    validate_schema(MockDF(), ["patient_id", "diagnosis"])

def test_validate_schema_fails_when_column_missing():
    """Schema validation should raise ValueError when columns are missing."""
    class MockDF:
        columns = ["patient_id"]
    
    try:
        validate_schema(MockDF(), ["patient_id", "diagnosis"])
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "diagnosis" in str(e)